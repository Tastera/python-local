import requests
from bs4 import BeautifulSoup

url = "https://ko.valutafx.com/KRW.htm"
res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')
EUR = soup.find_all("div", {"class":"padding-10"}, "div", {"class":"crt"})

#pick = soup.select('#tab_P div.padding-10 div.crt')
 #tab_P > div.padding-10 > div
 #tab_P > div.padding-10 > div
 #tab_P > div.padding-10
#for country in pick:
#   print(country.select_one("#tab_P > div.padding-10 > div > div:nth-of-type(7)"))
    #tab_P > div.padding-10 > div > div:nth-child(7)
    #print(country.select_one("div:nth-of-type(8) strong"))
    #tab_P > div.padding-10 > div > div:nth-child(8)

for cena_EUR in EUR:
    print(cena_EUR.text)