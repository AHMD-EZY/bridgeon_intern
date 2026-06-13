import requests

res = requests.get("https://api.github.com/users/AHMD-EZY")

if res.status_code == 200:
    data = res.json()

    print(f"Name: {data['name'] }")
    print(f"Location: {data['location'] }")
    print(f"Public Repos: {data['public_repos']}")
    print(f"Created At: {data['created_at']}")

else:
    print("Error fetching data:", res.status_code)