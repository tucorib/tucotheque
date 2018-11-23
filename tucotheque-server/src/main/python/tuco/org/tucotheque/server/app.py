'''
Created on 22 nov. 2018

@author: tuco
'''
from flask import Flask
from tuco.org.tucotheque.server.api.barcode import api_bp as barcode_api
from tuco.org.tucotheque.server.api.discogs import api_bp as discogs_api
from tuco.org.tucotheque.server.config import config

app = Flask(__name__)
app.register_blueprint(barcode_api, url_prefix='/barcode')
app.register_blueprint(discogs_api, url_prefix='/discogs')

if __name__ == '__main__':
    app.run(host=config.get('api.host'), port=config.get('api.port'))