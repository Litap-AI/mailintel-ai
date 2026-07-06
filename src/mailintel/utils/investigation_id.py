"""
Investigation ID generator.
"""

from datetime import UTC, datetime
from uuid import uuid4


def generate_investigation_id() -> str:
    """Generate a unique investigation identifier."""

    timestamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")

    random_suffix = uuid4().hex[:4].upper()

    return f"INV-{timestamp}-{random_suffix}"
