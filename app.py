from flask import Flask
import json
from requests.models import HTTPError
from helper import requestHandler as rh
from helper import createDB


app = Flask(__name__)


@app.route("/")
def index():
    return


@app.route("/auth")
def auth():
    try:
        # TODO: get puuid from Riot OAuth

        # getting token, gameName, and tagLine from token.json
        # only for test purposes before implementing auth using RSO
        data = json.load(open("token.json", "r"))
        token = data["token"]
        gameName = data["gameName"]
        tagLine = data["tagLine"]
        header = {
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Riot-Token": token
        }

        AccountDto = rh.get_puuid_request_url(gameName, tagLine)
        MatchlistDto = rh.get_match_request_url(AccountDto.get("puuid"))
        test = json.dumps(AccountDto)
        print(AccountDto.get("puuid"))
        createDB()
    except HTTPError as e:
        print("HTTPERROR")
        return {}, e.response.status_code
    except Exception as e:
        print(e)
        return {}, 500
    else:
        return test, 200
