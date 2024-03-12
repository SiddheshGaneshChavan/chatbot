import streamlit as st
import requests

# Set up Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",
    layout="centered",
)

# Define your Google API key
API_KEY = "AIzaSyBacsmqylyAQhSXweJFZtRaRsl8OT3JWvA"

# Function to make API call and get response
# Function to make API call and get response
def make_api_call(user_input):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": user_input}]
            }
        ]
    }
    response = requests.post(url, json=data, headers=headers)
    response_json = response.json()
    if "candidates" in response_json and response_json["candidates"]:
        return response_json["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "Sorry, I couldn't understand that."


# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")

# Input field for user's message
user_prompt = st.text_input("Ask Gemini-Pro...")

# Button to trigger API call
if st.button("Send"):
    if user_prompt:
        # Display user's message
        st.write("User:", user_prompt)
        
        # Make API call and get response
        gemini_response = make_api_call(user_prompt)
        
        # Display Gemini-Pro's response
        st.write("Gemini-Pro:", gemini_response)
