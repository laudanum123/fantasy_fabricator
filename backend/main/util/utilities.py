'''Different utilities for the backend'''
import json
import re
import openai



def query_gpt_api(prompt):
    '''
    query gpt api
    '''
    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt=prompt,
                                        max_tokens=2000)
    return response



def clean_gpt_response(gpt_response: str) -> dict:
    '''
    clean gpt response
    '''
    # Remove leading/trailing whitespaces
    gpt_response = gpt_response.strip()

    gpt_response = re.sub(r'[^\x20-\x7E]+', '', gpt_response)
    # Remove extra quotation marks
    #gpt_response = re.sub('"', '', gpt_response)

    gpt_response = verify_gpt_response_keys(gpt_response)
    # Parse response into a Python dictionary
    response_dict = json.loads(gpt_response)

    # Verify keys and make necessary adjustments
    if 'AdventureTitle' not in response_dict:
        response_dict['AdventureTitle'] = ''
    if 'AdventureHook' not in response_dict:
        response_dict['AdventureHook'] = ''
    if 'AdventurePlot' not in response_dict:
        response_dict['AdventurePlot'] = ''
    if 'AdventureClimax' not in response_dict:
        response_dict['AdventureClimax'] = ''
    if 'AdventureResolution' not in response_dict:
        response_dict['AdventureResolution'] = ''
    if 'AdventureNPCs' not in response_dict:
        response_dict['AdventureNPCs'] = ''

    # Turn the JSON string into a JSON response
    return response_dict


def verify_gpt_response_keys(response_string: str) -> str:
    """verify that the keys in the response string are correct

    Args:
        response_string (str): pre_cleaned response string

    Returns:
        str: cleaned response string
    """
    correct_keys = [
        '"AdventureTitle"', '"AdventureHook"', '"AdventurePlot"',
        '"AdventureClimax"', '"AdventureResolution"', '"AdventureNPCs"'
    ]

    # Split after each key-value pair and then split key and value
    # Replace incorrect key with correct one if necessary
    key_value_pairs = response_string.split('",')
    for i, pair in enumerate(key_value_pairs):
        key = pair[:pair.index(":")]
        value = pair[pair.index(":") + 1:]
        if key.strip() != correct_keys[i]:
            key_value_pairs[i] = f"{correct_keys[i]}: {value}"

    # Rejoin key-value pairs and add curly braces if necessary
    new_response = '",'.join(key_value_pairs)
    if new_response[0] != "{":
        new_response = "{" + new_response
    if new_response[-1] != "}":
        new_response = new_response + "}"

    return new_response


def extract_entities_from_adventure(adventure):

    adventure.pop("id", None)

    # join all the values of the dictionary into one string
    corpus = ''.join([v for k, v in adventure.items() if type(v) == str])
    prompt = f'Given the following RPG story: {corpus}.\
    Extract all entities. \
    Entities refer to all NPCs (non-player character) and locations.\
    NPCs include but not limited to: Any character mentioned in the story such as NPCs, side characters,players,characters and living beings\
    Locations include but not limited to: Any location mentioned in the RPG story such as Forest,Desert,River,Oceans,Temple. \
    The extracted content should exactly string match what is present in the RPG story. \
    Format the answer as a json object with the following structure with a value of type "list":\
    {{  "NPCs": [NPC content],\
        "Locations": [Locations content] }}'

    response = openai.Completion.create(engine="text-davinci-003",
                             prompt= prompt,
                             max_tokens=2000)

    text = response['choices'][0]['text']

    npc_loc_json =  json.loads(text)

    npc = npc_loc_json.get("NPCs")
    locations = npc_loc_json.get("Locations")


    return npc,locations




