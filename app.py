from flask import Flask
import json
import requests


app = Flask(__name__)


@app.route("/")
def index():
    return

@app.route("/authsuccess")
def authsuccess():

    # getting token, gameName, and tagLine from token.json
    # only for test purposes before implementing auth using RSO
    data = json.load(open("token.json","r"))
    token = data["token"]
    gameName = data["gameName"]
    tagLine = data["tagLine"]

    # hard coding for getting account puuid by riot id
    url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id"
    header = {
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": token
    }
    
    response = requests.get(url+ "/" + gameName + "/" + tagLine, headers=header)
    print(response.status_code)
    return response.text
