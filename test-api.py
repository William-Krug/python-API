import flask
import psycopg2 
from flask import request, jsonify, make_response
from psycopg2.extras import RealDictCursor

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def homePage():
  return "<h1>This is the TESTING home page</h1>"

@app.route('/getAll', methods=['GET'])
def api_GET():
  connection = psycopg2.connect(
    user="zeddicus",
    host="127.0.0.1",
    port="5432",
    database="python_db"
  )
  cursor = connection.cursor()
  sqlQuery = 'SELECT * FROM "test"'
  cursor.execute(sqlQuery)
  data = cursor.fetchall()
  return jsonify(data)

@app.route('/add', methods=['POST'])
def api_POST():
  name = request.form['name']
  age = request.form['age']
  bo = request.form['bool']
  try:
    connection = psycopg2.connect(
      user="zeddicus",
      host="127.0.0.1",
      port="5432",
      database="python_db"
    )
    cursor = connection.cursor(cursor_factory=RealDictCursor)

    print(name, age, bo)
    sqlQuery = 'INSERT INTO "test" (name, age, bool) VALUES (%s, %s, %s)'
    cursor.execute(sqlQuery, (name, age, bo))
    connection.commit()
    count = cursor.rowcount
    print(count, "object INSERTED")
    result = {'status': 'CREATED'}
    return make_response(jsonify(result), 201)
  except (Exception, psycopg2.Error) as error:
    if(connection):
      print("Failed to insert object", error)
      result = {'status': 'ERROR'}
      return make_response(jsonify(result), 500)
  finally:
    if(connection):
      cursor.close()
      connection.close()
      print("PostgreSQL connection is closed")

app.run()