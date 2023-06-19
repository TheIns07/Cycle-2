import requests

url = "https://streaming-availability.p.rapidapi.com/v2/services"

headers = {
	"X-RapidAPI-Key": "b91daa5fb6msha897dfb06b2473bp1098c0jsnf65794ed3609",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())