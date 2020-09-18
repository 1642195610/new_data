# import urllib.request
# import urllib.parse
# url = "https://www.zhisheji.com/new_index_tj"
# dic = {
#     "page" : "3"
# }
# header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
# a = urllib.parse.urlencode(dic).encode()
# request = urllib.request.Request(url,headers=header,data=a)
# response = urllib.request.urlopen(request)
# str_data = response.read().decode()
# with open("致设计.html","w",encoding="utf-8-sig",newline="")as data :
#     data_data = data.write(str_data)

import urllib.request
import urllib.parse
url = "https://www.zhisheji.com/new_index_tj"
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
dict = {
    "page":"5"
}
a = urllib.parse.urlencode(dict).encode()
request = urllib.request.Request(url,headers=header,data=a)
response = urllib.request.urlopen(request)
str_data = response.read().decode()
with open("致设计.html","w",encoding="utf-8-sig",newline="")as data:
    data_data = data.write(str_data)