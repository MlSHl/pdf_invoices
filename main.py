import requests

api_key = "60b6d83018ef4f4a912afb95313925ae"
url = ("https://newsapi.org/v2/everything?q=apple&from=2024-02-"
       "25&to=2024-02-25&sortBy=popularity&apiKey=60b6d83018ef4f"
       "4a912afb95313925ae")
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
