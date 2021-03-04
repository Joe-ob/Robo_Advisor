# this is the "app/robo_advisor.py" file
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
ALPHAVANTAGE_API_KEY=os.getenv("ALPHAVANTAGE_API_KEY")


stock_symbol=input("Please enter the cryptocurrency or stock ticker you are looking for:")
print("Requesting Stock Market Data for", stock_symbol, "...")

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={ALPHAVANTAGE_API_KEY}"
response=requests.get(request_url)


parsed_response = json.loads(response.text)
#print(parsed_response["Time Series (Daily)"])

print(parsed_response["Time Series (Daily)"]["2021-03-03"])

for item{} in parsed_response["Time Series (Daily)"]:
    print(item)
    for data in item:
        print(data)

