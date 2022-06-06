import json
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Try /appointments or /profiles"

@app.route("/appointments")
def appointments():
    f = open("mock_data.json")
    data = json.load(f)
    appointments = []
    for i in data["appointments"]:
        appointments.append(data["appointments"][i])
    return str(appointments)

@app.route("/profiles")
def profiles():
    f = open("mock_data.json")
    data = json.load(f)
    profiles = []
    for i in data["profiles"]:
        profiles.append(data["profiles"][i])
    return str(profiles)