from flask import Flask, jsonify, request 

app = Flask(__name__)

@app.route("/profile/")
def profile():
    return jsonify(
        slackUsername = "supra243",
        backend = True,
        age = 20,
        bio = "i am a backend developper"
    )

@app.route("/arithmetic/")
def arithmetic():
    x = request.json.get('x', None)
    y = request.json.get('y', None)
    operation_type = request.json.get('operation_type', None)

    if operation_type is None or x is None or y is None:
        return None

    if operation_type == "addition":
        result = x+y
    elif operation_type == "multiplication":
        result = x*y
    elif operation_type == "subtraction":
        result = x-y
    else:
        result = None
    return jsonify(
        slackUsername = "supra243",
        operation_type = operation_type,
        result = result
    )
        
        
        