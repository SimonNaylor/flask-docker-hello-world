from flask import Flask, jsonify, request
import requests

# configuration
Debug= False

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)




# PING PONG
@app.route('/ping', methods=['GET'])
def ping_pong():
    '''Returning pong! for any response'''
    return jsonify('pong!')



@app.route('/word', methods=['GET'])
def word():
    '''Returns a random word, flips it, and sets to the uppercase.'''
    word1 = requests.get('https://random-word-api.herokuapp.com/word?number=1').json()[0][::-1].upper()
    return jsonify(word1)

@app.route('/string-count', methods=['POST'])
def string_count():
    '''Returns the string count of a word'''
    data = requests.get('https://random-word-api.herokuapp.com/word?number=1').json()[0]
    word = len(data)
    return jsonify(word)

if __name__ == '__main__':
    app.run()

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
