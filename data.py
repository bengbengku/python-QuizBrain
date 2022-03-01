import requests

parameters = {
    "amount": 10,
    "difficulty": "medium",
    "type": "boolean"
}

res = requests.get("https://opentdb.com/api.php", params=parameters)
res.raise_for_status()
data = res.json()
question_data = data["results"]
