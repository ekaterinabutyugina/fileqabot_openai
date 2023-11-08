import streamlit as st
import openai
import yaml

# Open Credentials

try:
    with open('chatgpt_api_credentials1.yml', 'r') as file:
        creds = yaml.safe_load(file)
except:
    creds = {}

# Open Sidebar
with st.sidebar:
    openai_api_key = creds.get('openai_key', '')

    if openai_api_key:
        st.text("OpenAI API Key provided")
    else:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    # adding a hyperlink
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

# Set Title:
st.title("📝 File Q&A with ChatGPT")

# Upload the file:
uploaded_file = st.file_uploader("Upload an article", type=("txt", "md"))

# Text input:
question = st.text_input(
    "Ask something about the article",
    placeholder="Can you give me a short summary?",
    disabled=not uploaded_file
)
if uploaded_file and question and not openai_api_key:
    st.info("Please add your OpenAI API key to continue.")

if uploaded_file and question and openai_api_key:
    # Parsing the text:
    article = uploaded_file.read().decode()
    # st.text(article)

    # Prompting:
    my_prompt = f"""Here's an article {article}.\n\n
        \n\n\n\n{question}"""
    # st.text(my_prompt)

    # ChatGPT Connection:
    openai.api_key = openai_api_key
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=my_prompt,
        temperature=0,
    )

    response

    st.write("### Answer")
    st.write(response['choices'][0]['text'])
