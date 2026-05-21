import streamlit as st
from backend_api import upload_document_to_backend, chat_with_backend_agent

# Applies global custom styling for the Streamlit application
def apply_global_styles():

    st.markdown(
        """
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap');

        :root{
            --bg1:#120a03;
            --bg2:#0b0f14;
            --bg3:#070a10;

            --orange:#f97316;
            --orange-soft:#fb923c;
            --orange-deep:#c2410c;

            --text:#e5e7eb;
            --muted:#94a3b8;

            --green:#22c55e;
            --green-soft:#4ade80;
            --green-deep:#16a34a;
        }

        /* Main application background and typography */
        .stApp {
            background: radial-gradient(circle at 20% 20%, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
            font-family: 'Inter', system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
            color: var(--text);
        }

        /* Main page layout spacing */
        .block-container {
            padding-top: 1rem;
            padding-left: 2.5rem;
            padding-right: 2.5rem;
        }

        /* Header section container */
        .header-container {
            padding: 2.2rem 2rem 1.6rem 2rem;
            margin-bottom: 1.2rem;
            border-bottom: 1px solid rgba(249,115,22,0.25);
        }

        /* Main application title */
        .title {
            font-size: 2.35rem;
            font-weight: 700;
            color: var(--orange);
            letter-spacing: 0.4px;
        }

        /* Application subtitle styling */
        .subtitle {
            margin-top: 0.6rem;
            font-size: 1rem;
            color: var(--muted);
            max-width: 900px;
            line-height: 1.5;
        }

        /* Sidebar appearance */
        section[data-testid="stSidebar"] {
            background-color: rgba(10, 10, 12, 0.92);
            border-right: 1px solid rgba(249,115,22,0.15);
            backdrop-filter: blur(12px);
        }

        /* Chat row layout */
        .chat-row {
            display: flex;
            width: 100%;
            margin: 0.65rem 0;
        }

        /* User message styling */
        .chat-user {
            margin-left: auto;
            max-width: 75%;
            background: linear-gradient(135deg, #1f2937, #0f172a);
            color: #e5e7eb;
            padding: 0.85rem 1rem;
            border-radius: 12px;
            border: 1px solid rgba(148,163,184,0.18);
        }

        /* Assistant message styling */
        .chat-assistant {
            margin-right: auto;
            max-width: 75%;
            background: linear-gradient(135deg, rgba(249,115,22,0.12), rgba(11,18,32,0.9));
            color: #ffedd5;
            padding: 0.85rem 1rem;
            border-radius: 12px;
            border: 1px solid rgba(249,115,22,0.25);
            transition: all 0.25s ease;
        }

        /* Assistant message hover effect */
        .chat-assistant:hover {
            background: linear-gradient(135deg, rgba(249,115,22,0.25), rgba(11,18,32,0.95));
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(249,115,22,0.15);
        }

        /* Shared button styling */
        .stButton button {
            background: linear-gradient(135deg, rgba(249,115,22,0.18), rgba(11,18,32,0.9));
            color: #ffedd5;
            border: 1px solid rgba(249,115,22,0.35);
            border-radius: 12px;
            padding: 0.55rem 1rem;
            font-weight: 500;
            transition: all 0.25s ease;
            box-shadow: 0 6px 18px rgba(0,0,0,0.35);
        }

        /* Button hover animation */
        .stButton button:hover {
            transform: translateY(-2px) scale(1.01);
            border-color: rgba(249,115,22,0.6);
            box-shadow: 0 10px 26px rgba(249,115,22,0.18);
        }

        /* Button active state */
        .stButton button:active {
            transform: scale(0.98);
        }

        /* Text input field styling */
        .stTextInput input {
            background-color: rgba(15, 23, 42, 0.75);
            border: 1px solid rgba(249,115,22,0.25);
            color: #e5e7eb;
            border-radius: 10px;
        }

        /* Focus state for text input */
        .stTextInput input:focus {
            border: 2px solid var(--green);
            box-shadow: 0 0 0 3px rgba(34,197,94,0.15);
        }

        /* Chat input send button styling */
        div[data-testid="stChatInput"] button {
            background: linear-gradient(135deg, rgba(34,197,94,0.25), rgba(74,222,128,0.15));
            border: 1px solid rgba(34,197,94,0.6);
            color: #dcfce7;
            border-radius: 10px;
            transition: all 0.25s ease;
        }

        /* Chat send button hover effect */
        div[data-testid="stChatInput"] button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 15px rgba(34,197,94,0.35);
            border-color: rgba(74,222,128,0.9);
        }

        /* Horizontal divider styling */
        hr {
            border: none;
            border-top: 1px solid rgba(249,115,22,0.15);
        }

        </style>
        """,
        unsafe_allow_html=True
    )

# Displays application title and subtitle
def display_header():

    apply_global_styles()

    st.markdown(
        """
        <div class="header-container">
            <div class="title">AtlasWorks Policy Assistant</div>
            <div class="subtitle">
                Secure enterprise intelligence system for policy retrieval, compliance guidance, and internal knowledge discovery across organizational documents
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Renders sidebar section for PDF uploads
def render_document_upload_section(fastapi_base_url: str):

    with st.sidebar:

        st.markdown("### Policy Documents")

        # File uploader for PDF documents
        uploaded_file = st.file_uploader("Upload PDF", type="pdf")

        # Trigger upload process
        if st.button("Upload Document", use_container_width=True):

            if uploaded_file:

                with st.spinner("Processing document..."):

                    try:
                        # Upload document to backend API
                        res = upload_document_to_backend(
                            fastapi_base_url,
                            uploaded_file
                        )

                        st.success(f"{res.get('filename')} uploaded")

                    except Exception as e:
                        st.error(f"Upload failed: {e}")

            else:
                st.warning("Select a file first")

# Renders sidebar settings for agent configuration
def render_agent_settings_section():

    with st.sidebar:

        st.markdown("---")
        st.markdown("### System Settings")

        # Toggle external web search functionality
        st.session_state.web_search_enabled = st.toggle(
            "External Search",
            value=st.session_state.web_search_enabled
        )

# Displays chat history from session state
def display_chat_history():

    for msg in st.session_state.messages:

        # Render user messages
        if msg["role"] == "user":

            st.markdown(
                f"<div class='chat-row'><div class='chat-user'>{msg['content']}</div></div>",
                unsafe_allow_html=True
            )

        # Render assistant messages
        else:

            st.markdown(
                f"<div class='chat-row'><div class='chat-assistant'>{msg['content']}</div></div>",
                unsafe_allow_html=True
            )

# Displays LangGraph execution trace events
def display_trace_events(trace_events):

    if not trace_events:
        return

    with st.expander("Execution Trace"):

        for event in trace_events:

            # Display node name
            st.markdown(f"**{event.get('node_name', 'step')}**")

            # Display event description
            st.write(event.get("description", ""))

            # Display structured event details if available
            if event.get("details"):
                st.json(event["details"])
