import requests
from functions import send_email

topic = "apple"
api_key = "60b6d83018ef4f4a912afb95313925ae"
url = (f"https://newsapi.org/v2/everything?q={topic}&from=2024-02-"
       "25&to=2024-02-25&sortBy=popularity&apiKey=60b6d83018ef4f"
       "4a912afb95313925ae&language=en")
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()
message = "Subject: Today's News" + "\n"
for article in content["articles"][0:20]:
    title = (article["title"]).strip()
    desc = (article["description"]).strip()
    message = message + "title: " + title + "\n" + "desc: " + desc + f"URL:{article['url']}" + 2*"\n"

message = message.encode('utf-8')
send_email(message)