import os
from flask import Flask
from models import setup_db
from flask_cors import CORS
import boto3 


def create_app(test_config=None):

    client = boto3.client(
        excited = EXCITED,
    )

    app = Flask(__name__)
    setup_db(app)
    CORS(app)


    @app.route('/')
    def get_greeting():
        excited = client.excited
        greeting = "Hello" 
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()