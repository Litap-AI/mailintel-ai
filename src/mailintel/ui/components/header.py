"""
MailIntel UI Header Component.
"""

import streamlit as st


def render_header() -> None:
    """Render the application header."""

    st.markdown(
        """
# 📧 MailIntel AI

### Evidence-Driven Email Investigation Platform

Analyze suspicious RFC822 emails using explainable AI,
rule-based investigation workflows, and enterprise-style
investigation reporting.
"""
    )

    st.divider()
