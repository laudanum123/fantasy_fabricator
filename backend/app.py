"""
    This is the main entry point of the application.
"""

from main import app


@app.route("/generate_npc", methods=["POST"])
def generate_npc():
    """Create a new NPC for an Adventure using GPT-3 and return the result"""
    print(request.json)
    if request.json:



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
