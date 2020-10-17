from dataclasses import dataclass


@dataclass
class SearchCommentsQuery:
    post_slug: str
