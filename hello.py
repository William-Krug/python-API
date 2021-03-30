## Import Flask
from flask import Flask
## Create instance of flask
app = Flask(__name__)

## Tell Flask what URL should trigger which function
@app.route('/')
def index():
  return 'Index Page'

@app.route('/hello')
def hello_world():
  return 'Hello, World!'

def i_am_a_GET():
  return 'You have called a GET function'

def i_am_a_POST():
  return 'You have called a  POST function'

@app.route('/test', methods=['GET', 'POST'])
def test():
  if request.method == 'POST':
    return i_am_a_POST()
  else:
    return i_am_a_GET()