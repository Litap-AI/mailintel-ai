"""
MailIntel UI Footer Component.
"""

from datetime import UTC, datetime

import streamlit as st


def render_footer() -> None:
    """Render application footer."""

    st.divider()

    generated = datetime.now(UTC).strftime("%d %b %Y %H:%M UTC")

    st.caption(
        f"""
MailIntel AI v1.0.0

Evidence-Driven Email Investigation Platform

Generated: {generated}
"""
    )
