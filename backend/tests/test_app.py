'''Tests for app.py'''
import json
from unittest.mock import patch
import pytest
import utilities
from backend.app import app


@pytest.fixture
def client():
    """create a db client for the tests

    Yields:
        client: db client
    """
    app.config['TESTING'] = True
    db_client = app.test_client()
    yield db_client


@patch('sqlalchemy.orm.session.sessionmaker')
@patch('openai.Completion.create')
def test_generate_adventure(mock_create, mock_save, client):
    '''Tests generate_adventure route'''
    # set up mock response
    mock_response = {
        "id":
        "cmpl-1q2w3e4r5t6y7u8i9o0p",
        "object":
        "text_completion",
        "created":
        1620000000,
        "model":
        "davinci003",
        "choices": [{
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
            "finish_reason": "length"
        }],
        "usage": {
            "prompt_tokens": 2000,
            "completion_tokens": 2000,
            "total_tokens": 4000
        }
    }

    mock_create.return_value = mock_response

    # set up test client

    # set up test data
    test_data = {
        "adventureTitle":
        "The Lost Temple",
        "adventureSetting":
        "Medieval Fantasy",
        "adventurePlot":
        "The players must find a way to stop an ancient evil from being unleashed."
    }

    # send request
    response = client.post('/generate_adventure',
                           data=json.dumps(test_data),
                           content_type='application/json')

    data = json.loads(response.get_data())

    # assert response
    assert response.status_code == 201
    assert data['message'] == utilities.clean_gpt_response(
        mock_response["choices"][0]["text"])


def test_get_adventures_from_db(client):
    """tests get_adventures_from_db route

    Args:
        client (_type_): _description_
    """

    response = client.get('/get_adventures_from_db')
    assert response.status_code == 200
    assert len(json.loads(response.data)) > 0
