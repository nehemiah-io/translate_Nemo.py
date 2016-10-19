from flask import Flask, request, jsonify, json

app = Flask(__name__)
pets = []


@app.route("/")
def hello():
    return "Dogs will rule the world soon!"

@app.route("/pets", methods = ['GET', 'POST'])
def storePets():
    json = request.get_json()
    print(json['age'])
    return jsonify({"theAge" : json['age']})

@app.route("/hello", methods = ['GET', "POST"])
def southpark():
    return "HELLO Children!, Hi Chef!"

@app.route("/hello/<name>")
def Eminem(name):
    return "Hello " + name
if __name__ == "__main__":
    app.run()
