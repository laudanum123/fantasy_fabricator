from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

# routes.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/adventure', methods=['POST'])
def create_adventure():
    # code to create an adventure
    pass

@app.route('/character', methods=['POST'])
def create_character():
    pass
    # code to create a character

# etc.

if __name__ == '__main__':
    app.run()
