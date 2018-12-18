import requests
from bs4 import BeautifulSoup

url = "https://sports.media.daum.net/sports/record/primera"
res = requests.get(url).text

soup = BeautifulSoup(res, 'html.parser')
pick = soup.select('tbody. tr')

for rank in pick:
    print(rank.select_one("td:nth-of-type(2) a strong").text)
    print(rank.select_one("td:nth-of-type(3) strong").text)