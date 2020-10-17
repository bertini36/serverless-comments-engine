from src.modules.comments.application.search.comments_searcher import (
    CommentsSearcher,
)
from src.modules.comments.application.search.search_comments_query import (
    SearchCommentsQuery,
)
from src.modules.comments.infrastructure.repository.inmemory_comments_repository import (  # noqa
    InMemoryCommentsRepository,
)
from ..conftest import IN_MEMORY_COMMENTS_PATH

repository = InMemoryCommentsRepository(IN_MEMORY_COMMENTS_PATH)


def test_search_comments():
    query = SearchCommentsQuery(post_slug='dummy')
    CommentsSearcher(repository).search(query)
