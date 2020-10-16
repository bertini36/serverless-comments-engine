from dataclasses import dataclass


@dataclass
class CreateCommand:
    post_slug: str
    name: str
    email: str
    text: str
