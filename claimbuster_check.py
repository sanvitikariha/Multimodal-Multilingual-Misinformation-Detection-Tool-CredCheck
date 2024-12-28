# claimbuster_check.py
import requests
import streamlit as st

API_KEY = ""
API_ENDPOINT = ""

def check_claim(sentences):
    url = f"{API_ENDPOINT}{requests.utils.quote(sentences)}"
    headers = {"x-api-key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"HTTP {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": str(e)}
    
