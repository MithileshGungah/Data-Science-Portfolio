# rag_agent_app/frontend/backend_api.py

import requests
import json

# Uploads a PDF document to the FastAPI backend for indexing
def upload_document_to_backend(fastapi_base_url: str, uploaded_file):
    """
    Sends a PDF file to the backend upload endpoint.

    Args:
        fastapi_base_url (str): Base URL of the FastAPI backend.
        uploaded_file: Streamlit uploaded file object.

    Returns:
        dict: Parsed JSON response from the backend.

    Raises:
        requests.exceptions.RequestException: Raised for HTTP request failures.
        json.JSONDecodeError: Raised if response JSON is invalid.
    """

    # Prepare multipart form-data payload
    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    # Send upload request to backend API
    response = requests.post(
        f"{fastapi_base_url}/upload-document/",
        files=files
    )

    # Raise exception for unsuccessful HTTP responses
    response.raise_for_status()

    # Return parsed backend response
    return response.json()

# Sends a chat request to the backend RAG agent
def chat_with_backend_agent(
    fastapi_base_url: str,
    session_id: str,
    query: str,
    enable_web_search: bool
):
    """
    Sends a user query to the backend agent service.

    Args:
        fastapi_base_url (str): Base URL of the FastAPI backend.
        session_id (str): Unique session identifier.
        query (str): User input message.
        enable_web_search (bool): Enables or disables web search.

    Returns:
        tuple: (agent_response: str, trace_events: list)

    Raises:
        requests.exceptions.RequestException: Raised for HTTP request failures.
        json.JSONDecodeError: Raised if response JSON is invalid.
    """

    # Request payload sent to backend
    payload = {
        "session_id": session_id,
        "query": query,
        "enable_web_search": enable_web_search
    }

    # Send chat request to backend API
    response = requests.post(
        f"{fastapi_base_url}/chat/",
        json=payload,
        stream=False
    )

    # Raise exception for unsuccessful HTTP responses
    response.raise_for_status()

    # Parse backend JSON response
    data = response.json()

    # Extract response text and execution trace
    agent_response = data.get(
        "response",
        "Sorry, I couldn't get a response from the agent."
    )

    trace_events = data.get("trace_events", [])

    return agent_response, trace_events