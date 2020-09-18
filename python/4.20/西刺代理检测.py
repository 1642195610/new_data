import requests
from save.save import h
from lxml import etree
url = "https://www.xicidaili.com/nn/3"
response = requests.get(url, headers=h())
with open("西刺代理检测.html" ,"w", encoding="utf-8")as file:
    file = file.write(response.text)
response = response.text
response = etree.HTML(response)
m = response.xpath('//table[@id="ip_list"]/tr')
list = []
for ip in m[1:] :
    ip = ip.xpath('./td/text()')
    ipm = ip[0]
    dkh = ip[1]
    xy = ip[5].lower()
    if xy == "https":
        dict = {}
        dict[xy] = ipm + ":" + dkh
        list.append(dict)
print(list)
