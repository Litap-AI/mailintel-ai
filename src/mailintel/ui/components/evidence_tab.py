"""
Evidence tab component.
"""

import streamlit as st

from mailintel.domain.investigation import Investigation


def render_evidence_tab(
    investigation: Investigation,
) -> None:
    """Render collected evidence."""

    st.subheader("Collected Evidence")

    if not investigation.evidence:
        st.info("No evidence collected.")
        return

    for evidence in investigation.evidence:
        with st.expander(
            f"{evidence.title} ({evidence.severity.value.upper()})",
            expanded=False,
        ):
            left, right = st.columns(2)

            with left:
                st.write("**Collector**")
                st.write(evidence.collector)

                st.write("**Category**")
                st.write(evidence.category.value)

                st.write("**Source**")
                st.write(evidence.source.value)

            with right:
                st.write("**Severity**")
                st.write(evidence.severity.value.upper())

                st.write("**Confidence**")
                st.write(f"{evidence.confidence:.2f}")

                st.write("**Observed Value**")
                st.code(evidence.observed_value)

            st.write("**Description**")
            st.write(evidence.description)

            if evidence.references:
                st.write("**References**")

                for reference in evidence.references:
                    st.write(f"- {reference}")

            if evidence.metadata:
                st.write("**Metadata**")

                st.json(evidence.metadata)
