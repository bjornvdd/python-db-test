import json
import requests
from pprint import pprint


# checking op status code 200 OK
def test_get_all_players():
    response = requests.get("http://127.0.0.1:8000/all/players")
    assert response.status_code == 200
    #print for debugging purposes
    print(response.status_code)


# checking op status code 200 OK
def test_get_all_teams():
    response = requests.get("http://127.0.0.1:8000/all/teams")
    assert response.status_code == 200
    #print for debugging purposes
    print(response.status_code)


# checking op status code 200 OK
def test_get_all_stadiums():
    response = requests.get("http://127.0.0.1:8000/all/stadiums")
    assert response.status_code == 200
    print(response.status_code)


# hier gaat hij kijken of dat de rank bestaat of niet als de rank niet bestaat passed hij omda ik een status code 404 heb meegegeven.
# Wanneer de rank wel bestaat dan failed hij...
def test_get_specific_rank_if_not_exist():
    response = requests.get("http://127.0.0.1:8000/team/rank?rank=3")
    assert response.status_code == 404
    #print for debugging purposes
    print(response.status_code)


# post requests
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

#POST TEST
def test_make_player():
    url = "http://127.0.0.1:8000/make/player"
    body = {
        "id": 0,
        "first_name": "bjorndd",
        "last_name": "vdd",
        "email": "vdd@gmail.com",
        "number": 18,
        "birth_date": "17/10/1799",
        "password": "test"
    }

    response = requests.post(url, data=body, headers=headers)
    print(response.status_code)
    pprint(response.json())
