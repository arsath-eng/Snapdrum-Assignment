import os
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings, ChatNVIDIA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

# Define the desired JSON structure using Pydantic
class AnswerOutput(BaseModel):
    answer: str = Field(description="The natural language answer to the user's question.")
    contexts: List[str] = Field(description="A list of direct plot snippets used to answer the question.")
    reasoning: str = Field(description="A short explanation of how the answer was formed based on the context.")

class MovieRAG:
    def __init__(self):
        # Ensure API Key is loaded
        if not os.getenv("NVIDIA_API_KEY"):
            raise ValueError("NVIDIA_API_KEY not found in environment variables.")

        # 1. Initialize NVIDIA Embeddings
        # 'nvidia/nv-embed-v1' is a strong standard embedding model
        self.embeddings = NVIDIAEmbeddings(model="nvidia/nv-embed-v1", truncate="END")
        
        # 2. Initialize LLM
        # 'meta/llama-3.1-70b-instruct' is powerful and available via NVIDIA NIM
        self.llm = ChatNVIDIA(model="meta/llama-3.1-70b-instruct", temperature=0.1)
        
        self.vector_store = None
        self.retriever = None

    def ingest(self, documents):
        """Embeds documents and creates the FAISS index."""
        print("Embedding documents and building Vector Store (this may take a moment)...")
        self.vector_store = FAISS.from_documents(documents, self.embeddings)
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})
        print("Vector Store ready.")

    def save_index(self, folder_path: str):
        """Saves the FAISS index to disk."""
        if self.vector_store:
            self.vector_store.save_local(folder_path)
            print(f"Index saved to {folder_path}")
        else:
            print("No vector store to save.")

    
    def load_index(self, folder_path: str):
        """Loads the FAISS index from disk."""
        if os.path.exists(folder_path):
            print(f"Loading index from {folder_path}...")
            # allow_dangerous_deserialization is required for FAISS safety since v0.1
            self.vector_store = FAISS.load_local(
                folder_path, 
                self.embeddings, 
                allow_dangerous_deserialization=True
            )
            self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 3})
            print("Index loaded successfully.")
            return True
        return False

    def ask(self, query: str):
        """Retrieves context and generates a structured answer."""
        if not self.vector_store:
            return "Please ingest data first."

        # Retrieve relevant docs
        docs = self.retriever.invoke(query)
        context_text = "\n\n".join([f"Movie: {d.metadata['title']}\nPlot: {d.page_content}" for d in docs])

        # Setup Parser
        parser = JsonOutputParser(pydantic_object=AnswerOutput)

        # Prompt Template
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful movie assistant. Answer the user question based ONLY on the provided context. \n"
                       "Output must be valid JSON following this format:\n{format_instructions}"),
            ("user", "Context:\n{context}\n\nQuestion: {question}")
        ])

        # Build Chain
        chain = prompt | self.llm | parser

        # Execute
        response = chain.invoke({
            "context": context_text,
            "question": query,
            "format_instructions": parser.get_format_instructions()
        })
        
        return response