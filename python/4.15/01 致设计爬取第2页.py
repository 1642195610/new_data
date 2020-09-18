import urllib.request
import urllib.parse
url = "https://www.zhisheji.com/new_index_tj"
header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
dict = {
        "page":2
}
a = urllib.parse.urlencode(dict).encode()
request = urllib.request.Request(url,headers = header,data= a)
response = urllib.request.urlopen(request)
str = response.read().decode()
with open("2.html","w",encoding="utf-8-sig")as file:
        file = file.write(str)