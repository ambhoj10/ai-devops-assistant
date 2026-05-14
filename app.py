import streamlit as st
from dotenv import load_dotenv
import os

from langchain_openai import AzureChatOpenAI

# Load environment variables
load_dotenv()

# Configure Azure OpenAI
llm = AzureChatOpenAI(
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0
)

# Sidebar
st.sidebar.title("AI DevOps Assistant")

st.sidebar.markdown("""
### Supported Logs
- Kubernetes
- Docker
- Azure DevOps
- CI/CD Pipelines

### Features
✅ Root Cause Analysis  
✅ Severity Detection  
✅ Suggested Fixes  
✅ Prevention Tips
""")

# Streamlit UI
st.title("AI DevOps Assistant")

st.caption("AI-powered DevOps log analyzer using Azure OpenAI")

st.write("Analyze DevOps deployment logs using Azure OpenAI")

user_input = st.text_area(
    "Paste your DevOps log here",
    height=300,
    placeholder="Paste Kubernetes, Docker, or Azure DevOps logs..."
)

if st.button("🔍 Analyze Logs"):

    if not user_input:
        st.warning("Please enter logs")

    else:

        prompt = f"""
        You are a highly experienced Senior DevOps Engineer.

        Analyze the following DevOps deployment log carefully.

        Your response MUST follow this exact format.

        Root Cause:
        - Explain the primary issue clearly.

        Severity:
        - Critical / High / Medium / Low

        Suggested Fix:
        - Provide step-by-step fix recommendations.

        Prevention Tips:
        - Explain how to avoid this issue in future deployments.

        Deployment Log:
        {user_input}

        Keep the response concise, professional, and actionable.
        """

        with st.spinner("Analyzing logs..."):

            try:
                response = llm.invoke(prompt)

                st.subheader("📊 AI Analysis Report")

                st.markdown(response.content)

            except Exception as e:
                st.error(f"Error: {str(e)}")