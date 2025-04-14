from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/helloworld/<user>/<int:age>/<float:height>")
def hello_world(user, age, height):
  return {
    "User": str(app), 
    "Age": age, 
    "Height": height, 
  }


@app.route("/welcome")
def welcome():
  return {"message": "Hello World"}


@app.route("/projects/")
def projects():
  return "The project page"


@app.route("/about", methods=["GET", "POST"])
def about():
  if request.method == "GET":
    return "This is a GET"
  else:
    return "This is a POST"


with app.test_request_context():
  url = "/about"
  print(url_for('welcome'))
  print(url_for('projects'))
  print(url_for('about', next='/'))
  print(url_for('hello_world', user="John Doe", age=32, height=1.75))