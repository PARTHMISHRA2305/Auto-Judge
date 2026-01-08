import streamlit as st
import joblib
import numpy as np
import pandas as pd
import re


# Load models
classifier = joblib.load("classifier.pkl")
regressor = joblib.load("regressor.pkl")

st.title("AutoJudge: ML-Based Problem Difficulty Estimator")

# Inputs
st.subheader("Enter Problem Details")
problem_desc = st.text_area("Problem Description")
input_format = st.text_area("Input Format Description")
output_format = st.text_area("Output Format Description")

# Predict button
if st.button("Predict Difficulty"):
    
    # Validation
    if not problem_desc.strip() or not input_format.strip() or not output_format.strip():
        st.warning("All fields are required. Please complete them before predicting.")
    else:

        # Combine text
        combined_text = f"{problem_desc} {input_format} {output_format}"

        # Feature engineering
        total_length = len(combined_text)
        math_count = len(re.findall(r"[=<>+\-*/^]", combined_text))

        keywords = ["dp", "graph", "tree", "recursion", "greedy", "modulo"]
        keyword_features = {
            kw: len(re.findall(rf"\b{kw}\b", combined_text.lower()))
            for kw in keywords
        }

        # Prepare DataFrame
        features = {
            "text": combined_text,
            "text_length": total_length,
            "math_symbols": math_count,
            **keyword_features
        }
        input_data = pd.DataFrame([features])

        # Predictions
        predicted_class = classifier.predict(input_data)[0]
        predicted_log = regressor.predict(input_data)[0]
        predicted_score = np.expm1(predicted_log)

        # Output
        st.success(f"**Predicted Difficulty Level:** {predicted_class}")
        st.success(f"**Predicted Difficulty Score:** {round(predicted_score, 2)}")
