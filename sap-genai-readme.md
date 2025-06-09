# Brontobyte SAP GenAI PoC

This repository demonstrates a Generative AI integration with SAP using LangChain, LangGraph, and Langfuse.

This PoC demonstrates how Generative AI can be integrated with SAP systems to enhance procurement workflows using natural language queries, intelligent vendor lookup, and traceable agent orchestration.

## 🚀 Features

- **Natural Language PO Queries**: Ask questions about purchase orders in plain English
- **Vendor Autocomplete**: Smart vendor name suggestions
- **PO Detail Viewer**: Quick access to purchase order details
- **Voice Input**: Voice-to-text capabilities for hands-free operation
- **Agent Orchestration**: LangGraph-based task automation

## 📋 Prerequisites

- Python 3.8 or higher
- Streamlit Cloud account (for deployment)
- (Optional) SAP system access for actual integration

## 🔧 Setup Instructions

### 1. Clone or Download the Project
```bash
git clone https://github.com/venkatkaza/brontobyte_sap_genai_poc.git
cd brontobyte_sap_genai_poc
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Locally
```bash
streamlit run main.py
```

## 🌐 Deploying to Streamlit Cloud

### 1. Push to GitHub
Ensure your repository is pushed to GitHub with the following structure:
```
brontobyte_sap_genai_poc/
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── agents/
│   ├── __init__.py
│   └── langgraph_orchestrator.py
├── po_handler/
│   ├── __init__.py
│   ├── po_query_handler.py
│   └── po_detail_modal.py
├── vendor/
│   ├── __init__.py
│   └── vendor_autocomplete.py
├── retrievers/
│   ├── __init__.py
│   └── faiss_memory.py
├── voice/
│   ├── __init__.py
│   └── voice_to_text.py
└── bridge/
    └── anylogic_bridge_stub.py
```

### 2. Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `brontobyte_sap_genai_poc`
5. Set branch: `main`
6. Set main file path: `main.py`
7. Click "Deploy"

### 3. Environment Variables (if needed)
For production deployment with actual SAP integration, add these in Streamlit Cloud settings:
```
SAP_HOST=your_sap_host
SAP_CLIENT=your_client_id
SAP_USER=your_username
SAP_PASSWORD=your_password
OPENAI_API_KEY=your_openai_key  # For LangChain
```

## 🛠️ Current Implementation Status

### ✅ Implemented (Demo/Stub)
- Basic Streamlit UI
- PO query handling (simulated)
- Vendor autocomplete
- PO detail viewer
- Voice input simulation
- Basic agent orchestration

### 🚧 To Be Implemented
- Actual SAP RFC/REST integration
- Real LangChain/LangGraph implementation
- Langfuse tracking
- FAISS vector store
- Voice recognition
- Authentication
- Error handling
- Caching

## 📝 Usage

1. **PO Queries**: Type natural language queries like "Show me pending POs" or "What's my latest purchase order?"
2. **Vendor Search**: Start typing a vendor name to see suggestions
3. **PO Details**: Enter a PO ID to view its details
4. **Voice Input**: Click the voice button to simulate voice queries
5. **Quick Actions**: Use the sidebar buttons for common tasks

## ⚠️ Important Notes

1. **Demo Mode**: Currently all data is simulated. No actual SAP connection.
2. **Security**: Never commit real SAP credentials to the repository
3. **Scalability**: This is a PoC. Production deployment would need:
   - Proper authentication
   - Error handling
   - Rate limiting
   - Caching
   - Monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This is a proof of concept for demonstration purposes.

## 🚨 Troubleshooting

### Common Issues:

1. **Import Errors**: Ensure you're running from the project root with `main.py`
2. **Missing Dependencies**: Run `pip install -r requirements.txt`
3. **Streamlit Cloud Build Fails**: Check that all files are committed and requirements.txt is complete

## 📞 Contact

For questions about this PoC, please contact the development team.
