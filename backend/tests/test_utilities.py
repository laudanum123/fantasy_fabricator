import json
from unittest.mock import patch
import re
import pytest
from main.util.utilities import (extract_entities_from_adventure,
                       query_gpt_api, verify_gpt_response_keys)


@patch('openai.Completion.create')
def test_query_gpt_api(mock_create):
    prompt = "What is the meaning of life?"
    mock_create.return_value = {"choices": [{"text": '42'}]}
    response = query_gpt_api(prompt)
    mock_create.assert_called_with(engine="text-davinci-003",
                                   prompt=prompt,
                                   max_tokens=2000)
    assert response == {"choices": [{"text": '42'}]}


def test_extract_named_entities():
    text = "Barack Obama was born in Hawaii."
    entities = extract_named_entities(text)
    assert entities == ["Barack Obama", "Hawaii"]


def test_verify_gpt_response_keys():
    response_string = '''{"AdventureTitle": "Fate of Agurna",  "AdventureHook":
"The forest of Agurna, a peaceful, secluded place, has recently been under 
attack by mysterious, unseen forces. A powerful witch named Celeste gathers
the bravest adventurers she can find and gives them one simple task: find 
out who or what is behind the Agurna attacks and save the forest.",  
"AdventurePlot": "The adventurers start their journey in a nearby village, 
where they can receive clues to lead them in the right direction. After 
talking to some of the villagers, they find out about Celeste's tower, 
a hidden magical hideout. They travel to the tower and confront Celeste. 
She tells them about the mysterious forces attacking Agurna, and the adventurers agree 
to help. The adventurers travel to Agurna, and soon come across a group of strange creatures. 
After a long battle, the adventurers come to the conclusion that these creatures are being 
controlled by a powerful being. After gathering more clues, the adventurers discover that 
the powerful being is a sorcerer named Malius.The adventurers track Malius to his hidden 
lair, deep within the forest of Agurna. With the help of Celeste, they make their way to 
the entrance of the lair. Inside, they confront Malius and his minions and after a fierce 
battle, they defeat him.",  "AdventureClimax": "The adventurers triumph over Malius and 
his minions, and the forest of Agurna is saved. After freeing the creatures from his 
control, Celeste uses her powerful magic to seal  the entrance to the lair, thus 
ensuring that no one else can use it to cause more harm to the forest.",  
"AdventureResolution": "The adventurers return to Celeste's tower, where they are 
rewarded with riches and glory. They also learn that Celeste is the guardian of the 
forest and has been using her magic to protect it for many years. The adventurers 
have now become heroes and are widely celebrated for their heroic deeds.",  
"AdventureNPCs: "Celeste, Malius, villagers of the nearby village, strange creatures 
controlled by Malius."}'''

    response_string = re.sub(r'[^\x20-\x7E]+', '', response_string)

    expected_output = '''{"AdventureTitle":  "Fate of Agurna",  "AdventureHook":"The forest\
 of Agurna, a peaceful, secluded place, has recently been under attack by mysterious, unseen\
 forces. A powerful witch named Celeste gathersthe bravest adventurers she can find and gives\
 them one simple task: find out who or what is behind the Agurna attacks and save the forest.",\
  "AdventurePlot": "The adventurers start their journey in a nearby village, where they can\
 receive clues to lead them in the right direction. After talking to some of the villagers,\
 they find out about Celeste\'s tower, a hidden magical hideout. They travel to the tower\
 and confront Celeste. She tells them about the mysterious forces attacking Agurna, and \
the adventurers agree to help. The adventurers travel to Agurna, and soon come across a \
group of strange creatures. After a long battle, the adventurers come to the conclusion \
that these creatures are being controlled by a powerful being. After gathering more \
clues, the adventurers discover that the powerful being is a sorcerer named Malius.\
The adventurers track Malius to his hidden lair, deep within the forest of Agurna. \
With the help of Celeste, they make their way to the entrance of the lair. Inside, \
they confront Malius and his minions and after a fierce battle, they defeat him.", \
 "AdventureClimax": "The adventurers triumph over Malius and his minions, and the \
forest of Agurna is saved. After freeing the creatures from his control, Celeste \
uses her powerful magic to seal  the entrance to the lair, thus ensuring that no \
one else can use it to cause more harm to the forest.",  "AdventureResolution": \
"The adventurers return to Celeste\'s tower, where they are rewarded with riches \
and glory. They also learn that Celeste is the guardian of the forest and has \
been using her magic to protect it for many years. The adventurers have now \
become heroes and are widely celebrated for their heroic deeds.","AdventureNPCs":\
  "Celeste, Malius, villagers of the nearby village, strange creatures controlled \
by Malius."}'''

    output = verify_gpt_response_keys(response_string)
    assert output == expected_output