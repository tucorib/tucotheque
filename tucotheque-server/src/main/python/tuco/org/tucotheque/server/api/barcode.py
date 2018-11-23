'''
Created on 22 nov. 2018

@author: tuco
'''
from flask import Blueprint, jsonify
from tuco.org.tucotheque.server.services import vinyls
from flask_restful import Resource, Api

class Barcode(Resource):
    
    def get(self, barcode):
        results = {'results': []}
        results['results'] += vinyls.search(barcode)
        return jsonify(results)

api_bp = Blueprint('barcode', __name__)
api = Api(api_bp)    
api.add_resource(Barcode, '/<string:barcode>')