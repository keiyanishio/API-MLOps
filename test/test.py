import requests as req

print(req.get("http://localhost:8000/").text)