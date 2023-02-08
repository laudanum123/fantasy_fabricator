from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
# app.config.from_object(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../fantasy_fabricator.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fantasy_fabricator.db'
db = SQLAlchemy(app)
# configure the SQLite database, relative to the app instance folder

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension

CORS(app, resources={r"/*": {"origins": "*"}})

from main.routes.routes import routes

app.register_blueprint(routes)