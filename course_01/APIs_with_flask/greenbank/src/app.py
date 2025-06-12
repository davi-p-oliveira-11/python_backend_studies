from flask import Flask, url_for, request, jsonify

app = Flask(__name__)


@app.route("/olamundo/<usuario>/<int:idade>/<float:altura>")
def hello_world(usuario, idade, altura):
      return jsonify(
            {
              'Usuario': usuario,
              'Idade': idade,
              'Altura': altura,
            }
      )


@app.route("/bemvindo")
def bem_vindo():
      return {"message": "Ola mundo"}


@app.route("/projects/")
def projects():
      return "The project page"


@app.route("/about", methods=["GET", "POST"])
def about():
      if request.method == 'GET':
            return 'This is a  GET'
      else:
            return 'This is a POST'


with app.test_request_context():
      url = '/about'
      print(url_for("bem_vindo"))  
      print(url_for("projects"))
      print(url_for("about", next="/")) 
      print(url_for("hello_world", usuario="guilherme", idade=29, altura=1.64))
  