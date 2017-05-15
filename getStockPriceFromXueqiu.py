#!/usr/bin/python3
# This program is used get stock price from Xueqiu website
import time
import datetime
import requests
import bs4

today = datetime.datetime.now()
print('Today is', today.date().isoformat())
print('\n')
# headers will simulate browser to access and avoid https 403 error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko\
/20100101 Firefox/23.0'}
stockpool = {'Walmart': 'WMT', 'Coca-Cola': 'KO', 'Reynolds American': 'RAI',
             'Amazon': 'AMZN'}
for k, v in stockpool.items():
    xqurl = "https://xueqiu.com/S/" + v
    res = requests.get(xqurl, headers=headers)
    # 'html.parser' will solve 'No parser was specified' warning
    resSoup = bs4.BeautifulSoup(res.text, "html.parser")

    # The source html source code sample:
    # '<strong data-current="75.71" class="stockDown">$75.71</strong>'
    stprice = resSoup.select('strong[data-current]')
    stockprice = stprice[0].getText()
    print('Stock price of', k, 'is', stockprice)

time.sleep(2)
print('\nThe end')
