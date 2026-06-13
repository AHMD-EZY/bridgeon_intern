import requests
def fetch_user(username: str)->dict:
    try:
        url=f"https://api.github.com/users/{username}"
        response=requests.get(url)
        if response.status_code==200:
            return response.json()
        return{}
    except exeption:
        print("Error fetching data:", exeption)
        return{}
def joke()->tuple(str, str):
    try:
        res=requests.get("https://official-joke-api.appspot.com/jokes/random")
        if res.status_code==200:
            joke=res.json()
            return joke["setup"], joke["punchline"]
        return "",""
    except exeption:
        print("Error fetching joke:", exeption)
        return "",""
def display_user(username: str)->None:
    if not user:
        print("User not found.")
        return
    print(f"Name: {user.get('name')}")
    print(f"Location: {user.get('location')}")
    print(f"Public Repos: {user.get('public_repos')}")
    print(f"Created At: {user.get('created_at')}")
username=input("Enter GitHub username:")
user=fetch_user(username)
display_user(username)
setup, punchline=joke()
print("\nJoke:")
print(f"Setup: {setup}")
print(f"Punchline: {punchline}")