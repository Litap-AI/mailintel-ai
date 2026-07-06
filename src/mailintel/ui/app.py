import json
import tempfile
from pathlib import Path

import streamlit as st

from mailintel.ai import InvestigationSummaryEngine
from mailintel.intelligence import DomainIntelligence
from mailintel.reporting import ReportBuilder
from mailintel.reporting.pdf import PDFReportGenerator
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
pdf_generator = PDFReportGenerator()


st.title("📧 MailIntel AI")
st.caption("Evidence-Driven Email Investigation Platform")

MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 MB

uploaded_file = st.file_uploader(
    "Upload RFC822 Email (.eml)",
    type=["eml"],
    help=("Supported format: RFC822 (.eml)\nMaximum files: 1\nMaximum size: 25 MB"),
)

if uploaded_file is not None:
    file_size = uploaded_file.size

    if file_size > MAX_FILE_SIZE:
        st.error("File exceeds the maximum size of 25 MB.")
        st.stop()

        st.info(
            f"""
    **Selected File**

    • Name: {uploaded_file.name}

    • Size: {file_size / (1024 * 1024):.2f} MB
    """
        )

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

    risk_profile = investigation.metadata.get("risk_profile", {})

    risk_level = risk_profile.get("level", "UNKNOWN")

    level_color = {
        "VERY LOW": "🟢",
        "LOW": "🟡",
        "MEDIUM": "🟠",
        "HIGH": "🔴",
        "CRITICAL": "⚫",
    }

    st.subheader("Overall Investigation Risk")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.metric(
            "Risk Score",
            f"{investigation.risk_score}/100",
        )

        st.progress(
            investigation.risk_score / 100,
        )

    with col2:
        st.markdown(f"## {level_color.get(risk_level, '⚪')} {risk_level}")

    st.divider()

    m1, m2, m3 = st.columns(3)

    m1.metric(
        "Evidence",
        len(investigation.evidence),
    )

    m2.metric(
        "Findings",
        len(investigation.findings),
    )

    m3.metric(
        "Domains",
        len(domains["url_domains"]),
    )

    st.subheader("Risk Profile")

    authentication = risk_profile.get("authentication", 0)
    language = risk_profile.get("language", 0)
    url = risk_profile.get("url", 0)
    identity = risk_profile.get("identity", 0)
    attachment = risk_profile.get("attachment", 0)

    st.write("Authentication")
    st.progress(authentication / 40)
    st.caption(f"{authentication} / 40")

    st.write("Language Intelligence")
    st.progress(language / 20)
    st.caption(f"{language} / 20")

    st.write("URL Intelligence")
    st.progress(url / 20)
    st.caption(f"{url} / 20")

    st.write("Identity")
    st.progress(identity / 10)
    st.caption(f"{identity} / 10")

    st.write("Attachments")
    st.progress(attachment / 10)
    st.caption(f"{attachment} / 10")

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

        with tempfile.TemporaryDirectory() as tmp_dir:
            pdf_path = pdf_generator.generate(
                investigation=investigation,
                summary=summary,
                report=report,
                output_path=Path(tmp_dir) / f"{investigation.id}.pdf",
            )

            with open(pdf_path, "rb") as pdf_file:
                st.download_button(
                    label="📄 Download Executive PDF",
                    data=pdf_file.read(),
                    file_name=f"{investigation.id}.pdf",
                    mime="application/pdf",
                )

        st.download_button(
            label="📁 Download JSON Report",
            data=json.dumps(
                report,
                indent=2,
            ),
            file_name=f"{investigation.id}.json",
            mime="application/json",
        )
