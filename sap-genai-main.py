# main.py - Entry point for Streamlit Cloud

import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).parent))

# Import custom modules
from po_handler.po_query_handler import handle_po_query
from vendor.vendor_autocomplete import get_vendor_suggestions
from po_handler.po_detail_modal import get_po_details
from retrievers.faiss_memory import init_vector_store
from voice.voice_to_text import transcribe_voice
from agents.langgraph_orchestrator import run_agent_task

# Page configuration
st.set_page_config(
    page_title="SAP GenAI PoC", 
    layout="wide",
    page_icon="🏢"
)

# Initialize session state
if 'memory' not in st.session_state:
    st.session_state.memory = init_vector_store()

# Header
st.title("🏢 Brontobyte SAP GenAI Assistant")
st.markdown("---")

# Main layout
col1, col2 = st.columns([2, 1])

with col1:
    # Query Section
    st.markdown("### 📋 Purchase Order Query")
    query = st.text_area("Ask a question about your POs:", height=100)
    
    col_submit, col_voice = st.columns([1, 1])
    with col_submit:
        if st.button("Submit Query", type="primary", use_container_width=True):
            if query:
                with st.spinner("Processing query..."):
                    result = handle_po_query(query, st.session_state.memory)
                    st.success(result)
            else:
                st.warning("Please enter a query")
    
    with col_voice:
        if st.button("🎤 Voice Input", use_container_width=True):
            voice_query = transcribe_voice()
            st.info(f"Transcribed: {voice_query}")
            result = handle_po_query(voice_query, st.session_state.memory)
            st.success(result)
    
    # PO Details Section
    st.markdown("### 📦 PO Detail Viewer")
    po_col1, po_col2 = st.columns([3, 1])
    with po_col1:
        po_id = st.text_input("Enter PO ID:")
    with po_col2:
        if st.button("Get Details", use_container_width=True):
            if po_id:
                details = get_po_details(po_id)
                st.dataframe(pd.DataFrame(details), use_container_width=True)
            else:
                st.warning("Please enter a PO ID")

with col2:
    # Vendor Autocomplete Section
    st.markdown("### 🔍 Vendor Search")
    vendor_input = st.text_input("Start typing a vendor name:")
    if vendor_input:
        suggestions = get_vendor_suggestions(vendor_input)
        if suggestions:
            st.markdown("**Suggestions:**")
            for suggestion in suggestions:
                if st.button(suggestion, key=f"vendor_{suggestion}", use_container_width=True):
                    st.info(f"Selected: {suggestion}")
        else:
            st.info("No vendors found")
    
    # Agent Tasks Section
    st.markdown("### 🤖 Quick Actions")
    if st.button("Check Pending POs", use_container_width=True):
        result = run_agent_task("pending_pos")
        st.info(result)
    
    if st.button("View Latest PO", use_container_width=True):
        result = run_agent_task("latest_po")
        st.info(result)

# Footer
st.markdown("---")
st.markdown("### ℹ️ About")
st.info("""
This PoC demonstrates GenAI integration with SAP systems for:
- Natural language PO queries
- Intelligent vendor lookup
- Voice-enabled interactions
- Agent-based task automation
""")

# Sidebar with additional info
with st.sidebar:
    st.markdown("## 🚀 SAP GenAI PoC")
    st.markdown("### Features")
    st.markdown("""
    - ✅ Natural Language Processing
    - ✅ Vendor Autocomplete
    - ✅ PO Management
    - ✅ Voice Queries
    - ✅ Agent Orchestration
    """)
    
    st.markdown("### 📊 Statistics")
    st.metric("Pending POs", "5")
    st.metric("Total Vendors", "5")
    st.metric("Active Queries", "0")
