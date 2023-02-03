"""
    This is the main entry point of the application.
"""
from models import Adventures, Entities
import models
import openai
import utilities
from api_key import API_KEY
from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker

openai.api_key = API_KEY

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
engine = models.engine


@app.route("/generate_adventure", methods=["POST"])
def generate_adventure():
    """
    create adventure based on user input using GPT-3 and return the result
    """
    message_body = request.json

    prompt = f'You are a professional writer of RPG Adventures who is tasked with\
    creating an adventure with the title {message_body["adventureTitle"]}. The adventure is supposed to be\
    set in a {message_body["adventureSetting"]} setting. The general plot of the adventure should be based\
    on the following: {message_body["adventurePlot"]}.\
    Please write a detailed adventure that includes a breakdown of\
    the following:\
    1. The adventure hook\
    2. The adventure plot\
    3. The adventure climax\
    4. The adventure resolution\
    5. Important NPCs and monsters\
    Please use the above structure and use a minimum of 1000 words for your answer.\
    Format the answer as a json object with the following stucture:\
    {{  "AdventureTitle": content,\
        "AdventureHook": content,\
        "AdventurePlot": content,\
        "AdventureClimax": content,\
        "AdventureResolution": content,\
        "AdventureNPCs": content}}'
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=2000
    )

    gpt_json = utilities.clean_gpt_response(response["choices"][0]["text"])

    # create adventure object for new adventure
    session = sessionmaker(bind=engine)
    with session() as session:
        adventure = Adventures(
            gpt_json["AdventureTitle"],
            gpt_json["AdventureHook"],
            gpt_json["AdventurePlot"],
            gpt_json["AdventureClimax"],
            gpt_json["AdventureResolution"],
            gpt_json["AdventureNPCs"],
        )
        if not app.config["TESTING"]:
            session.add(adventure)
            session.commit()

        # extract named entities from adventure
        combined_texts = [
            gpt_json["AdventureHook"],
            gpt_json["AdventurePlot"],
            gpt_json["AdventureClimax"],
            gpt_json["AdventureResolution"],
            gpt_json["AdventureNPCs"],
        ]
        corpus = " ".join(combined_texts)
        entities = utilities.extract_named_entities(corpus)
        print(entities)
        for entity in entities:
            entity = Entities(entity, adventure.id)
            if not app.config["TESTING"]:
                session.add(entity)
                session.commit()

    # return json response
    response = jsonify({"status": "success", "message": gpt_json})
    response.status_code = 201
    return response


@app.route("/get_adventures_from_db", methods=["GET"])
def get_adventures_from_db():
    """
    get all or single adventure(s) from database
    """
    if request.args.get("id"):
        adventure_id = request.args.get("id")
        adventures = Adventures.get_adventures(adventure_id)
    else:
        adventures = Adventures.get_adventures()

    response = jsonify(adventures)

    # reduce to required fields
    response.status_code = 200
    return response


@app.route("/get_entities_from_db", methods=["GET"])
def get_entities_from_db():
    """
    get all or single entity(ies) from database
    """
    if request.args.get("id"):
        adventure_id = request.args.get("id")
        entities = Entities.get_entities(adventure_id=adventure_id)
    else:
        entities = Entities.get_entities()

    response = jsonify(entities)

    # reduce to required fields
    response.status_code = 200
    return response


@app.route("/delete_adventures_from_db", methods=["DELETE"])
def delete_adventures_from_db():
    """
    delete adventure(s) from database
    """
    print(request.json)
    if request.json:
        adventure_ids = request.json["ids"]
        Adventures.delete_adventures(adventure_ids)

    response = jsonify({"status": "success", "message": "adventure deleted"})
    response.status_code = 204
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
