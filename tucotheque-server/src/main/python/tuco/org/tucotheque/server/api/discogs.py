'''
Created on 23 nov. 2018

@author: tuco
'''
from flask_restful import Resource, Api
from flask.blueprints import Blueprint
import discogs_client
from tuco.org.tucotheque.server.config import config
from flask import jsonify

client = discogs_client.Client('tuco.org.tucotheque.server/1.0', user_token=config.get('libraries.discogs.token'))

class DiscogsRelease(Resource):
    
    def get(self, id):
        return jsonify(client._get(client.release(id).data['resource_url']))

api_bp = Blueprint('discogs_releases', __name__)
api = Api(api_bp)
api.add_resource(DiscogsRelease, '/release/<int:id>')
