# this is the "app/robo_advisor.py" file

import requests
import json
import datetime


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)



request_url = ("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo")
response=requests.get(request_url)

parsed_response=json.loads(response.text)

tsd=parsed_response["Time Series (Daily)"]

dates=list(tsd.keys()) #This assumes first day is on top but can sort later

latest_day=dates[0]

Last_refreshed=parsed_response["Meta Data"]["3. Last Refreshed"]

latest_close=tsd[latest_day]["4. close"]

high_prices=[]
for day in dates:
    daily_high=float(tsd[day]["2. high"])
    high_prices.append(daily_high)
recent_high=max(high_prices)



print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {Last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")



