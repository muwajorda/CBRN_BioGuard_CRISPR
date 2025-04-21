import streamlit as st
import pandas as pd
from utils.model_utils import classify_sequence
from utils.generate_summary import generate_gpt_summary

st.set_page_config(page_title="CBRN-BioGuard", layout="wide")

st.title("🧬 CBRN-BioGuard - Simulated Biosecurity Risk Classifier")

uploaded_file = st.file_uploader("Upload a CSV file with DNA sequences", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Sample of Uploaded Data", df.head())

    st.subheader("Classification Results")
    df["predicted_label"], df["predicted_type"] = zip(*df["sequence"].map(classify_sequence))
    st.dataframe(df.head())

    if st.button("Generate Risk Summary"):
        summary = generate_gpt_summary(df)
        st.markdown("### 🧠 GPT Risk Summary")
        st.markdown(summary)

