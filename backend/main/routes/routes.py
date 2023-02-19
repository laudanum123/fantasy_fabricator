import openai
from main.util.api_key import API_KEY
from flask import Blueprint,request,jsonify
from main import db
from main.models import Adventures,Entities,AdventureNPCs,AdventureLocations
from main.util import utilities

routes = Blueprint('routes',__name__)

openai.api_key = API_KEY
@routes.route('/generate_adventure', methods=['POST']) ## occasional error: raise JSONDecodeError("Expecting value", s, err.value) from None json.decoder.JSONDecodeError: Expecting value: line 1 column 21 (char 20)
def generate_adventure():
    '''
    create adventure based on user input using GPT-3 and return the result
    '''

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
        "AdventureNPCs": content}}'\

    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt=prompt,
                                        max_tokens=2000)

    gpt_json = utilities.clean_gpt_response(response['choices'][0]['text'])

    # create adventure object for new adventure
    adventure = Adventures(adventure_title = gpt_json['AdventureTitle'],
                           adventure_hook = gpt_json['AdventureHook'],
                           adventure_plot = gpt_json['AdventurePlot'],
                           adventure_climax = gpt_json['AdventureClimax'],
                           adventure_resolution = gpt_json['AdventureResolution'],
                           adventure_npcs = gpt_json['AdventureNPCs'])

    db.session.add(adventure)
    db.session.commit()

    # extract named entities from adventure
    combined_texts = [
        gpt_json['AdventureHook'], gpt_json['AdventurePlot'],
        gpt_json['AdventureClimax'], gpt_json['AdventureResolution'],
        gpt_json['AdventureNPCs']
    ]
    corpus = ' '.join(combined_texts)
    entities = utilities.extract_named_entities(corpus)
    print(entities)
    for entity in entities:
        entity = Entities(entity_name = entity,adventure_id = adventure.id)
        db.session.add(entity)
        db.session.commit()

    # return json response
    response = jsonify({"status": "success", "message": gpt_json})
    response.status_code = 201
    return response




@routes.route('/get_adventures_from_db', methods=['GET'])
def get_adventures_from_db():
    '''
    get all or single adventure(s) from database
    '''

    if request.args.get('id'):
        adventure_id = request.args.get('id')
        adventures = Adventures.get_adventures(adventure_id)
    else:
        adventures = Adventures.get_adventures()

    response = jsonify(adventures)

    # reduce to required fields
    response.status_code = 200
    return response


@routes.route('/delete_adventures_from_db', methods=['DELETE'])
def delete_adventures_from_db():
    '''
    delete adventure(s) from database
    '''

    print(request.json)
    if request.json:
        adventure_ids = request.json['ids']
        Adventures.delete_adventures(adventure_ids)

    response = jsonify({"status": "success", "message": "adventure deleted"})
    response.status_code = 204
    return response


@routes.route('/extract_entities/<id>', methods=['POST'])
def extract_entities(id):

    adventure_dict = Adventures.get_adventures(id)[0]
    adventure = Adventures.query.filter_by(id=id).first()

    npc_list,locations_list = utilities.extract_entities_from_adventure(adventure_dict)

    for npc in npc_list:
        npc_obj = AdventureNPCs.query.filter_by(adventure_id=id, npc_name=npc).first()
        if not npc_obj:
            npc_obj = AdventureNPCs(adventure_id=id, npc_name=npc)
            db.session.add(npc_obj)

    for location in locations_list:
        location_obj = AdventureLocations.query.filter_by(adventure_id=id, location_name=location).first()
        if not location_obj:
            location_obj = AdventureLocations(adventure_id=id, location_name=location)
            db.session.add(location_obj)

    if adventure:
        adventure.entities_extracted = True

    db.session.commit()

    response = jsonify({"status": "success", "message": [npc_list,locations_list]})
    response.status_code = 201

    return response

@routes.route('/get_NPCs_from_db', methods=['GET'])
def get_NPCs_from_db():
    '''
    get NPCs from database
    '''

    adventure_id = request.args.get('id')
    npc = AdventureNPCs.get_NPCs(adventure_id)

    response = jsonify(npc)

    # reduce to required fields
    response.status_code = 200
    return response

@routes.route('/get_locations_from_db', methods=['GET'])
def get_locations_from_db():
    '''
    get locations from database
    '''


    adventure_id = request.args.get('id')

    npc = AdventureLocations.get_locations(adventure_id)

    response = jsonify(npc)

    # reduce to required fields
    response.status_code = 200
    return response
