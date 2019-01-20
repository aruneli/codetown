import json
import os
import urllib2

stock = 'aapl'
print(stock)


def get_stock_price(stock):
    response = urllib2.urlopen('https://api.iextrading.com/1.0/stock/' + stock + '/chart/1m')
    return json.loads(response.read())


def render(stock):
    map = {}
    response = get_stock_price(stock)
    for res in response:
        value=max((res['high']), (res['low']))
        map[res['label']]=value
    print maxProfit(map)


def maxProfit(map):
        prices = list(map.values())
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        maxProfit = 0
        for p in prices:
            if p < minPrice:
                minPrice = p
            elif p - minPrice > maxProfit:
                maxProfit = p - minPrice
        return maxProfit, prices.index(minPrice), map.keys()[prices.index(minPrice)], prices.index(p), map.keys()[prices.index(p)]


render(stock)





