def generate_gpt_summary(df):
    counts = df["predicted_type"].value_counts()
    total = len(df)
    lines = [f"Total Sequences Analyzed: **{total}**"]
    for threat_type, count in counts.items():
        percent = (count / total) * 100
        lines.append(f"- {threat_type}: **{count}** sequences ({percent:.2f}%)")
    return "\\n".join(lines)
