import requests
from bs4 import BeautifulSoup

url = "https://www.bithumb.com/"
res = requests.get(url).text # .text가 없으면 객체 자체가 나옴. 문서화 해야하기에 .text

soup = BeautifulSoup(res, 'html.parser')

# pick = soup.select('#tableAsset > tbody > tr:nth-of-type(1) > td:nth-of-type(1)')
pick = soup.select('tbody.coin_list tr') # tr 안에 많은 요소가 있구먼
for coin in pick:
    print(coin.select_one("td:nth-of-type(1) a strong").text)
    print(coin.select_one("td:nth-of-type(2) strong").text)