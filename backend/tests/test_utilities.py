from main.util.utilities import (
    clean_gpt_response,
    verify_gpt_response_keys,
    extract_entities_from_adventure,
)
import pytest


@pytest.fixture()
def adventure_data():
    return {
        "id": 1,
        "title": "The Great Adventure",
        "story": "You are a brave adventurer on a quest to save the world from the evil dragon.",
        "author": "John Doe",
    }


def test_clean_gpt_response(adventure_data):
    # GIVEN: expected keys and a response string with values for the expected keys
    expected_keys = ["key1", "key2", "key3"]
    response_string = f'{{ "key1": "{adventure_data["title"]}", "key2": "{adventure_data["story"]}", "key3": "{adventure_data["author"]}" }}'

    # WHEN: the response string is cleaned
    cleaned_response = clean_gpt_response(response_string, expected_keys)

    # THEN: the cleaned response is a dictionary with the expected keys and values
    assert type(cleaned_response) == dict
    assert cleaned_response["key1"] == adventure_data["title"]
    assert cleaned_response["key2"] == adventure_data["story"]
    assert cleaned_response["key3"] == adventure_data["author"]



def test_verify_gpt_response_keys(adventure_data):

    # Given the expected response keys
    expected_keys = ["title", "story", "author"]

    # Given the adventure data
    adventure_data = {
        "title": "The Adventure",
        "story": "Once upon a time...",
        "author": "John Doe"
    }

    # When the GPT response keys are verified
    response_string = f'{{ "key1": "{adventure_data["title"]}", "key2": "{adventure_data["story"]}", "key3": "{adventure_data["author"]}" }}'
    cleaned_response = verify_gpt_response_keys(response_string, expected_keys)

    # Then the cleaned response should have the expected keys
    assert type(cleaned_response) == str
    assert "title" in cleaned_response
    assert "story" in cleaned_response
    assert "author" in cleaned_response


def test_extract_entities_from_adventure(monkeypatch, adventure_data, client):
    # Given the monkeypatch fixture, the adventure_data fixture, and the client fixture

    # Given a mock function that returns a JSON string containing NPCs and locations
    def mock_create(*args, **kwargs):
        return {
            "choices": [
                {
                    "text": '{"NPCs": ["wizard", "warrior", "dragon"], "Locations": ["castle", "cave", "forest"]}'
                }
            ]
        }

    # Given the monkeypatch fixture is used to replace the `openai.Completion.create()` function with the mock function
    monkeypatch.setattr("openai.Completion.create", mock_create)

    # When extract_entities_from_adventure() is called with the adventure_data and client arguments
    npc_list, locations_list = extract_entities_from_adventure(adventure_data)

    # Then npc_list and locations_list should be lists
    assert type(npc_list) == list
    assert type(locations_list) == list

    # Then npc_list should contain "wizard", "warrior", and "dragon"
    for npc in ["wizard", "warrior", "dragon"]:
        assert npc in npc_list

    # Then locations_list should contain "castle", "cave", and "forest"
    for location in ["castle", "cave", "forest"]:
        assert location in locations_list

