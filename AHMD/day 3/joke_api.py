import requests
res=requests.get("https://official-joke-api.appspot.com/jokes/random")
if res.status_code==200:
    joke=res.json()
    print(joke["setup"])
    print(joke["punchline"])
else:
    print("Error:", res.status_code)