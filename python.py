import requests
from bs4 import BeautifulSoup

url = "https://ko.valutafx.com/KRW.htm"
res = requests.get(url)
print(res)

print("hihi")