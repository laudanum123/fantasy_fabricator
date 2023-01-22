'''Tests for app.py'''
import json
from unittest.mock import patch
from app import app


@patch('openai.Completion.create')
def test_generate_adventure(mock_create):
    '''Tests generate_adventure route'''
    # set up mock response
    mock_response = {
        "AdventureTitle": "The Lost Temple",
        "AdventureHook":
        "The players must find a way to stop an ancient evil from being unleashed.",
        "AdventurePlot":
        "The players are hired to infiltrate a rival guild and steal a powerful artifact",
        "AdventureClimax":
        "The players must defeat the guild leader in a final battle to stop the ancient evil from being unleashed.",
        "AdventureResolution":
        "The players succeed in defeating the guild leader and stopping the ancient evil.",
        "AdventureNPCs": "Guild leader, ancient evil"
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
    assert data['message'] == mock_response
