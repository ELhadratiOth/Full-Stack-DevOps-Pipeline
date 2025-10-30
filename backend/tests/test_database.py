"""Test database utilities"""
from app.database import init_db, get_session


def test_init_db():
    """Test database initialization"""
    # This should not raise any exceptions
    init_db()


def test_get_session():
    """Test get_session generator"""
    session_gen = get_session()
    session = next(session_gen)
    assert session is not None
    # Clean up
    try:
        next(session_gen)
    except StopIteration:
        pass  # Expected behavior
