"""Initialize the Flask app and configure it to use the database."""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "5791628bb0b13ce0c676dfde280ba245"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../fantasy_fabricator.db"
db = SQLAlchemy(app)


CORS(app, resources={r"/*": {"origins": "*"}})
from main.routes.routes import routes

app.register_blueprint(routes)
