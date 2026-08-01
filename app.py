karfrom langchain.agents import create_agent
import langchain
from tavily import TavilyClient
import pytesseract as pyt
import streamlit as st
import os
import time
import numpy as np
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

###Load anv and api keys###
st.title("Agentic PPT Generator")

st.header("""User can generate, PPT,Images,fetch latest news""")

st.sidebar.title("Give API Keys")

TAVILY_API_KEY = "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"
GOOGLE_API_KEY = "AQ.Ab8RN6KThHBx7TihS7Znx7izlGoD5CPotjOvvwrIPv8iWvAPEA"
ALL_API = [TAVILY_API_KEY,GOOGLE_API_KEY]

if not all(ALL_API):
  st.sidebar.error("Must Pass All API-Keys")

  url = "https://aistudio.google.com/api-keys"
  st.markdown(f"Get Google AP key-{url}")

  url ="https://app.tavily.com/playground"
  st.markdown(f"Get Tavily AP key-{url}")

elif all(ALL_API):
  st. success("API KEYS LOADED")
  options = ["gemini-3.5-flash-lite", "gemini-3.5-flash",
  "gemini-2.5-flash-lite","gemini-2.5-flash"]

  selected_model = st.selectbox("Select-Model",options = options)

  model = ChatGoogleGenerativeAI(
    model = selected_model,
    google_api_key = api)

else:
  st.sidebar.info("Try Valid API-keys")
