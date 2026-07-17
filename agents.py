import os
import json
import re

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted

from prompts import (
    MASTER_ANALYZER_PROMPT,
    JD_MATCH_PROMPT
)

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    api_key = st.secrets.get("GEMINI_API_KEY")

st.write("API Key Loaded:", api_key is not None)
st.write("Key Prefix:", api_key[:5] if api_key else "None")
st.stop()


# ---------------------------------------------------------
# CLEAN JSON
# ---------------------------------------------------------

def clean_json(text):

    text = text.replace("```json", "")
    text = text.replace("```", "").strip()

    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        return match.group()

    return text


# ---------------------------------------------------------
# COMMON GEMINI FUNCTION
# ---------------------------------------------------------

def run_json_agent(prompt):

    try:

        response = model.generate_content(prompt)

    except ResourceExhausted:

        raise Exception(
            "Gemini API quota exceeded. Please try again later."
        )

    text = clean_json(response.text)

    try:

        return json.loads(text)

    except Exception:

        print("=" * 60)
        print(text)
        print("=" * 60)

        raise


# ---------------------------------------------------------
# MASTER RESUME ANALYZER
# ---------------------------------------------------------

def analyze_resume(resume_text):

    prompt = MASTER_ANALYZER_PROMPT.format(
        resume=resume_text
    )

    return run_json_agent(prompt)


# ---------------------------------------------------------
# JOB DESCRIPTION MATCH
# ---------------------------------------------------------

def job_match_analysis(resume_text, job_description):

    prompt = JD_MATCH_PROMPT.format(

        resume=resume_text,

        job_description=job_description

    )

    return run_json_agent(prompt)