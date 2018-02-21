import bs4, json, requests


#Need to transfer the ticker symbols to a new dictionary w/ no values (instead of list)

#Globals
tickerSymbols =[]
prices = []
cryptoPrices = {}


def getTickerSymbols():
    res = requests.get('https://min-api.cryptocompare.com/data/all/coinlist')
    res.raise_for_status()
    response = res.json()
    for i, v in response['Data'].items():
        if v['IsTrading']:
            tickerSymbols.append(i)
#getTickerSymbols()


def getAllTickerPrices():
    for i in tickerSymbols:
        res = requests.get('https://min-api.cryptocompare.com/data/price?fsym=' + i + '&tsyms=USD')
        res.raise_for_status()
        response = res.json()
        print(response)

#getAllTickerPrices()


def getprices(base, pair):
    exchangesAll = ['Coinbase', 'Cryptopia', 'Poloniex', 'HitBTC', 'Gemini', 'Bittrex']
    exchangesUSD = ['Coinbase', 'Gemini']
    comparisonDict = {}
    innerComparison ={}
    for i in exchangesUSD:
        res = requests.get('https://min-api.cryptocompare.com/data/price?fsym=' + base + '&tsyms=' + pair + ',USD&e=' + i)
        res.raise_for_status()
        response = res.json()
        print(i + '(' + base + ' prices)')
        print('*items*')
        print(response.items())
        print('*keys*')
        print(response.keys())
        print('*values*')
        print(response.values())
        for key, value in response.items():
            print(key + ' - ' + str(value))
        print('\n\n')


    print(comparisonDict)
    return comparisonDict
        #    print('VARIABLE i -- ' + i)
        #    print('VARIABLE X -- ' + str(x))
        #    print('VARIABLE V -- ' + str(v))
        #    print('\n')

#getprices('ETH', 'BTC')

#def arbitragecalc(targetCoin, tradingPair):
    #exchangeData = getprices(targetCoin, tradingPair)




def gethistoricalprice(base, pair):
    res = requests.get('https://min-api.cryptocompare.com/data/histoday?fsym=' + base + '&tsym=' + pair + '&toTs=1518220800' + '&limit=10')
    res.raise_for_status()
    response = res.json()
    dataOut = response['Data']

    for i in dataOut:
        for key, value in i.items():
            print(key + ' --- ' + str(value))

        print('--NEXT---\n')

gethistoricalprice('BTC', 'USD')

