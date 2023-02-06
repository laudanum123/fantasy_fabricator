"""
    This is the main entry point of the application.
"""

from main import app


@app.route("/generate_npc", methods=["POST"])
def generate_npc():
    """Create a new NPC for an Adventure using GPT-3 and return the result"""
    print(len(request.json))
    print(request.json)
    if request.json["adventureId"] == "":
        return "Please provide adventure id", 400

    npc = {}
    npc["name"] = request.json["characterName"]
    npc["game_system"] = request.json["selectedSystem"]
    npc["adventure_id"] = request.json["adventureId"]

    if npc["game_system"] == "Define other":
        npc["game_system"] = request.json["custom_system"]

    session = sessionmaker(bind=engine)

    adventure = Adventures.get_adventures(npc["adventure_id"])[0]
    print(adventure)
    prompt = f'You are a professional writer of RPG Adventures who is tasked with\
    creating an background and game stats for Non Player Characters. \
    The NPC is called {npc["name"]} and is supposed to be\
    set in a {npc["game_system"]} setting. The background of the NPC should be compatible with\
    the following adventure: {adventure["AdventureHook"]} . {adventure["AdventurePlot"]}.\
    {adventure["AdventureClimax"]}.{adventure["AdventureResolution"]}.\
    Please use the above structure and use a minimum of 1000 words for your answer.\
    Format the answer as a json object with the following stucture. The NPCStats should use the common Statblock format of the respective game system:\
    {{  "NPCBackground": content,\
        "NPCStats": content,\
        }}'
    gpt_response = openai.Completion.create(
        engine="text-davinci-003", prompt=prompt, max_tokens=3000
    )

    print(gpt_response)
    npc = AdventureNPCs(npc, gpt_response)
    if not app.config["TESTING"]:
        with session() as session:
            session.add(npc)
            session.commit()

    response = jsonify({"status": "success", "message": npc.to_dict()})
    response.status_code = 201
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
