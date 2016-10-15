from flask import Flask, request, jsonify, json

app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Nehemiah has the best body."
@app.route("/pets", methods = ['GET', 'POST'])
def storePets():
    result = request.form
    return result["age"]

@app.route("/hello", methods = ['GET', "POST"])
def bigbutts():
    result = request.form
    return result["HELLO WORLD"]
if __name__ == "__main__":
    app.run()
