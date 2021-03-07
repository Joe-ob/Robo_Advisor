# this is the "app/robo_advisor.py" file

import requests
import json
import os
import datetime
import csv


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)



request_url = ("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo")
response=requests.get(request_url)

parsed_response=json.loads(response.text)
tsd=parsed_response["Time Series (Daily)"]
dates=list(tsd.keys()) 
latest_day=dates[0]

last_refreshed=parsed_response["Meta Data"]["3. Last Refreshed"]

latest_close=tsd[latest_day]["4. close"]

high_prices=[]
low_prices=[]

for day in dates:
    daily_high=float(tsd[day]["2. high"])
    high_prices.append(daily_high)

    daily_low=float(tsd[day]["3. low"])
    low_prices.append(daily_low)

recent_high=max(high_prices)
recent_low=min(low_prices)


csv_file_path=os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers=["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file:
    writer=csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for day in dates:

        writer.writerow({
            "timestamp": day,
            "open": to_usd(float(tsd[day]["1. open"])),
            "high": to_usd(float(tsd[day]["2. high"])),
            "low": to_usd(float(tsd[day]["3. low"])),
            "close": to_usd(float(tsd[day]["4. close"])),
            "volume": tsd[day]["5. volume"]
        })

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"Writing Data to CSV File Path: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")




