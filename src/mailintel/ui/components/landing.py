"""
Landing page component.
"""

import streamlit as st


def render_landing() -> None:
    """Render landing page."""

    st.subheader("Welcome")

    st.write(
        """
MailIntel AI investigates suspicious RFC822 email messages
using authentication analysis, language intelligence,
URL analysis and explainable risk assessment.
"""
    )

    st.divider()

    st.subheader("Investigation Workflow")

    st.markdown(
        """
Upload Email

⬇

Extract Evidence

⬇

Authentication Intelligence

⬇

Language & URL Intelligence

⬇

Risk Assessment

⬇

Executive Investigation Report
"""
    )

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("Investigation Modules")

        st.markdown(
            """
🛡 Authentication Intelligence

• SPF

• DKIM

• DMARC

---

🌐 URL Intelligence

• URL Extraction

• Domain Analysis

---

🧠 Language Intelligence

• Reward Language

• Credential Theft

• Financial Fraud

• Urgency Detection
"""
        )

    with right:
        st.subheader("Output")

        st.markdown(
            """
📊 Explainable Risk Profile

📄 Executive PDF Report

📁 JSON Investigation Report

📝 Evidence Timeline

🤖 AI Investigation Summary
"""
        )

    st.divider()
