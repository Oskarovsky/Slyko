from flask import Flask
from config import Config
from app import routes


slyko_app = Flask(__name__)
slyko_app.config.from_object(Config)

