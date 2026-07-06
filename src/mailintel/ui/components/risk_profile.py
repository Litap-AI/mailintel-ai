"""
Risk profile component.
"""

import streamlit as st

from mailintel.domain.investigation import Investigation


def render_risk_profile(
    investigation: Investigation,
) -> None:
    """Render category-wise investigation risk."""

    profile = investigation.metadata.get(
        "risk_profile",
        {},
    )

    st.subheader("Risk Profile")

    categories = [
        ("Authentication", profile.get("authentication", 0), 40),
        ("Language Intelligence", profile.get("language", 0), 20),
        ("URL Intelligence", profile.get("url", 0), 20),
        ("Identity", profile.get("identity", 0), 10),
        ("Attachments", profile.get("attachment", 0), 10),
    ]

    for title, score, maximum in categories:
        left, right = st.columns([5, 1])

        with left:
            st.write(title)

            st.progress(score / maximum if maximum else 0)

        with right:
            st.metric(
                "",
                f"{score}/{maximum}",
            )

    st.divider()
