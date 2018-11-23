'''
Created on 23 nov. 2018

@author: tuco
'''
from tuco.org.tucotheque.server.app import app
from flask.helpers import url_for
import urllib

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

if __name__ == '__main__':
    app.config['SERVER_NAME'] = 'localhost'
    with app.app_context():
        for rule in app.url_map.iter_rules():
            options = {}
            for arg in rule.arguments:
                options[arg] = "[{0}]".format(arg)
                
            methods = ','.join(rule.methods)
            url = url_for(rule.endpoint, **options)
            print urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))