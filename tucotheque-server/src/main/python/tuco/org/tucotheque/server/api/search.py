'''
Created on 22 nov. 2018

@author: tuco
'''
from flask import Blueprint, request, jsonify
from tuco.org.tucotheque.server.services import vinyls

api_bp = Blueprint('api', __name__)

@api_bp.route('/search')
def search():
    barcode = request.args.get('barcode', None)
    
    results = {'results': []}
    results['results'] += vinyls.search(barcode)
    return jsonify(results)
