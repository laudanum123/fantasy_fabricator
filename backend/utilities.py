'''Different utilities for the backend'''
import json
import re
import openai


def convert_response_to_json(response):
    '''
    convert response to json
    '''
    gpt_text = response['choices'][0]['text']
    gpt_text_clean = re.sub(r'[^\x20-\x7E]+', '', gpt_text)
    gpt_json = json.loads(gpt_text_clean)
    return gpt_json


def query_gpt_api(prompt):
    '''
    query gpt api
    '''
    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt=prompt,
                                        max_tokens=2000)
    return response