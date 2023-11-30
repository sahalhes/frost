from flask import Flask, render_template
import yfinance as yf
import pandas as pd
from flask import Flask

app = Flask(__name__)

def get_total_trend_points(ticker):
    # (The unchanged function definition)
    # ...
    

@app.route('/')
def index():
    tickersPointsDict = {}
    with open('sp500.csv', 'r') as file:
        sp500_list = [line.rstrip('\n') for line in file]
    stringOfTickers = ' '.join(sp500_list)

    data = yf.download(stringOfTickers, group_by="ticker", period='100d')
    for symbol in sp500_list:
        points = get_total_trend_points(data[symbol])
        tickersPointsDict[symbol] = points

    topStocks = hillClimbTop(tickersPointsDict, 20)
    bottomStocks = hillClimbBottom(tickersPointsDict, 20)

    return render_template('index.html', topStocks=topStocks, bottomStocks=bottomStocks)

if __name__ == '__main__':
    app.run(debug=True)
