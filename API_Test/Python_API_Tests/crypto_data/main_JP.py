import bs4, json, requests

res = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')
res.raise_for_status()
response = res.json()



#Need to transfer the ticker symbols to a new dictionary w/ no values (instead of list)
tickerSymbols =[]

def getTickerSymbols():
    for i, v in response['Data'].items():
        if v['IsTrading']:
            tickerSymbols.append(i)

getTickerSymbols()





