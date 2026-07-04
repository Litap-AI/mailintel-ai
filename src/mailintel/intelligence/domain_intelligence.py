"""
Domain Intelligence.

Extracts sender and URL domains from an investigation.
"""

from urllib.parse import urlparse

from mailintel.domain.investigation import Investigation


class DomainIntelligence:
    """Extract useful domains from an investigation."""

    def extract(
        self,
        investigation: Investigation,
    ) -> dict[str, list[str]]:

        sender_domains: set[str] = set()
        url_domains: set[str] = set()

        for evidence in investigation.evidence:
            if evidence.title == "URL Found":
                parsed = urlparse(evidence.observed_value)

                if parsed.netloc:
                    url_domains.add(parsed.netloc.lower())

        return {
            "sender_domains": sorted(sender_domains),
            "url_domains": sorted(url_domains),
        }
