import webbrowser

url = "https://www.google.com/search?&q=" # ? 뒤에는 옵션
q_list = ["bts", "IU", "black pink", "Winner"]

for q in q_list:
    webbrowser.open(url+q)