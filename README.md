# Python Server Side

## Resources

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [psycopg2](https://pypi.org/project/psycopg2/)

## Creating routes

@app.route('/')
def index():
return 'Index Page'

@app.route('/hello')
def hello_world():
return 'Hello, World!'

## Set up App

`import Flask`
`app = flask.Flask(__name__)`

`@app.route('/')`
`def hello_world():`
`return 'Hello, World!'`

## Running the App

`export FLASK_APP=pageName.py`
`flask run`

or

`export FLASK_APP=pageName.py`
`python -m flask run`

app can now be viewed at http://127.0.0.1:5000/
