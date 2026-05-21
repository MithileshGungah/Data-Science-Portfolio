import streamlit as st
import requests
import json

from config import FRONTEND_CONFIG
from session_manager import init_session_state
from ui_components import (
    display_header,
    render_document_upload_section,
    render_agent_settings_section,
    display_chat_history,
    display_trace_events
)
from backend_api import chat_with_backend_agent

# Main Streamlit application entry point
def main():

    # Initialize Streamlit session state variables
    init_session_state()

    # Backend API base URL from configuration
    fastapi_base_url = FRONTEND_CONFIG["FASTAPI_BASE_URL"]

    # Render application header
    display_header()

    # Render document upload interface
    render_document_upload_section(fastapi_base_url)

    # Render agent configuration settings
    render_agent_settings_section()

    st.markdown("---")

    # Chat interface title
    st.header("Ask AtlasWorks")

    # Display previous conversation history
    display_chat_history()

    # Handle new user input from chat box
    if prompt := st.chat_input("Ask something..."):

        # Store user message in session history
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        # Render user message in chat UI
        with st.chat_message("user"):
            st.markdown(prompt)

        # Render assistant response section
        with st.chat_message("assistant"):

            # Display loading indicator while processing
            with st.spinner("Thinking..."):

                try:
                    # Send request to backend agent API
                    response, trace = chat_with_backend_agent(
                        fastapi_base_url,
                        st.session_state.session_id,
                        prompt,
                        st.session_state.web_search_enabled
                    )

                    # Display assistant response
                    st.markdown(response)

                    # Store assistant response in session history
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response
                    })

                    # Display execution trace events
                    display_trace_events(trace)

                # Handle backend connectivity issues
                except requests.exceptions.ConnectionError:
                    st.error("Backend not running (FastAPI not reachable)")

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "Backend connection error"
                    })

                # Handle HTTP request-related errors
                except requests.exceptions.RequestException as e:
                    st.error(f"Request error: {e}")

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": str(e)
                    })

                # Handle invalid JSON responses
                except json.JSONDecodeError:
                    st.error("Invalid JSON response from backend")

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": "Invalid backend response"
                    })

                # Handle unexpected runtime errors
                except Exception as e:
                    st.error(f"Unexpected error: {e}")

                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": str(e)
                    })

# Application execution entry point
if __name__ == "__main__":
    main()