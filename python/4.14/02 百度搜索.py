# import urllib.request
# import urllib.parse
# s = input("请输入要搜索的内容:")
# dic = {
#     "wd":s
# }
# a = urllib.parse.urlencode(dic)
# url = "https://www.baidu.com/s?" + a
# print(url)
# header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36","Cookie":"BIDUPSID=27F09807276F153FDBE95B243752091A; PSTM=1586513675; BAIDUID=27F09807276F153FF86A89F6483C9249:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; H_PS_PSSID=1461_31124_21120_31187_31218_30824_31164_31195; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_645EC=8dcbnm1au3LuWLCze1996gAmyHgszbPCAXM9Fkx4xChk%2Bbg%2FyqPSrHUdnhs; BDSVRTM=121; COOKIE_SESSION=74172_0_1_0_5_1_0_0_0_1_2_0_0_0_3_0_1586770642_0_1586844811%7C3%230_0_1586844811%7C1"}
# request = urllib.request.Request(url,headers=header)
# response = urllib.request.urlopen(request)
# str_data = response.read().decode()
# with open("%s.html"%(s),"w",encoding="utf-8-sig",newline="")as file:
#     file = file.write(str_data)


import urllib.request
import urllib.parse
s = input("请输入您要搜索的内容:")
dict = {
    "wd":s
}
a = urllib.parse.urlencode(dict)
url = "https://www.baidu.com/s?" + a
print(url)
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36","Cookie": "BIDUPSID=27F09807276F153FDBE95B243752091A; PSTM=1586513675; BAIDUID=27F09807276F153FF86A89F6483C9249:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; H_PS_PSSID=1461_31124_21120_31187_31218_30824_31164_31195; delPer=0; BD_CK_SAM=1; PSINO=1; COOKIE_SESSION=7_0_2_1_5_1_0_0_1_1_0_0_0_0_0_0_1586770642_0_1586844818%7C4%230_0_1586844818%7C1; H_PS_645EC=ad8fQ2RdC8K9gq1VG8QaCXfG81cnkrKI17fnc6KtoWT0VkZgjIxi08oC9Ik; BDSVRTM=120"}
request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request)
str_data = response.read().decode()
with open("%s.html"%(s),"w",encoding="utf-8-sig",newline="") as data:
    data_data = data.write(str_data)

