from dataclasses import dataclass


@dataclass
class CreateCommentCommand:
    post_slug: str
    name: str
    email: str
    text: str
