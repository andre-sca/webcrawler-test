from flask import Flask
from flask_cors import CORS
import os

apiApp = Flask(__name__)

from web.rest.seeker import seeker_v1_blueprint
from web.rest.links import links_v1_blueprint

apiApp.register_blueprint(seeker_v1_blueprint, url_prefix="/api/v1")
apiApp.register_blueprint(links_v1_blueprint, url_prefix="/api/v1")

CORS(apiApp)

apiApp.run(host='0.0.0.0')
