import pandas as pd
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List

def load_and_chunk_data(file_path: str, num_rows: int = 500, chunk_size: int = 1500) -> List[Document]:
    """
    Loads movie data and chunks the plots.
    """
    print(f"Loading top {num_rows} rows from {file_path}...")
    
    # Load only necessary columns to save memory
    try:
        df = pd.read_csv(file_path)
        # Filter for entries with plots
        df = df.dropna(subset=['Plot', 'Title'])
        # Take the subset
        subset = df.head(num_rows)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find file at {file_path}. Check your data folder.")

    print("Chunking data...")
    # Using RecursiveCharacterTextSplitter
    # ~1500 chars is roughly 300-400 words
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=150,
        length_function=len,
    )

    documents = []
    for _, row in subset.iterrows():
        # create chunks for this movie
        chunks = splitter.split_text(row['Plot'])
        
        for chunk in chunks:
            # Create a Document object with metadata
            doc = Document(
                page_content=chunk,
                metadata={"title": row['Title'], "release_year": row.get('Release Year', 'Unknown')}
            )
            documents.append(doc)
            
    print(f"Created {len(documents)} chunks from {num_rows} movies.")
    return documents