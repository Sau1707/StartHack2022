import json
import string
import flask
from flask import request, jsonify
from matplotlib.style import use

def getData(user: string = None):
    with open("users.json","r") as file:
        if user: return json.loads(file.read())[user]
        return json.loads(file.read())

def writeData(data):
    with open("users.json","w") as file:
        file.write(json.dumps(data, sort_keys=True, indent=4))

def createUser(user: string):
    data = getData()
    data[user] = {}
    writeData(data)

def setData(user, value: dict = None):
    data = getData()
    for key in value:
        data[user][key] = value[key]
    writeData(data)

createUser("test")
print(getData("test"))

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "Hi, I'm an api made by Flask by LastMinute team"

@app.route('/newuser', methods=["POST"])
def newUser():
    if 'id' in request.args:
        createUser(request.args[id])
        return "New user created successfully"
    else:
        return "Error: No id field provided. Please specify an id."



app.run()