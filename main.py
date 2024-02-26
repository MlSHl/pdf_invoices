import requests
from functions import send_email

api_key = "60b6d83018ef4f4a912afb95313925ae"
url = ("https://newsapi.org/v2/everything?q=apple&from=2024-02-"
       "25&to=2024-02-25&sortBy=popularity&apiKey=60b6d83018ef4f"
       "4a912afb95313925ae")
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
message = ""
for article in content["articles"]:
    title = (article["title"]).strip()
    desc = (article["description"]).strip()
    message = message + "title: " + title + "\n" + "desc: " + desc + 2*"\n"

message = message.encode('utf-8')
send_email(message)