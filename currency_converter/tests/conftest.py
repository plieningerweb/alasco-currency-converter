import logging

import pytest

from currency_converter.app import create_app

@pytest.fixture
def app():
    """Create application for the tests."""
    _app = create_app()
    _app.logger.setLevel(logging.CRITICAL)
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()

@pytest.fixture
def client(app):
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'not-so-secret'
    client = app.test_client()

    yield client

@pytest.fixture
def client_csrf_disabled(app):
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    client = app.test_client()

    yield client
