from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/helloworld/<user>/<int:age>/<float:height>")
def hello_world(user, age, height):
  print(age)
  print(f"Type of the variable age: {type(age)}")
  print(f"Type of the variable user: {type(user)}")
  print(f"Type of the variable height: {type(height)}")
  return f"<h1>Hello, World! user: {user.upper()} </h1>"


@app.route("/welcome")
def welcome():
  return "<h1>Welcome ! </h1>"


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