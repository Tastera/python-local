import requests
from bs4 import BeautifulSoup

url = "https://www.coinnest.co.kr/"
res = requests.get(url).text

soup = BeautifulSoup(res, 'html.parser')
pick = soup.select('ul.price_today_ul li')

for coin in pick:
    print(coin.select_one("li:nth-of-type(1) a strong"))
    print(coin.select_one("li:nth-of-type(2) strong"))

    #price_today_ul > li:nth-child(1) > a > dl > dt