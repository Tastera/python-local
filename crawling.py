import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"
# res = request.get(url)
# print(res) # 200이 나온걸 보아하니 정상적으로 연결이 되었군!
 
# res = requests.get(url).text # .text 덕분에
# print(res) # 어떤 내용이 들어있는지 확인할 수 있음

# res = requests.get(url).status_code
# print(res) # <Response [200]>이 아니라 200으로 나오네!

res = requests.get(url).text
# print(res)

soup = BeautifulSoup(res, 'html.parser') # 파이썬이 보기 편하도록 변경 what the 'htlml.parser?
picks = soup.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin.hide > div.realtime_part > ol > li > div > div:nth-of-type(1) > span.txt_issue > a')
# nth-child 를 nth-of-type으로 변경함, bs4에 child가 호환이 안됨.
# soup아 골라줭, 실시간검색어 동성제약 우클릭 -> 검사 -> 관리자모드 -> copy selector로 해당 내용 복사
# print(pick)

for p in picks:
    print(p.text) # .text는 여는 태그와 닫는 태그 사이의 글자만 가져옴 ex)a ~ /a
