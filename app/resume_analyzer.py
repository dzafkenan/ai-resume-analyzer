import streamlit as st
import openai
import os

# Load API key from Streamlit secret
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.set_page_config(page_title="Resume Analyzer", layout="centered")
st.title("🧠 AI-Powered Resume Analyzer")
st.write("Upload your resume (.txt) and receive GPT-powered feedback instantly.")

uploaded_file = st.file_uploader("📄 Upload your resume (.txt)", type=["txt"])

if uploaded_file:
    resume_text = uploaded_file.read().decode("utf-8")

    with st.spinner("Analyzing your resume..."):
        prompt = f"""
You are an AI resume reviewer. Analyze the following resume content for strengths and weaknesses. Provide:
1. A brief summary of the candidate's strengths.
2. Specific areas for improvement.
3. Suggestions to enhance clarity, tone, and relevance.

Resume Content:
\"\"\"
{resume_text}
\"\"\"
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4
            )
            feedback = response.choices[0].message.content.strip()
            st.subheader("📋 Feedback")
            st.write(feedback)
        except Exception as e:
            st.error(f"❌ Error from OpenAI API: {e}")
