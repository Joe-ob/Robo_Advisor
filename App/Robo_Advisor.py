# this is the "app/robo_advisor.py" file

import csv
import datetime
import json
import os
from dotenv import load_dotenv
import requests
import plotly
import plotly.graph_objs as go


#This is used later to print current Date/Time
now=datetime.datetime.now()
now_formatted=now.strftime("%Y-%m-%d %H:%M:%S")

#Function to convert values to dollars
def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#Needed to bring in API key from Env variable
load_dotenv()
api_key=os.environ.get("ALPHAVANTAGE_API_KEY")

#Boolean value in a while loop for data validation
#Collaborated with John Sansbury for this part
is_ticker_valid=False

while is_ticker_valid==False:
    ticker=input("Please enter a valid ticker for the stock you wish to analyze: ")
    if len(ticker) >= 1 and len(ticker) <= 5 and ticker.isalpha() == True:
        ticker=ticker.upper()

        request_url = (f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={api_key}")
        response=requests.get(request_url)

        #parses data to a useable/dynamic format
        parsed_response=json.loads(response.text)
        
        if parsed_response=={'Error Message': 'Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY.'}:
            print("You have entered an invalid stock ticker that is either invalid or not tracked by the API. Please try again")

            is_ticker_valid=False
        
        else:

            is_ticker_valid=True
    else:
        print("The ticker you entered is invalid, please try again.")
        is_ticker_valid=False



tsd=parsed_response["Time Series (Daily)"]
dates=list(tsd.keys()) 
latest_day=dates[0]

#pulls date of most recent update
last_refreshed=parsed_response["Meta Data"]["3. Last Refreshed"]

#most recent close price
latest_close=float(tsd[latest_day]["4. close"])

#creates lists to append data in for loop
high_prices=[]
low_prices=[]
close_prices=[]


for day in dates:

    daily_high=float(tsd[day]["2. high"])
    high_prices.append(daily_high)

    daily_low=float(tsd[day]["3. low"])
    low_prices.append(daily_low)

    daily_close=float(tsd[day]["4. close"])
    close_prices.append(daily_close)

 
#find 52 week high low and average
recent_high=max(high_prices)
recent_low=min(low_prices)
ave_close=sum(close_prices)/len(close_prices)


#uses current and ave price to make recomendation
if latest_close>ave_close:
    rec="Buy"
    rec_reason="This stock is trading above its 6-month average. You might want to ride the momentum"
else:
        rec="Sell"
        rec_reason="Be careful, This stock is trading below its 6-month average. It's value may be dropping"

#posts data in  csv file
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

#prints output
print("-------------------------")
print(f"SELECTED SYMBOL: {ticker}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {now_formatted}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"RECOMMENDATION: {rec}")
print(f"RECOMMENDATION REASON: {rec_reason}")
print("-------------------------")
print(f"Writing Data to CSV File Path: {csv_file_path}")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")



#Plots daily closing price against time
plotly.offline.plot({
    "data": [go.Scatter(x=dates, y=close_prices)],
    "layout": go.Layout(title=f"{ticker} close prices")
}, auto_open=True)

