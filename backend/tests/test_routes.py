"""Tests for app.py"""
import json
from unittest.mock import patch
import pytest
import main.util.utilities as utilities
from main import app, db
from main.models import Adventures, AdventureNPCs, AdventureLocations


@pytest.fixture
def client():
    """create a db client for the tests

    Yields:
        client: db client
    """
    app.config["TESTING"] = True
    db_client = app.test_client()
    yield db_client


@patch("openai.Completion.create")
@patch("main.util.utilities.extract_entities_from_adventure")
def test_generate_adventure(mock_extract, mock_create, client):
    """Tests generate_adventure route"""
    # set up mock response
    mock_response = {
        "id": "cmpl-1q2w3e4r5t6y7u8i9o0p",
        "object": "text_completion",
        "created": 1620000000,
        "model": "davinci003",
        "choices": [
            {
                "text": """{
        "AdventureTitle": "The Lost Temple",
        "AdventureHook":
        "The players must find a way to stop an ancient evil from being unleashed.",
        "AdventurePlot":
        "The players are hired to infiltrate a rival guild and steal a powerful artifact",
        "AdventureClimax":
        "The players must defeat the guild leader in a final battle to stop the ancient evil from being unleashed.",
        "AdventureResolution":
        "The players succeed in defeating the guild leader and stopping the ancient evil.",
        "AdventureNPCs": "Guild leader, ancient evil"}""",
                "index": 0,
                "logprobs": None,
                "finish_reason": "length",
            }
        ],
        "usage": {
            "prompt_tokens": 2000,
            "completion_tokens": 2000,
            "total_tokens": 4000,
        },
    }

    mock_create.return_value = mock_response

    # set up test client

    # set up test data
    test_data = {
        "adventureTitle": "The Lost Temple",
        "adventureSetting": "Medieval Fantasy",
        "adventurePlot": "The players must find a way to stop an ancient evil from being unleashed.",
    }

    # send request
    response = client.post(
        "/generate_adventure",
        data=json.dumps(test_data),
        content_type="application/json",
    )

    data = json.loads(response.get_data())

    expected_keys = [
        "AdventureTitle",
        "AdventureHook",
        "AdventurePlot",
        "AdventureClimax",
        "AdventureResolution",
        "AdventureNPCs",
    ]

    # assert response
    assert response.status_code == 201
    assert data["message"] == utilities.clean_gpt_response(
        mock_response["choices"][0]["text"], expected_keys=expected_keys
    )


def test_get_adventures_from_db(client):
    """tests get_adventures_from_db route

    Args:
        client (_type_): _description_
    """

    response = client.get("/get_adventures_from_db")
    assert response.status_code == 200
    assert len(json.loads(response.data)) > 0


def test_get_specific_adventures_from_db(client):
    """tests get_adventures_from_db route

    Args:
        client (_type_): _description_
    """

    response = client.get("/get_adventures_from_db?id=1")
    assert response.status_code == 200
    assert len(json.loads(response.data)) > 0


# Create a fixture to set up and tear down the test database and some sample data
@pytest.fixture
def test_db():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    db.create_all()
    adventure1 = Adventures(
        title="The Lost Temple", description="A mysterious temple hidden in the jungle."
    )
    adventure2 = Adventures(
        title="The Dragon's Lair",
        description="A dangerous quest to slay a fearsome dragon.",
    )
    db.session.add_all([adventure1, adventure2])
    db.session.commit()
    yield db
    db.drop_all()


# Test the extract_entities function with a valid id
def test_extract_entities_valid_id(test_db):
    # Create a test client
    client = app.test_client()
    # Send a POST request to the /extract_entities/1 endpoint
    response = client.post("/extract_entities/1")
    # Check the status code is 201
    assert response.status_code == 201
    # Check the response data is a JSON object
    assert response.is_json
    # Load the response data as a Python dictionary
    data = json.loads(response.data)
    # Check the status is "success"
    assert data["status"] == "success"
    # Check the message is a list of two lists
    assert isinstance(data["message"], list)
    assert len(data["message"]) == 2
    # Check the first list contains the expected NPC names
    assert data["message"][0] == ["temple", "jungle"]
    # Check the second list contains the expected location names
    assert data["message"][1] == ["temple", "jungle"]
    # Check the database has the expected NPC and location records
    npc1 = AdventureNPCs.query.filter_by(adventure_id=1, npc_name="temple").first()
    npc2 = AdventureNPCs.query.filter_by(adventure_id=1, npc_name="jungle").first()
    location1 = AdventureLocations.query.filter_by(
        adventure_id=1, location_name="temple"
    ).first()
    location2 = AdventureLocations.query.filter_by(
        adventure_id=1, location_name="jungle"
    ).first()
    assert npc1 is not None
    assert npc2 is not None
    assert location1 is not None
    assert location2 is not None


# Test the extract_entities function with an invalid id
def test_extract_entities_invalid_id(test_db):
    # Create a test client
    client = app.test_client()
    # Send a POST request to the /extract_entities/3 endpoint
    response = client.post("/extract_entities/3")
    # Check the status code is 404
    assert response.status_code == 404
    # Check the response data is a JSON object
    assert response.is_json
    # Load the response data as a Python dictionary
    data = json.loads(response.data)
    # Check the status is "error"
    assert data["status"] == "error"
    # Check the message is "Adventure not found"
    assert data["message"] == "Adventure not found"
    # Check the database has no NPC or location records for adventure id 3
    npcs = AdventureNPCs.query.filter_by(adventure_id=3).all()
    locations = AdventureLocations.query.filter_by(adventure_id=3).all()
    assert len(npcs) == 0
    assert len(locations) == 0
