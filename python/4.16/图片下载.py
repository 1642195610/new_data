import requests
from h import h
url = "https://img.zcool.cn/community/0156975e8edc81a80120a895d8c3ba.jpg@260w_195h_1c_1e_1o_100sh.jpg"
response = requests.get(url,headers = h)
with open("1.jpg","wb") as file:
    file = file.write(response.content)