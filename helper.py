import requests
from requests import status_codes
from requests.models import HTTPError
import json
import sqlite3
import os


class requestHandler():
    base_url = "https://americas.api.riotgames.com"

    # FIXME:  # Remove before production; Take token from legit source

    data = json.load(open("token.json", "r"))
    token = data["token"]
    gameName = data["gameName"]
    tagLine = data["tagLine"]

    header = {
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": token
    }

    def get_puuid_request_url(gameName: str, tagLine: str) -> dict:
        """
        Returns AccountDto (Refer to Riot Docs at: https://developer.riotgames.com/apis#account-v1)

            Parameters:
                gameName (str): In-game name
                tagLine (str): Tag line that goes with the name

            Returns:
                MatchlistDto (dict): dictionary of AccountDto JSON converted using json package

            Raises:
                HTTPError: Raises HTTPError with response status code
        """
        try:
            response = requests.get(
                requestHandler.base_url + "/riot/account/v1/accounts/by-riot-id/" + gameName + "/" + tagLine, headers=requestHandler.header)
        except HTTPError:
            response.raise_for_status()
        else:
            return response.json()

    def get_match_request_url(puuid: str) -> dict:
        """
        Returns MatchlistDto (Refer to Riot Docs at: https://developer.riotgames.com/apis#val-match-v1)

            Parameters:
                puuid (str): In-game name

            Returns:
                MatchlistDto (dict): dictionary of MatchlistDto JSON converted using json package

            Raises:
                HTTPError: Raises HTTPError with response status code
        """
        try:
            response = requests.get(
                requestHandler.base_url + "/val/match/v1/matchlists/by-puuid/" + puuid, headers=requestHandler.header)
        except HTTPError:
            response.raise_for_status()
        else:
            return response.json()


def createDB() -> None:
    try:
        # create matchlist db
        if("matchlist.db" not in os.listdir(os.getcwd())):
            matchlist_conn = sqlite3.connect(
                'matchlist.db')  # MatchlistEntryDto
            c = matchlist_conn.cursor()
            c.execute("""CREATE TABLE matchlist(
                matchId INTEGER PRIMARY KEY,
                gameStartTimemillis INTEGER,
                teamId TEXT
            )""")
            matchlist_conn.commit()
            print("matchlist initialized")
        else:
            print("matchlist already created")

        # create matches db
        if("matches.db" not in os.listdir(os.getcwd())):
            matches_conn = sqlite3.connect('matches.db')
            c = matches_conn.cursor()
            c.execute("""CREATE TABLE matches(
                matchInfo BLOB,
                players BLOB,
                coaches BLOB,
                teams BLOB,
                roundResults BLOB
            )
            """)
            matches_conn.commit()
            print("matches initialized")
        else:
            print("matches already created")

        # create matchinfo db
        if("matchinfo.db" not in os.listdir(os.getcwd())):
            matchinfo_conn = sqlite3.connect('matchinfo.db')  # MATCHINFO DTO
            c = matchinfo_conn.cursor()
            c.execute("""CREATE TABLE matchinfo(
                matchId TEXT PRIMARY KEY,
                mapId TEXT,
                gameLengthMillis INTEGER,
                gameStartMillis INTEGER,
                provisioningFlowId TEXT,
                isCompleted INTEGER,
                customGameName TEXT,
                queueId TEXT,
                gameMode TEXT,
                isRanked INTEGER,
                seasonId TEXT
            )""")
            matchinfo_conn.commit()
            print("matchinfo initialized")
        else:
            print("matchinfo already created")

        # create player db
        if("player.db" not in os.listdir(os.getcwd())):
            player_conn = sqlite3.connect('player.db')
            c = player_conn.cursor()
            c.execute("""CREATE TABLE player(
                puuid TEXT,
                gameName TEXT,
                tagLine TEXT,
                teamId TEXT,
                partyId TEXT,
                characterId TEXT,
                stats BLOB,
                competitiveTier INTEGER,
                playerCard TEXT,
                playerTitle TEXT
            )""")
            player_conn.commit()
            print("player.db intialized")
        else:
            print("player.db already created")
        if("matchlist.db" not in os.listdir(os.getcwd())):
            playerstats_conn = sqlite3.connect('playerstats.db')
            c = playerstats_conn.cursor()
            c.execute("""CREATE TABLE playerstats(
                score INTEGER,
                roundsPlayed INTEGER,
                kills INTEGER,
                deaths INTEGER,
                assists INTEGER,
                playtimeMillis INTEGER,
                abilityCasts BLOB
            )""")
            playerstats_conn.commit()
            print("playerstats.db intialized")
        else:
            print("playerstats.db already created")

        if("ability.db" not in os.listdir(os.getcwd())):
            ability_conn = sqlite3.connect('ability.db')
            c = ability_conn.cursor()
            c.execute("""CREATE TABLE ability(
                grenadeCasts INTEGER,
                ability1Casts INTEGER,
                ability2Casts INTEGER,
                ultimateCasts INTEGER
            )""")
            ability_conn.commit()
            print("ability.db initialized")
        else:
            print("ability.db already created")

        if("team.db" not in os.listdir(os.getcwd())):
            team_conn = sqlite3.connect('team.db')
            c = team_conn.cursor()
            c.execute("""CREATE TABLE team(
                teamId TEXT,
                won INTEGER,
                roundsPlayed INTEGER,
                roundsWon INTEGER,
                numPoints INTEGER
            )""")
            team_conn.commit()
            print("teamconn.db initialized")

        else:
            print("teamconn.db already created")
        print("All DB created")
    except Exception as e:
        print("db error")
        raise("DB ERROR")


def updateDBfromAPI(){

}
