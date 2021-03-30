## Import Flask
## need `request` for HTTP requests
import flask
from flask import request
## Create instance of flask
app = flask.Flask(__name__)

## Tell Flask what URL should trigger which function
@app.route('/')
def index():
  return 'Index Page'

@app.route('/hello')
def hello_world():
  return 'Hello, World!'

## HTTP requests

def i_am_a_GET():
  return 'You have called a GET function'

def i_am_a_POST():
  return 'You have called a  POST function'

def i_am_a_PUT():
  return 'You have called a PUT function'

def i_am_a_DELETE():
  return 'You have called a  DELETE function'


## be sure to import `requests` from flask
@app.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def test():
  if request.method == 'POST':
    return i_am_a_POST()
  elif request.method == 'PUT':
    return i_am_a_PUT()
  elif request.method == 'DELETE':
    return i_am_a_DELETE()
  else:
    return i_am_a_GET()