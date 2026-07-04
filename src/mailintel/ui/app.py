import json
import tempfile
from pathlib import Path

import streamlit as st

from mailintel.ai import InvestigationSummaryEngine
from mailintel.intelligence import DomainIntelligence
from mailintel.reporting import ReportBuilder
from mailintel.workflows.analyze_email import AnalyzeEmailWorkflow

st.set_page_config(
    page_title="MailIntel AI",
    page_icon="📧",
    layout="wide",
)

workflow = AnalyzeEmailWorkflow()
summary_engine = InvestigationSummaryEngine()
domain_engine = DomainIntelligence()
report_builder = ReportBuilder()

st.title("📧 MailIntel AI")
st.caption("Evidence-Driven Email Investigation Platform")

uploaded_file = st.file_uploader(
    "Upload Email (.eml)",
    type=["eml"],
)

if uploaded_file is not None:
    with st.spinner("Analyzing email..."):
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".eml",
        ) as tmp:
            tmp.write(uploaded_file.read())
            email_path = Path(tmp.name)

        investigation = workflow.run(email_path)

    summary = summary_engine.generate(investigation)
    domains = domain_engine.extract(investigation)
    report = report_builder.build(investigation)

    st.success("Investigation Complete")

    st.progress(min(investigation.risk_score / 100, 1.0))

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Risk", f"{investigation.risk_score}/100")
    c2.metric("Evidence", len(investigation.evidence))
    c3.metric("Findings", len(investigation.findings))
    c4.metric("Domains", len(domains["url_domains"]))

    st.divider()

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📋 Evidence",
            "🚨 Findings",
            "🤖 AI Summary",
            "🌐 Domains",
            "📄 Report",
        ]
    )

    with tab1:
        for evidence in investigation.evidence:
            with st.expander(evidence.title):
                st.write(f"Severity: **{evidence.severity.value.upper()}**")
                st.write(f"Collector: **{evidence.collector}**")
                st.code(evidence.observed_value)
                st.write(evidence.description)

    with tab2:
        if investigation.findings:
            for finding in investigation.findings:
                st.error(f"### {finding.title}")
                st.write(finding.description)

        else:
            st.success("No findings.")

    with tab3:
        st.info(summary)

    with tab4:
        st.subheader("URL Domains")

        for domain in domains["url_domains"]:
            st.code(domain)

    with tab5:
        st.subheader("Investigation Report")

        st.json(report)

        st.download_button(
            "⬇ Download JSON Report",
            data=json.dumps(report, indent=2),
            file_name="investigation_report.json",
            mime="application/json",
        )
