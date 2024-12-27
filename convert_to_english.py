# convert_to_english.py
import os
import google.generativeai as genai
import absl.logging
import streamlit as st

# Initialize Abseil logging to suppress warnings
absl.logging.set_verbosity(absl.logging.ERROR)
absl.logging.set_stderrthreshold(absl.logging.ERROR)

# Set up your API key (replace with your actual API key)
os.environ['GOOGLE_API_KEY'] = ""
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Load the desired model
model = genai.GenerativeModel("gemini-1.0-pro")

def translation(query):
    prompt = f"Convert this '{query}' to English language."
    response = model.generate_content(prompt, stream=True)
    translation = ""
    for chunk in response:
        translation += chunk.text
    return translation.strip()

