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

    st.progress(min(investigation.risk_score / 100.0, 1.0))

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Risk Score", investigation.risk_score)
    m2.metric("Evidence", len(investigation.evidence))
    m3.metric("Findings", len(investigation.findings))
    m4.metric("Domains", len(domains["url_domains"]))

    st.divider()

    tabs = st.tabs(
        [
            "📋 Evidence",
            "🚨 Findings",
            "🤖 AI Summary",
            "🌐 Domains",
            "🧠 Language",
            "📄 Report",
        ]
    )

    # --------------------------------------------------
    # Evidence
    # --------------------------------------------------

    with tabs[0]:
        for evidence in investigation.evidence:
            with st.expander(evidence.title):
                st.write(f"**Severity:** {evidence.severity.value.upper()}")

                st.write(f"**Collector:** {evidence.collector}")

                st.code(evidence.observed_value)

                st.write(evidence.description)

    # --------------------------------------------------
    # Findings
    # --------------------------------------------------

    with tabs[1]:
        if investigation.findings:
            for finding in investigation.findings:
                st.error(f"### {finding.title}")

                st.write(finding.description)

                st.caption(f"Confidence: {finding.confidence:.2f}")

                st.divider()

        else:
            st.success("No findings detected.")

    # --------------------------------------------------
    # AI Summary
    # --------------------------------------------------

    with tabs[2]:
        st.info(summary)

    # --------------------------------------------------
    # Domains
    # --------------------------------------------------

    with tabs[3]:
        st.subheader("URL Domains")

        if domains["url_domains"]:
            for domain in domains["url_domains"]:
                st.code(domain)

        else:
            st.success("No domains detected.")

    # --------------------------------------------------
    # Language Intelligence
    # --------------------------------------------------

    with tabs[4]:
        st.subheader("Language Intelligence")

        language_items = [
            item for item in investigation.evidence if item.collector == "LanguageCollector"
        ]

        if not language_items:
            st.success("No language intelligence findings.")

        else:
            for item in language_items:
                metadata = item.metadata

                with st.expander(item.title):
                    st.write(f"**Severity:** {item.severity.value.upper()}")

                    st.progress(
                        min(
                            float(metadata.get("score", 0)) / 100,
                            1.0,
                        )
                    )

                    st.write(f"**Score:** {metadata.get('score', 0)}")

                    st.write(f"**Matches:** {metadata.get('match_count', 0)}")

                    matches = metadata.get("matches", [])

                    if matches:
                        st.write("Matched Terms")

                        for word in matches:
                            st.code(word)

    # --------------------------------------------------
    # Report
    # --------------------------------------------------

    with tabs[5]:
        st.subheader("Investigation Report")

        st.json(report)

        st.download_button(
            "⬇ Download JSON Report",
            data=json.dumps(
                report,
                indent=2,
            ),
            file_name="investigation_report.json",
            mime="application/json",
        )
