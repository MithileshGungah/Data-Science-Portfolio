# rag_agent_app/backend/vectorstore.py

import os
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load API key for Pinecone service
from config import PINECONE_API_KEY

# Configure environment for Pinecone authentication
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

# Initialize Pinecone client instance
pc = Pinecone(api_key=PINECONE_API_KEY)

# Embedding model used for converting text into vector representations
# Default model produces 384-dimensional embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Vector index name used for storage and retrieval
INDEX_NAME = "langgraph-rag-index"

# Retrieve a LangChain retriever backed by Pinecone
def get_retriever():
    """Returns a retriever connected to the Pinecone vector store."""

    # Create index if it does not already exist
    if INDEX_NAME not in pc.list_indexes().names():
        print(f"Creating Pinecone index: {INDEX_NAME}")

        pc.create_index(
            name=INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

        print(f"Pinecone index created: {INDEX_NAME}")

    # Initialize vector store and expose retriever interface
    vectorstore = PineconeVectorStore(
        index_name=INDEX_NAME,
        embedding=embeddings
    )

    return vectorstore.as_retriever()

# Adds a document to the vector database after chunking
def add_document_to_vectorstore(text_content: str):
    """
    Splits input text into chunks and stores embeddings in Pinecone.
    """

    if not text_content:
        raise ValueError("Empty document content provided.")

    # Split large documents into manageable overlapping chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
    )

    # Convert raw text into LangChain document objects
    documents = text_splitter.create_documents([text_content])

    print(f"Document split into {len(documents)} chunks")

    # Initialize vector store for insertion
    vectorstore = PineconeVectorStore(
        index_name=INDEX_NAME,
        embedding=embeddings
    )

    # Store document embeddings in Pinecone
    vectorstore.add_documents(documents)

    print(f"Inserted {len(documents)} chunks into index '{INDEX_NAME}'")