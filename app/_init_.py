from flask import Flask
from flasgger import Swagger
import yaml
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

app.run(host='0.0.0.0')