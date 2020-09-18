# import requests,json,h,re
# url = "http://www.iciba.com/index.php?"
# # s = input("请输入你要翻译的内容:")
# s = "好"
# params = {
#     "word": s ,
#     "callback" : "jQuery19007634390054761464_1587002428602",
#     "a" : "getWordMean",
#     "c" : "search",
#     "list" : "1,2,3,4,5,8,9,10,12,13,14,15,18,21,22,24,3003,3004,3005",
#     "_" : "1587002428607"
# }
# response = requests.get(url,headers = h.h, params= params)
# str = response.text
# # print(str)
# p = r'\((.+)\)'
# f = re.findall(p,str,re.S)[0]
# f = json.loads(f)
# x = f["baesInfo"]["symbols"][0]["parts"][0]["part"]
# xc = f["baesInfo"]["symbols"][0]["parts"][0]["means"]
# d = f["baesInfo"]["symbols"][1]["parts"][0]["part"]
# dc = f["baesInfo"]["symbols"][1]["parts"][0]["means"]
# m = f["baesInfo"]["symbols"][1]["parts"][1]["part"]
# mc = f["baesInfo"]["symbols"][1]["parts"][1]["means"]
# print(x,xc,d,dc,m,mc)
