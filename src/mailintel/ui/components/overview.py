"""
Executive overview component.
"""

import streamlit as st

from mailintel.domain.investigation import Investigation


def render_overview(
    investigation: Investigation,
    domain_count: int,
    attachment_count: int = 0,
) -> None:
    """Render investigation overview."""

    risk = investigation.metadata.get(
        "risk_profile",
        {},
    )

    st.subheader("Investigation Overview")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            f"""
### Investigation

**ID**

`{investigation.id}`

**Email**

{investigation.title}
"""
        )

    with col2:
        st.metric(
            "Overall Risk",
            f"{investigation.risk_score}/100",
        )

        st.caption(f"Level: **{risk.get('level', 'UNKNOWN')}**")

    st.progress(
        investigation.risk_score / 100,
    )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Evidence",
        len(investigation.evidence),
    )

    c2.metric(
        "Findings",
        len(investigation.findings),
    )

    c3.metric(
        "Domains",
        domain_count,
    )

    c4.metric(
        "Attachments",
        attachment_count,
    )
