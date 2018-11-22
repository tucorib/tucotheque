'''
Created on 22 nov. 2018

@author: tuco
'''
from flask import Flask
from tuco.org.tucotheque.server.api.search import api_bp as search_api
from tuco.org.tucotheque.server.config import config

app = Flask(__name__)
app.register_blueprint(search_api)

if __name__ == '__main__':
    app.run(host=config.get('api.host'), port=config.get('api.port'))