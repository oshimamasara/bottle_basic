from bottle import route, run, request
import requests
import json

@route('/')
def hello():
    return "こんにちは"

@route('/225')
def greet():
    response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=^N225&interval=5min&apikey=T8ST9ZM5WP7JNMNG')
    data = json.loads(response.text)
    print(data.keys())
    data = data["Time Series (5min)"]
    latest_date = sorted(data.keys())[-1]
    stock_price = data[latest_date]["4. close"]
    return "アメリカ東部時間: " + latest_date + "の 日経225 の最新株価: " + stock_price

run(host='localhost', port=8080, debug=True)

server.stop()
