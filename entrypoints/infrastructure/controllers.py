from flask import jsonify, request
from flask_cors import cross_origin

from modules.comments.application.create.comments_creator import CommentsCreator
from modules.comments.application.search.comments_searcher import CommentsSearcher
from modules.comments.domain.comments_repository import CommentsRepository
from modules.comments.domain.exceptions import DatabaseError, InvalidDataError


@cross_origin()
def get_comments(post_slug, comments_repository: CommentsRepository):
    try:
        searcher = CommentsSearcher(comments_repository)
        comments = searcher.search(post_slug)
        return jsonify([comment.serialize() for comment in comments]), 200

    except InvalidDataError as e:
        return jsonify({'text': str(e)}), 400

    except DatabaseError as e:
        return jsonify({'text': str(e)}), 500


@cross_origin()
def add_comment(post_slug, comments_repository: CommentsRepository):
    try:
        creator = CommentsCreator(comments_repository)
        creator.create(post_slug, **request.get_json())
        return jsonify({}), 200

    except InvalidDataError as e:
        return jsonify({'text': str(e)}), 400

    except DatabaseError as e:
        return jsonify({'text': str(e)}), 500
