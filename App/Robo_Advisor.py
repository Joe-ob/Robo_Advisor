# this is the "app/robo_advisor.py" file

import requests
import json
import datetime


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)



request_url = ("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo")
response=requests.get(request_url)
#print(type(response)) #<>lass 'requests.models.Response'>
#print(response.status_code) #>200
#print(response.text)
parsed_response=json.loads(response.text)
print(parsed_response.keys())

Last_refreshed=parsed_response["Meta Data"]["3. Last Refreshed"]

print(Last_refreshed)

latest_close=parsed_response["Time Series (Daily)"]["2021-03-05"]["4. close"]
print(latest_close)



print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {Last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")



