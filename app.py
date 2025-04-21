import os
import sys
import streamlit as st
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'utils')))
from model_utils import classify_sequence
from generate_summary import generate_gpt_summary

st.set_page_config(page_title="CBRN-BioGuard CRISPR", page_icon="🧬", layout="wide")
st.title("🧬 CBRN-BioGuard CRISPR - Simulated Biosecurity Risk Classifier")

st.markdown("""
Welcome to **CBRN-BioGuard**, a simulated biosecurity tool designed to mimic red-teaming
scenarios in synthetic biology. This platform analyzes uploaded DNA sequences to classify
potential **CBRN (Chemical, Biological, Radiological, Nuclear)** threats using Python-based
machine learning logic. GPT is integrated to generate risk summaries based on your results.
""")

uploaded_file = st.file_uploader("📄 Upload a CSV file containing DNA sequences", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if "sequence" not in df.columns:
        st.error("The uploaded CSV must have a 'sequence' column.")
    else:
        st.success("File uploaded successfully!")
        st.dataframe(df.head())

        st.subheader("🚨 Threat Classification Results")
        df["predicted_label"], df["predicted_type"] = zip(*df["sequence"].map(classify_sequence))
        st.dataframe(df.head(20), use_container_width=True)

        if st.button("🧠 Generate GPT-style Biosecurity Summary"):
            st.info("Generating summary...")
            summary = generate_gpt_summary(df)
            st.markdown("### 🧠 GPT Summary")
            st.markdown(summary)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="⬇️ Download Classified Results",
            data=csv,
            file_name="classified_sequences.csv",
            mime="text/csv",
        )
else:
    st.warning("Please upload a CSV file to begin classification.")

