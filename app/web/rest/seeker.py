from flask import Blueprint, request
from services.seeker import get_page_links

seeker_v1_blueprint = Blueprint('seeker_v1_api', __name__)

@seeker_v1_blueprint.route('/seeker', methods=['POST'])
def seeker():
    data = request.get_json()
    linkList = []
    return get_page_links.getPageLinks(data['url'], linkList)
