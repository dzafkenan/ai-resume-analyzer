import streamlit as st
from openai import OpenAI
import os

# Load API key from Streamlit secrets
client = OpenAI()

# Set page config
st.set_page_config(page_title="AI-Powered Resume Analyzer")

# Title
st.title("📄 AI-Powered Resume Analyzer")
st.write("Upload your resume to receive an AI-generated analysis.")

# File uploader
uploaded_file = st.file_uploader("Upload a .txt version of your resume", type="txt")

# If a file is uploaded
if uploaded_file is not None:
    resume_text = uploaded_file.read().decode("utf-8")

    st.subheader("Resume Content:")
    st.code(resume_text, language="text")

    # Analyze button
    if st.button("Analyze Resume"):
        with st.spinner("Analyzing..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a professional career coach. Analyze the user's resume "
                                "and provide constructive feedback on how they can improve it. "
                                "Focus on clarity, impact, formatting, and relevance for technical roles."
                            ),
                        },
                        {
                            "role": "user",
                            "content": resume_text,
                        },
                    ],
                )
                ai_feedback = response.choices[0].message.content
                st.success("Analysis Complete!")
                st.subheader("AI Feedback:")
                st.write(ai_feedback)
            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
