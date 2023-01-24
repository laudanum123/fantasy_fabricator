"""
    This is the main entry point of the application.
"""
import models
import openai
import utilities
from api_key import API_KEY
from flask import Flask, jsonify, request
from flask_cors import CORS

openai.api_key = API_KEY

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/generate_adventure', methods=['POST'])
def generate_adventure():
    '''
    create adventure based on user input using GPT-3 and return the result
    '''
    message_body = request.json

    prompt = f'You are a professional writer of RPG Adventures who is tasked with\
    creating an adventure with the title {message_body["adventureTitle"]}. The adventure is supposed to be\
    set in a {message_body["adventureSetting"]} setting. Please write a detailed adventure that includes a breakdown of\
    the following:\
    1. The adventure hook\
    2. The adventure plot\
    3. The adventure climax\
    4. The adventure resolution\
    5. Important NPCs and monsters\
    Please use the above structure and use a minimum of 300 words for your answer.\
    Format the answer as a json object with the following stucture:\
    {{  "AdventureTitle": content,\
        "AdventureHook": content,\
        "AdventurePlot": content,\
        "AdventureClimax": content,\
        "AdventureResolution": content,\
        "AdventureNPCs: content}}'\

    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt=prompt,
                                        max_tokens=2000)

    gpt_json = utilities.convert_response_to_json(response)
    models.Adventures(gpt_json['AdventureTitle'], gpt_json['AdventureHook'],
                      gpt_json['AdventurePlot'], gpt_json['AdventureClimax'],
                      gpt_json['AdventureResolution'],
                      gpt_json['AdventureNPCs'])
    response = jsonify({"status": "success", "message": gpt_json})
    response.status_code = 201
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
