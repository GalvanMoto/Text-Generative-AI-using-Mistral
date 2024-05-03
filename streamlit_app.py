import streamlit as st
import requests

# Streamlit UI
st.title("Conversation Generator")

# Flask server URL
FLASK_URL = "http://localhost:5000/generate_text"

# User input
user_input = st.text_area("Enter your prompt here:")

# Conversation initiation
if st.button("Generate Text"):
    # Make a request to the Flask server
    response = requests.post(FLASK_URL, json={"prompt": user_input})
    
    # Parse the response
    if response.status_code == 200:
        data = response.json()
        generated_text = data.get("output")
        st.text("Generated Text:")
        st.write(generated_text)
    else:
        st.error("Failed to generate text. Please try again.")
