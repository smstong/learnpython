import json
import requests
import matplotlib.pyplot as plt

APIKEY='NX5Z0HJIO33UE859'
api_uri_base = 'https://www.alphavantage.co/query?'

def get_intraday(symbol, interval):
	api_uri = '{}function=TIME_SERIES_INTRADAY&symbol={}&interval={}&apikey={}'.format(api_uri_base,symbol,interval,APIKEY)
	response = requests.get(api_uri)
	if response.status_code == 200:
		return (response.content)
	else:
		print('error:{}'.format(response.status_code))
		return None

def get_daily(symbol):
	api_uri = '{}function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&outputsize=compact&apikey={}'.format(
			api_uri_base, symbol,APIKEY)
	response = requests.get(api_uri)
	if response.status_code == 200:
		return (response.content)
	else:
		print('error:{}'.format(response.status_code))
		return None

# data = get_intraday('MSFT', '1min')

data = get_daily('BNS')

if data is not None:
	obj = json.loads(data)
	a = []
	i = 0
	for day in obj['Time Series (Daily)'].items():
		i += 1
		if i > 30:
			break;
		a.append(float(day[1]['4. close']))
	a.reverse()
	print(a)
	plt.plot(a)
	plt.show()
else:
	print('No')
