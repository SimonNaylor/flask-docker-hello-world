import uuid
from flask import Flask, jsonify, request

import requests

# configuration
Debug= False

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)



# EXCEPTION HANDLER
from flask import json
from werkzeug.exceptions import HTTPException
import logging # <-- added

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    logging.exception(e) # <-- added
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response



# PING PONG
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/word')
def word():
    word1 = requests.get('https://random-word-api.herokuapp.com/word?number=1')
    upper = word1[::-1].upper()
    return jsonify(upper)

#@app.route('/string-count', methods=['GET'])
#def string():



if __name__ == '__main__':
    app.run()
