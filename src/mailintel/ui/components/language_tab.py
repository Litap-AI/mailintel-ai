"""
Language intelligence tab component.
"""

import streamlit as st

from mailintel.domain.investigation import Investigation


def render_language_tab(
    investigation: Investigation,
) -> None:
    """Render language intelligence."""

    st.subheader("Language Intelligence")

    language_items = [
        item for item in investigation.evidence if item.collector == "LanguageCollector"
    ]

    if not language_items:
        st.success("No language intelligence findings.")
        return

    for item in language_items:
        metadata = item.metadata

        with st.expander(
            item.title,
            expanded=False,
        ):
            left, right = st.columns([2, 1])

            with left:
                st.write("**Description**")
                st.write(item.description)

                st.write("**Observed Value**")
                st.code(item.observed_value)

            with right:
                st.metric(
                    "Severity",
                    item.severity.value.upper(),
                )

                st.metric(
                    "Confidence",
                    f"{item.confidence:.2f}",
                )

            score = float(
                metadata.get(
                    "score",
                    0,
                )
            )

            st.write("Risk Contribution")

            st.progress(min(score / 100, 1.0))

            st.caption(f"Score: {score:.0f}/100")

            st.write(f"Matched Terms: {metadata.get('match_count', 0)}")

            matches = metadata.get(
                "matches",
                [],
            )

            if matches:
                st.write("Detected Terms")

                cols = st.columns(4)

                for index, word in enumerate(matches):
                    cols[index % 4].code(word)

            else:
                st.info("No suspicious terms detected.")

            if metadata:
                with st.expander(
                    "Metadata",
                    expanded=False,
                ):
                    st.json(metadata)
