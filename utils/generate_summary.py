def generate_gpt_summary(df):
    threats = df[df['predicted_label'] == "Threat"]
    total = len(df)
    num_threats = len(threats)

    summary = f"""
    Based on the uploaded sequences, the model identified **{num_threats} potential threats**
    out of **{total} total sequences**. The model is trained to detect synthetic biological risks
    simulating possible **CBRN-level misuse scenarios**.

    These results are part of a simulated red-team exercise and do **not** reflect real biological risk.
    """

    return summary

