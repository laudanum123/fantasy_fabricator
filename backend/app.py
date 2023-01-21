"""
    This is the main entry point of the application.
"""
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/generate_character", methods=["GET"])
def generate_character():
    '''
    create adventure based on user input using GPT-3
    '''
    return jsonify("test!")


@app.route('/generate_adventure', methods=['POST'])
def generate_adventure():
    '''
    create adventure based on user input using GPT-3
    '''
    message_body = request.json
    return jsonify({"status": "success", "message": message_body}, 201)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
