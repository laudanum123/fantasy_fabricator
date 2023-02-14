import pytest
from main import app, db, routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main.models import Adventures, AdventureLocations, AdventureNPCs, Entities


@pytest.fixture()
def app():
    """Create and configure a new app instance for each test."""
    app = Flask(__name__)
    app.config.update(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"}
    )
    app.register_blueprint(routes)

    db.init_app(app)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture()
def client(app):
    """Provide the transactional fixtures with access to the database"""
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
