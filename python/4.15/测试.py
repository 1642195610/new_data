# import requests
# import header
# url = "https://www.baidu.com"
# str = input("请输入:")
# dic = {
#     "wd":str
# }
# response = requests.get(url,headers= header.header,param=dic)
# print(response.text)

import requests
import header
url = "https://fanyi.qq.com/api/translate"
s = input("请输入要翻译的内容:")
dic = {
"sourceText" : s
}
response = requests.post(url,headers=header.header,data= dic)
response = response.json()
print(response["translate"]['records'][0]['targetText'])
