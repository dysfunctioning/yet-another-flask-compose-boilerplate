#!/usr/bin/env python
# flake8: noqa
import os
import json
import time
import db_config
from flask import Flask, request
from backend.app.configuration import config
from backend.db.base import initialize_database


def create_app():
    time.sleep(3)  # TODO: best to implement wait_for_db_is_ready as a decorator here
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_CONNECTION_URI']
    flask_app.app_context().push()
    initialize_database()
    return flask_app



app = create_app()

@app.route('/', methods=['GET'])
def index():
    return 'Boilerplate heating up!'


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return 'heartbeat successful'


port = config.APP_PORT or 9001
environment = os.environ.get('ENV', 'development')
if __name__ == '__main__':
    if environment in ['development', 'testing']:
        print(f'Spinning up {environment} Flask app')
        print(port)
        app.run(host='0.0.0.0', port=port, debug=True)
