'''
Created on 22 nov. 2018

@author: tuco
'''
from flask import Flask
from tuco.org.tucotheque.server.api.search import api_bp as search_api

app = Flask(__name__)
app.register_blueprint(search_api)

if __name__ == '__main__':
    app.run()