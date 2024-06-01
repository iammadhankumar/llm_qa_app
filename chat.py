# Import the required libraries
import streamlit as st
import openai

# Set up the Streamlit app
st.title("Question Answering AI Agent 🤖")
st.caption("This app allows you to ask questions and get answers using OpenAI API")

# Get OpenAI API key from user
openai_access_token = st.text_input("OpenAI API Key", type="password")

if openai_access_token:
    # Initialize the OpenAI API with the provided key
    openai.api_key = openai_access_token

    model = st.radio(
        "Select the model",
        ["gpt-3.5-turbo", "gpt-4"],
        index=0,
    )

    # Get the user prompt (question)
    user_question = st.text_input("Enter your question")

    # Generate an answer when the button is clicked
    if st.button("Get Answer"):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_question},
            ]
        )
        answer = response.choices[0].message['content'].strip()
        st.write(answer)
