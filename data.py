import requests
PARAMETERS = {
    "amount": 10,
    "type": "boolean",
}
api_pull = requests.get("https://opentdb.com/api.php", params=PARAMETERS)
api_pull.raise_for_status()

question_data = api_pull.json()["results"]


