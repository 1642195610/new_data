import requests
from bc.bc import sj_User_Agent
def w():
    while True:
        try:
            url = "http://sc.chinaz.com/"
            header = sj_User_Agent()
            response = requests.get(url, headers=header)
            print(response)
            response.encoding = "utf-8"
            # with open("素材.html", "w", encoding="utf-8")as file:
            #     file = file.write(response.text)
            return response.text
            break
        except Exception as e:
            print("这个请求头不可用!!!")