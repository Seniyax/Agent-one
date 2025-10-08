import streamlit as st
from crew import run_process
import tempfile
import os
import sys

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



st.title("💰 Personal Finance Tracker Agent")

uploaded_file = st.file_uploader("Upload your expense CSV file", type=["csv"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name
    
    st.write("Analyzing your spending...")
    result = run_process(tmp_path)
    
    st.subheader("Agent Output:")
    st.write(result)
