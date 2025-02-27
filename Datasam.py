import streamlit as st
import pandas as pd
import openai

# Set up the page configuration
st.set_page_config(page_title="Data Report", layout="wide")

# File uploaders
st.title("Upload Files")
summary_file = st.file_uploader("Upload Summary CSV", type="csv")
detail_file = st.file_uploader("Upload Detail CSV", type="csv")
appendix_file = st.file_uploader("Upload Appendix Text", type="txt")

# Load data if files are uploaded
if summary_file is not None:
    summary_data = pd.read_csv(summary_file)
    st.title("Summary Report")
    st.dataframe(summary_data)

if detail_file is not None:
    detail_data = pd.read_csv(detail_file)

if appendix_file is not None:
    appendix_text = appendix_file.read().decode("utf-8")
    st.subheader("Appendix")
    st.write(appendix_text)

# ChatGPT API setup
import os

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to get insights from ChatGPT
def get_insights(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content'].strip()

# Generate insights
st.subheader("Insights from ChatGPT")
insights_messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Provide a brief summary of insights from the data."}
]
insights = get_insights(insights_messages)
st.write(insights)

# User query input
st.subheader("Enter your query")
user_query = st.text_input("Query:")

# Store user queries
if "user_queries" not in st.session_state:
    st.session_state["user_queries"] = []

if user_query:
    st.session_state["user_queries"].append(user_query)
    st.write("Your query has been stored.")

# Provide evidence link
st.subheader("Evidence")
st.write("[Link to detailed data evidence](#)")

# Note: Replace 'path/to/summary.csv' and 'path/to/detail.csv' with actual file paths.
# Replace 'your_openai_api_key' with your actual OpenAI API key.