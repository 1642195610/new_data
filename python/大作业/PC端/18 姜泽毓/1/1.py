import requests
from bc.bc import sj_User_Agent
def wai():
    while True:
        try:
            url = "https://erds.58.com/zufang/"
            response = requests.get(url, headers=sj_User_Agent())
            print(response)
            with open("租房.html", "w", encoding="utf-8")as file:
                return response.text
            break
        except Exception as e:
            print("这个请求头不可用!!!%s" % (e))
