import json
import re
import openai
import pytest
from main.models import Adventures, AdventureNPCs, AdventureLocations
from main.util.utilities import (
    query_gpt_api,
    clean_gpt_response,
    verify_gpt_response_keys,
    extract_entities_from_adventure,
)
from unittest.mock import patch
import pytest


@patch("openai.Completion.create")
def test_query_gpt_api(mock_create):
    prompt = "What is the meaning of life?"
    mock_create.return_value = {"choices": [{"text": "42"}]}
    response = query_gpt_api(prompt)
    mock_create.assert_called_with(
        engine="text-davinci-003", prompt=prompt, max_tokens=2000
    )
    assert response == {"choices": [{"text": "42"}]}


@pytest.fixture()
def adventure_data():
    return {
        "id": 1,
        "title": "The Great Adventure",
        "story": "You are a brave adventurer on a quest to save the world from the evil dragon.",
        "author": "John Doe",
    }


def test_clean_gpt_response(adventure_data):
    expected_keys = ["key1", "key2", "key3"]
    response_string = f'{{ "key1": "{adventure_data["title"]}", "key2": "{adventure_data["story"]}", "key3": "{adventure_data["author"]}" }}'

    cleaned_response = clean_gpt_response(response_string, expected_keys)
    assert type(cleaned_response) == dict
    assert cleaned_response["key1"] == adventure_data["title"]
    assert cleaned_response["key2"] == adventure_data["story"]
    assert cleaned_response["key3"] == adventure_data["author"]


def test_verify_gpt_response_keys(adventure_data):
    expected_keys = ["title", "story", "author"]
    response_string = f'{{ "key1": "{adventure_data["title"]}", "key2": "{adventure_data["story"]}", "key3": "{adventure_data["author"]}" }}'
    cleaned_response = verify_gpt_response_keys(response_string, expected_keys)

    assert type(cleaned_response) == str
    assert "title" in cleaned_response
    assert "story" in cleaned_response
    assert "author" in cleaned_response


def test_extract_entities_from_adventure(monkeypatch, adventure_data, client):
    def mock_create(*args, **kwargs):
        return {
            "choices": [
                {
                    "text": '{"NPCs": ["wizard", "warrior", "dragon"], "Locations": ["castle", "cave", "forest"]}'
                }
            ]
        }

    monkeypatch.setattr("openai.Completion.create", mock_create)

    npc_list, locations_list = extract_entities_from_adventure(adventure_data)

    assert type(npc_list) == list
    assert type(locations_list) == list

    for npc in ["wizard", "warrior", "dragon"]:
        assert npc in npc_list

    for location in ["castle", "cave", "forest"]:
        assert location in locations_list
