import requests

print("Github repository information fetcher")

username = input("Enter username: ")
repo = input("Enter repo name: ")

url = f"https://api.github.com/repos/{username}/{repo}"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print("\nRepository Information")
    print(f"Name: {data['name']}")
    print(f"Owner: {data['owner']['login']}")
    print(f"Description: {data['description']}")
    print(f"Stars: {data['stargazers_count']}")
    print(f"Forks: {data['forks_count']}")
    print(f"Language: {data['language']}")
    print(f"URL: {data['html_url']}")
else:
    print("Repository not found.")