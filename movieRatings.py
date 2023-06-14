import requests

url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer Madagascar 2"
}

response = requests.get(url, headers=headers)

print(response.text)