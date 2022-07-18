from flask import Blueprint, jsonify, request
from services.links import get_links

links_v1_blueprint = Blueprint('links_v1_api', __name__)

@links_v1_blueprint.route('/links', methods=['GET'])
def getLinks():
    response = get_links.getLinks()
    return jsonify({'links': response})