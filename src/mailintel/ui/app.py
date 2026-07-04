import tempfile
from pathlib import Path

import streamlit as st

from mailintel.workflows.analyze_email import (
    AnalyzeEmailWorkflow,
)

st.set_page_config(
    page_title="MailIntel AI",
    page_icon="📧",
    layout="wide",
)

st.title("📧 MailIntel AI")

st.caption("Evidence Driven Email Investigation Platform")

uploaded_file = st.file_uploader(
    "Upload an Email (.eml)",
    type=["eml"],
)

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".eml",
    ) as tmp:
        tmp.write(uploaded_file.read())

        email_path = Path(tmp.name)

    workflow = AnalyzeEmailWorkflow()

    investigation = workflow.run(email_path)

    st.success("Analysis Complete")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Risk Score",
            f"{investigation.risk_score}/100",
        )

    with col2:
        st.metric(
            "Evidence",
            len(investigation.evidence),
        )

    st.divider()

    st.subheader("Evidence")

    for evidence in investigation.evidence:
        st.write(f"**{evidence.title}**")

        st.write(f"Severity : {evidence.severity.value}")

        st.write(f"Value : {evidence.observed_value}")

        st.write("---")

    st.subheader("Findings")

    for finding in investigation.findings:
        st.warning(finding.title)
