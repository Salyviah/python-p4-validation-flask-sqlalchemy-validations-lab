import pytest
from models import Author, Post

def test_author_requires_name(session):
    with pytest.raises(ValueError, match="Author name must be at least 3 characters."):
        author = Author(name="AB")
        session.add(author)
        session.commit()

def test_author_unique_name(session):
    author1 = Author(name="John Doe")
    author2 = Author(name="John Doe")
    session.add(author1)
    session.commit()

    with pytest.raises(Exception):  # Check for IntegrityError on unique constraint
        session.add(author2)
        session.commit()

def test_post_content_too_short(session):
    with pytest.raises(ValueError, match="Post content must be at least 250 characters."):
        post = Post(
            title="Short Post",
            content="This is too short",
            summary="This is a summary",
            category="Fiction"
        )
        session.add(post)
        session.commit()

def test_post_summary_too_long(session):
    long_summary = "A" * 251
    with pytest.raises(ValueError, match="Post summary cannot exceed 250 characters."):
        post = Post(
            title="Long Summary",
            content="A" * 300,
            summary=long_summary,
            category="Fiction"
        )
        session.add(post)
        session.commit()

def test_post_invalid_category(session):
    with pytest.raises(ValueError, match="Category must be either 'Fiction' or 'Non-Fiction'."):
        post = Post(
            title="Invalid Category",
            content="A" * 300,
            summary="Valid summary",
            category="Sci-Fi"
        )
        session.add(post)
        session.commit()
