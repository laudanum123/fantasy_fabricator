'''Tests for app.py'''
import json
from unittest.mock import patch
from app import app
import utilities
import models


@patch('models.Adventures')
@patch('openai.Completion.create')
def test_generate_adventure(mock_create, mock_adventures):
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
        "davinci:2020-05-03",
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
    client = app.test_client()

    # set up test data
    test_data = {
        "adventureTitle": "The Lost Temple",
        "adventureSetting": "Medieval Fantasy"
    }

    # send request
    response = client.post('/generate_adventure',
                           data=json.dumps(test_data),
                           content_type='application/json')
    data = json.loads(response.get_data())

    # assert response
    assert response.status_code == 201
    assert data['message'] == utilities.convert_response_to_json(mock_response)
