import os
import sys
from dotenv import load_dotenv
import json

# Add the current directory to path so imports work cleanly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.preprocess import load_and_chunk_data
from app.rag_engine import MovieRAG

def main():
    load_dotenv() # Load environment variables
    
    # Configuration
    DATA_PATH = os.path.join("data", "wiki_movie_plots_deduped.csv")
    INDEX_PATH = os.path.join("data", "faiss_index")

    # Initialize System
    print("--- Initializing Mini RAG System ---")
    rag = MovieRAG()
    
    if rag.load_index(INDEX_PATH):
        print(" Loaded existing embeddings from disk (Skipped API calls).")
    else:
        print("No existing index found. Creating new one...")
        try:
            # Load 500 rows (or 1000)
            docs = load_and_chunk_data(DATA_PATH, num_rows=500)
            
            # Create embeddings
            rag.ingest(docs)
            
            # Save them so we don't have to do this next time
            rag.save_index(INDEX_PATH)
            print("New index created and saved to disk.")
            
        except Exception as e:
            print(f"Error processing data: {e}")
            return
    
    print("\nSystem Ready! Type 'exit' to quit.\n")

    # Interactive Loop
    while True:
        user_query = input("\nAsk a question about movie plots: ")
        if user_query.lower() in ['exit', 'quit']:
            break
            
        try:
            print("Thinking...")
            result = rag.ask(user_query)
            
            # Pretty print the JSON result
            print("\n--- Result (JSON) ---")
            print(json.dumps(result, indent=4))
            
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()