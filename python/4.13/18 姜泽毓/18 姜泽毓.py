# # 1.站酷: https://www.zcool.com.cn/
# # 把该网站的数据保存400条下来;格式和周五要求的格式一样
# import urllib.request
# url = "https://www.zcool.com.cn/"
# header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
# request = urllib.request.Request(url,headers= header)
# response = urllib.request.urlopen(request)
# str_data1 = response.read().decode()
# with open("站酷1.html","w",encoding="utf-8") as data1:
#     data1.write(str_data1)
# import re
# with open("站酷1.html","r",encoding="utf-8",newline="")as file1:
#     file1 = file1.read()
# p = r'<div class="card-box">(.+?)</div>\s+</div>'
# filem = re.findall(p,file1,re.S)
# z = []
# for i in filem:
#     p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
#     filet = re.findall(p,i,re.S)[0]
#     url = filet[1]
#     if url == "":
#         url = filet[4]
#     mz = filet[2]
#     if mz == "":
#         mz = filet[5]
#     p = r'<p class="card-info-type" title="(.+?)">'
#     lx = re.findall(p,i,re.S)[0]
#     p = r'<span class="statistics-view" title="共(.+?)人气">'
#     rqd = re.findall(p,i,re.S)
#     if len(rqd) > 0:
#         rq = rqd[0]
#     else:
#         rq = "无"
#     p = r'<span class="statistics-comment" title="共(.+?)评论">'
#     pld = re.findall(p,i,re.S)
#     if len(pld) > 0:
#         pl = pld[0]
#     else:
#         pl = "无"
#     p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
#     dzd = re.findall(p,i,re.S)
#     if len(dzd) > 0:
#         dz = dzd[0]
#     else:
#         dz = "无"
#     p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#     zzd = re.findall(p,i,re.S)[0]
#     zz = zzd[1]
#     if zz == "":
#         zz = zzd[3]
#     dic = {
#         '图片地址': url,
#         '作品名称': mz,
#         '作品类型': lx,
#         '人气': rq,
#         '评论数': pl,
#         '点赞数': dz,
#         '作者': zz
#     }
#     z.append(dic)
# import csv
# header = ['图片地址','作品名称','作品类型','人气','评论数','点赞数','作者']
# with open("站酷1.csv","w",encoding="utf-8-sig",newline="") as data:
#     csvd = csv.DictWriter(data,header)
#     csvd.writeheader()
#     csvd.writerows(z)
#
# import urllib.request
# url = "https://www.zcool.com.cn/?p=2#tab_anchor"
# header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
# request = urllib.request.Request(url,headers = header)
# response = urllib.request.urlopen(request)
# str_data = response.read().decode()
# with open("站酷2.html","w",encoding="utf-8")as data:
#     data = data.write(str_data)
# import re
# with open("站酷2.html","r",encoding="utf-8",newline="")as file:
#     file = file.read()
# p = r'<div class="card-box">(.+?)</div>\s+</div>'
# filem = re.findall(p,file,re.S)
# z = []
# for i in filem:
#     p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
#     filet = re.findall(p,i,re.S)[0]
#     url = filet[1]
#     if url == "":
#         url = filet[4]
#     mz = filet[2]
#     if mz == "":
#         mz = filet[5]
#     p = r'<p class="card-info-type" title="(.+?)">'
#     lx = re.findall(p,i,re.S)[0]
#     p = r'<span class="statistics-view" title="共(.+?)人气">'
#     rqd = re.findall(p,i,re.S)
#     if len(rqd) > 0:
#         rq = rqd[0]
#     else:
#         rq = "无"
#     p = r'<span class="statistics-comment" title="共(.+?)评论">'
#     pld = re.findall(p,i,re.S)
#     if len(pld) > 0:
#         pl = pld[0]
#     else:
#         pl = "无"
#     p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
#     dzd = re.findall(p,i,re.S)
#     if len(dzd) > 0:
#         dz = dzd[0]
#     else:
#         dz = "无"
#     p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#     zzd = re.findall(p,i,re.S)[0]
#     zz = zzd[1]
#     if zz == "":
#         zz = zzd[3]
#     dic = {
#         '图片地址': url,
#         '作品名称': mz,
#         '作品类型': lx,
#         '人气': rq,
#         '评论数': pl,
#         '点赞数': dz,
#         '作者': zz
#     }
#     z.append(dic)
# import csv
# header = ['图片地址','作品名称','作品类型','人气','评论数','点赞数','作者']
# with open("站酷2.csv","w",encoding="utf-8-sig",newline="") as data:
#     csvd = csv.DictWriter(data,header)
#     csvd.writeheader()
#     csvd.writerows(z)
#
# import urllib.request
# url = "https://www.zcool.com.cn/?p=4#tab_anchor"
# header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
# request = urllib.request.Request(url,headers= header)
# response = urllib.request.urlopen(request)
# str_data1 = response.read().decode()
# with open("站酷4.html","w",encoding="utf-8") as data1:
#     data1.write(str_data1)
# import re
# with open("站酷4.html","r",encoding="utf-8",newline="")as file1:
#     file1 = file1.read()
# p = r'<div class="card-box">(.+?)</div>\s+</div>'
# filem = re.findall(p,file1,re.S)
# z = []
# for i in filem:
#     p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
#     filet = re.findall(p,i,re.S)[0]
#     url = filet[1]
#     if url == "":
#         url = filet[4]
#     mz = filet[2]
#     if mz == "":
#         mz = filet[5]
#     p = r'<p class="card-info-type" title="(.+?)">'
#     lx = re.findall(p,i,re.S)[0]
#     p = r'<span class="statistics-view" title="共(.+?)人气">'
#     rqd = re.findall(p,i,re.S)
#     if len(rqd) > 0:
#         rq = rqd[0]
#     else:
#         rq = "无"
#     p = r'<span class="statistics-comment" title="共(.+?)评论">'
#     pld = re.findall(p,i,re.S)
#     if len(pld) > 0:
#         pl = pld[0]
#     else:
#         pl = "无"
#     p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
#     dzd = re.findall(p,i,re.S)
#     if len(dzd) > 0:
#         dz = dzd[0]
#     else:
#         dz = "无"
#     p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#     zzd = re.findall(p,i,re.S)[0]
#     zz = zzd[1]
#     if zz == "":
#         zz = zzd[3]
#     dic = {
#         '图片地址': url,
#         '作品名称': mz,
#         '作品类型': lx,
#         '人气': rq,
#         '评论数': pl,
#         '点赞数': dz,
#         '作者': zz
#     }
#     z.append(dic)
# import csv
# header = ['图片地址','作品名称','作品类型','人气','评论数','点赞数','作者']
# with open("站酷4.csv","w",encoding="utf-8-sig",newline="") as data:
#     csvd = csv.DictWriter(data,header)
#     csvd.writeheader()
#     csvd.writerows(z)
#
# import urllib.request
# url = "https://www.zcool.com.cn/?p=5#tab_anchor"
# header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
# request = urllib.request.Request(url,headers= header)
# response = urllib.request.urlopen(request)
# str_data1 = response.read().decode()
# with open("站酷5.html","w",encoding="utf-8") as data1:
#     data1.write(str_data1)
# import re
# with open("站酷5.html","r",encoding="utf-8",newline="")as file1:
#     file1 = file1.read()
# p = r'<div class="card-box">(.+?)</div>\s+</div>'
# filem = re.findall(p,file1,re.S)
# z = []
# for i in filem:
#     p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
#     filet = re.findall(p,i,re.S)[0]
#     url = filet[1]
#     if url == "":
#         url = filet[4]
#     mz = filet[2]
#     if mz == "":
#         mz = filet[5]
#     p = r'<p class="card-info-type" title="(.+?)">'
#     lx = re.findall(p,i,re.S)[0]
#     p = r'<span class="statistics-view" title="共(.+?)人气">'
#     rqd = re.findall(p,i,re.S)
#     if len(rqd) > 0:
#         rq = rqd[0]
#     else:
#         rq = "无"
#     p = r'<span class="statistics-comment" title="共(.+?)评论">'
#     pld = re.findall(p,i,re.S)
#     if len(pld) > 0:
#         pl = pld[0]
#     else:
#         pl = "无"
#     p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
#     dzd = re.findall(p,i,re.S)
#     if len(dzd) > 0:
#         dz = dzd[0]
#     else:
#         dz = "无"
#     p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#     zzd = re.findall(p,i,re.S)[0]
#     zz = zzd[1]
#     if zz == "":
#         zz = zzd[3]
#     dic = {
#         '图片地址': url,
#         '作品名称': mz,
#         '作品类型': lx,
#         '人气': rq,
#         '评论数': pl,
#         '点赞数': dz,
#         '作者': zz
#     }
#     z.append(dic)
# import csv
# header = ['图片地址','作品名称','作品类型','人气','评论数','点赞数','作者']
# with open("站酷5.csv","w",encoding="utf-8-sig",newline="") as data:
#     csvd = csv.DictWriter(data,header)
#     csvd.writeheader()
#     csvd.writerows(z)
#
# import urllib.request
# url = "https://www.zcool.com.cn/?p=6#tab_anchor"
# header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
# request = urllib.request.Request(url,headers= header)
# response = urllib.request.urlopen(request)
# str_data1 = response.read().decode()
# with open("站酷6.html","w",encoding="utf-8") as data1:
#     data1.write(str_data1)
# import re
# with open("站酷6.html","r",encoding="utf-8",newline="")as file1:
#     file1 = file1.read()
# p = r'<div class="card-box">(.+?)</div>\s+</div>'
# filem = re.findall(p,file1,re.S)
# z = []
# for i in filem:
#     p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
#     filet = re.findall(p,i,re.S)[0]
#     url = filet[1]
#     if url == "":
#         url = filet[4]
#     mz = filet[2]
#     if mz == "":
#         mz = filet[5]
#     p = r'<p class="card-info-type" title="(.+?)">'
#     lx = re.findall(p,i,re.S)[0]
#     p = r'<span class="statistics-view" title="共(.+?)人气">'
#     rqd = re.findall(p,i,re.S)
#     if len(rqd) > 0:
#         rq = rqd[0]
#     else:
#         rq = "无"
#     p = r'<span class="statistics-comment" title="共(.+?)评论">'
#     pld = re.findall(p,i,re.S)
#     if len(pld) > 0:
#         pl = pld[0]
#     else:
#         pl = "无"
#     p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
#     dzd = re.findall(p,i,re.S)
#     if len(dzd) > 0:
#         dz = dzd[0]
#     else:
#         dz = "无"
#     p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#     zzd = re.findall(p,i,re.S)[0]
#     zz = zzd[1]
#     if zz == "":
#         zz = zzd[3]
#     dic = {
#         '图片地址': url,
#         '作品名称': mz,
#         '作品类型': lx,
#         '人气': rq,
#         '评论数': pl,
#         '点赞数': dz,
#         '作者': zz
#     }
#     z.append(dic)
# import csv
# header = ['图片地址','作品名称','作品类型','人气','评论数','点赞数','作者']
# with open("站酷6.csv","w",encoding="utf-8-sig",newline="") as data:
#     csvd = csv.DictWriter(data,header)
#     csvd.writeheader()
#     csvd.writerows(z)
#
# import urllib.request
# url = "https://www.zcool.com.cn/?p=7#tab_anchor"
# header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
# request = urllib.request.Request(url,headers= header)
# response = urllib.request.urlopen(request)
# str_data1 = response.read().decode()
# with open("站酷7.html","w",encoding="utf-8") as data1:
#     data1.write(str_data1)
# import re
# with open("站酷7.html","r",encoding="utf-8",newline="")as file1:
#     file1 = file1.read()
# p = r'<div class="card-box">(.+?)</div>\s+</div>'
# filem = re.findall(p,file1,re.S)
# z = []
# for i in filem:
#     p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
#     filet = re.findall(p,i,re.S)[0]
#     url = filet[1]
#     if url == "":
#         url = filet[4]
#     mz = filet[2]
#     if mz == "":
#         mz = filet[5]
#     p = r'<p class="card-info-type" title="(.+?)">'
#     lx = re.findall(p,i,re.S)[0]
#     p = r'<span class="statistics-view" title="共(.+?)人气">'
#     rqd = re.findall(p,i,re.S)
#     if len(rqd) > 0:
#         rq = rqd[0]
#     else:
#         rq = "无"
#     p = r'<span class="statistics-comment" title="共(.+?)评论">'
#     pld = re.findall(p,i,re.S)
#     if len(pld) > 0:
#         pl = pld[0]
#     else:
#         pl = "无"
#     p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
#     dzd = re.findall(p,i,re.S)
#     if len(dzd) > 0:
#         dz = dzd[0]
#     else:
#         dz = "无"
#     p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#     zzd = re.findall(p,i,re.S)[0]
#     zz = zzd[1]
#     if zz == "":
#         zz = zzd[3]
#     dic = {
#         '图片地址': url,
#         '作品名称': mz,
#         '作品类型': lx,
#         '人气': rq,
#         '评论数': pl,
#         '点赞数': dz,
#         '作者': zz
#     }
#     z.append(dic)
# import csv
# header = ['图片地址','作品名称','作品类型','人气','评论数','点赞数','作者']
# with open("站酷7.csv","w",encoding="utf-8-sig",newline="") as data:
#     csvd = csv.DictWriter(data,header)
#     csvd.writeheader()
#     csvd.writerows(z)
#
# import urllib.request
# url = "https://www.zcool.com.cn/?p=8#tab_anchor"
# header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
# request = urllib.request.Request(url,headers= header)
# response = urllib.request.urlopen(request)
# str_data1 = response.read().decode()
# with open("站酷8.html","w",encoding="utf-8") as data1:
#     data1.write(str_data1)
# import re
# with open("站酷8.html","r",encoding="utf-8",newline="")as file1:
#     file1 = file1.read()
# p = r'<div class="card-box">(.+?)</div>\s+</div>'
# filem = re.findall(p,file1,re.S)
# z = []
# for i in filem:
#     p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
#     filet = re.findall(p,i,re.S)[0]
#     url = filet[1]
#     if url == "":
#         url = filet[4]
#     mz = filet[2]
#     if mz == "":
#         mz = filet[5]
#     p = r'<p class="card-info-type" title="(.+?)">'
#     lx = re.findall(p,i,re.S)[0]
#     p = r'<span class="statistics-view" title="共(.+?)人气">'
#     rqd = re.findall(p,i,re.S)
#     if len(rqd) > 0:
#         rq = rqd[0]
#     else:
#         rq = "无"
#     p = r'<span class="statistics-comment" title="共(.+?)评论">'
#     pld = re.findall(p,i,re.S)
#     if len(pld) > 0:
#         pl = pld[0]
#     else:
#         pl = "无"
#     p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
#     dzd = re.findall(p,i,re.S)
#     if len(dzd) > 0:
#         dz = dzd[0]
#     else:
#         dz = "无"
#     p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#     zzd = re.findall(p,i,re.S)[0]
#     zz = zzd[1]
#     if zz == "":
#         zz = zzd[3]
#     dic = {
#         '图片地址': url,
#         '作品名称': mz,
#         '作品类型': lx,
#         '人气': rq,
#         '评论数': pl,
#         '点赞数': dz,
#         '作者': zz
#     }
#     z.append(dic)
# import csv
# header = ['图片地址','作品名称','作品类型','人气','评论数','点赞数','作者']
# with open("站酷8.csv","w",encoding="utf-8-sig",newline="") as data:
#     csvd = csv.DictWriter(data,header)
#     csvd.writeheader()
#     csvd.writerows(z)
#
# import urllib.request
# url = "https://www.zcool.com.cn/?p=9#tab_anchor"
# header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
# request = urllib.request.Request(url,headers= header)
# response = urllib.request.urlopen(request)
# str_data1 = response.read().decode()
# with open("站酷9.html","w",encoding="utf-8") as data1:
#     data1.write(str_data1)
# import re
# with open("站酷9.html","r",encoding="utf-8",newline="")as file1:
#     file1 = file1.read()
# p = r'<div class="card-box">(.+?)</div>\s+</div>'
# filem = re.findall(p,file1,re.S)
# z = []
# for i in filem:
#     p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
#     filet = re.findall(p,i,re.S)[0]
#     url = filet[1]
#     if url == "":
#         url = filet[4]
#     mz = filet[2]
#     if mz == "":
#         mz = filet[5]
#     p = r'<p class="card-info-type" title="(.+?)">'
#     lx = re.findall(p,i,re.S)[0]
#     p = r'<span class="statistics-view" title="共(.+?)人气">'
#     rqd = re.findall(p,i,re.S)
#     if len(rqd) > 0:
#         rq = rqd[0]
#     else:
#         rq = "无"
#     p = r'<span class="statistics-comment" title="共(.+?)评论">'
#     pld = re.findall(p,i,re.S)
#     if len(pld) > 0:
#         pl = pld[0]
#     else:
#         pl = "无"
#     p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
#     dzd = re.findall(p,i,re.S)
#     if len(dzd) > 0:
#         dz = dzd[0]
#     else:
#         dz = "无"
#     p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#     zzd = re.findall(p,i,re.S)[0]
#     zz = zzd[1]
#     if zz == "":
#         zz = zzd[3]
#     dic = {
#         '图片地址': url,
#         '作品名称': mz,
#         '作品类型': lx,
#         '人气': rq,
#         '评论数': pl,
#         '点赞数': dz,
#         '作者': zz
#     }
#     z.append(dic)
# import csv
# header = ['图片地址','作品名称','作品类型','人气','评论数','点赞数','作者']
# with open("站酷9.csv","w",encoding="utf-8-sig",newline="") as data:
#     csvd = csv.DictWriter(data,header)
#     csvd.writeheader()
#     csvd.writerows(z)
#
# import urllib.request
# url = "https://www.zcool.com.cn/?p=10#tab_anchor"
# header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
# request = urllib.request.Request(url,headers= header)
# response = urllib.request.urlopen(request)
# str_data1 = response.read().decode()
# with open("站酷10.html","w",encoding="utf-8") as data1:
#     data1.write(str_data1)
# import re
# with open("站酷10.html","r",encoding="utf-8",newline="")as file1:
#     file1 = file1.read()
# p = r'<div class="card-box">(.+?)</div>\s+</div>'
# filem = re.findall(p,file1,re.S)
# z = []
# for i in filem:
#     p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
#     filet = re.findall(p,i,re.S)[0]
#     url = filet[1]
#     if url == "":
#         url = filet[4]
#     mz = filet[2]
#     if mz == "":
#         mz = filet[5]
#     p = r'<p class="card-info-type" title="(.+?)">'
#     lx = re.findall(p,i,re.S)[0]
#     p = r'<span class="statistics-view" title="共(.+?)人气">'
#     rqd = re.findall(p,i,re.S)
#     if len(rqd) > 0:
#         rq = rqd[0]
#     else:
#         rq = "无"
#     p = r'<span class="statistics-comment" title="共(.+?)评论">'
#     pld = re.findall(p,i,re.S)
#     if len(pld) > 0:
#         pl = pld[0]
#     else:
#         pl = "无"
#     p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
#     dzd = re.findall(p,i,re.S)
#     if len(dzd) > 0:
#         dz = dzd[0]
#     else:
#         dz = "无"
#     p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#     zzd = re.findall(p,i,re.S)[0]
#     zz = zzd[1]
#     if zz == "":
#         zz = zzd[3]
#     dic = {
#         '图片地址': url,
#         '作品名称': mz,
#         '作品类型': lx,
#         '人气': rq,
#         '评论数': pl,
#         '点赞数': dz,
#         '作者': zz
#     }
#     z.append(dic)
# import csv
# header = ['图片地址','作品名称','作品类型','人气','评论数','点赞数','作者']
# with open("站酷10.csv","w",encoding="utf-8-sig",newline="") as data:
#     csvd = csv.DictWriter(data,header)
#     csvd.writeheader()
#     csvd.writerows(z)
#

print("进阶版")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
#
# import re
# import urllib.request
# import csv
# header_csv = ["图片地址","作品名字","作品类型","人气数","点赞数","评论数","作者图片","作者"]
# with open("站酷终结版.csv","w",encoding="utf-8-sig",newline="") as file:
#     file_csv = csv.DictWriter(file,header_csv)
#     file_csv.writeheader()
# t = 0
# for a in range(1,11):
#     url = "https://www.zcool.com.cn/?p=%s#tab_anchor"%(a)
#     header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
#     request = urllib.request.Request(url,headers= header)
#     response = urllib.request.urlopen(request)
#     str_data1 = response.read().decode()
#     with open("站酷.html","w",encoding="utf-8") as data1:
#         data1.write(str_data1)
#     import re
#     with open("站酷.html","r",encoding="utf-8",newline="")as file1:
#         file1 = file1.read()
#     p = r'<div class="card-box">(.+?)</div>\s+</div>'
#     filem = re.findall(p,file1,re.S)
#     for i in filem:
#         t += 1
#         p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
#         filet = re.findall(p,i,re.S)[0]
#         url = filet[1]
#         if url == "":
#             url = filet[4]
#         mz = filet[2]
#         if mz == "":
#             mz = filet[5]
#         p = r'<p class="card-info-type" title="(.+?)">'
#         lx = re.findall(p,i,re.S)[0]
#         p = r'<span class="statistics-view" title="共(.+?)人气">'
#         rqd = re.findall(p,i,re.S)
#         if len(rqd) > 0:
#             rq = rqd[0]
#         else:
#             rq = "无"
#         p = r'<span class="statistics-comment" title="共(.+?)评论">'
#         pld = re.findall(p,i,re.S)
#         if len(pld) > 0:
#             pl = pld[0]
#         else:
#             pl = "无"
#         p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
#         dzd = re.findall(p,i,re.S)
#         if len(dzd) > 0:
#             dz = dzd[0]
#         else:
#             dz = "无"
#         p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#         zzd = re.findall(p,i,re.S)[0]
#         zz = zzd[1]
#         if zz == "":
#             zz = zzd[3]
#         dic = {
#             '图片地址': url,
#             '作品名字': mz,
#             '作品类型': lx,
#             '人气数': rq,
#             '评论数': pl,
#             '点赞数': dz,
#             '作者': zz
#         }
#         with open("站酷终结版.csv","a",encoding="utf-8-sig",newline="")as file :
#             file_csv = csv.DictWriter(file,header_csv)
#             file_csv.writerow(dic)
#             print("爬取%s条"%(t))
#     print("第%s页结束"%(a))

#
#
#
#
#
#
# # 2.致设计: https://www.zhisheji.com/
# # 保存该网页的第一页的数据,存入到csv
import urllib.request
url = "https://www.zhisheji.com/"
header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
request = urllib.request.Request(url,headers=header)
response = urllib.request.urlopen(request)
str_data = response.read().decode()
with open("致设计.html","w",encoding="utf-8",newline="")as data :
    data = data.write(str_data)
with open("致设计.html","r",encoding="utf-8")as file:
    file = file.read()
import re
p = r'<li id=".+?">(.+?)</div>\s+</li>'
fm = re.findall(p,file,re.S)
z = []
for i in fm:
    p = r'<span class="img-box"><img class="previews" mysrc="" src="(.+?)" alt="(.+?)" width="290" height="180" alt="fads">'
    tp = re.findall(p,i,re.S)[0]
    url = tp[0]
    mz = tp[1]
    p = r'<div class="desc">(.+?)</div>'
    lx = re.findall(p, i, re.S)[0]
    p = r'<div class="info">\s+<em><span class="icon-view"></span>(.+?)</em>'
    rqs = re.findall(p,i,re.S)[0]
    p =r'<em><span class="icon-praise"></span>(.+?)</em>'
    dzs = re.findall(p,i,re.S)[0]
    p = r'<em><span class="icon-comment"></span>(.+?)</em>'
    pls = re.findall(p,i,re.S)[0]
    p =r''
    p = r'<div class="sjs-name">\s+<a target="_blank" href=".+?" title="(.+?)">\s+<img class=".+?" mysrc="" src="(.+?)"'
    tp = re.findall(p,i,re.S)[0]
    ta = tp[1]
    zz = tp[0]
    dic = {
        "图片地址":url,
        "作品名字":mz,
        "作品类型":lx,
        "人气数":rqs,
        "点赞数":dzs,
        "评论数":pls,
        "作者图片":ta,
        "作者":zz
    }
    z.append(dic)
import csv
header = ["图片地址","作品名字","作品类型","人气数","点赞数","评论数","作者图片","作者"]
with open("致设计.csv","w",encoding="utf-8-sig",newline="")as data:
    data_csv = csv.DictWriter(data,header)
    data_csv.writeheader()
    data_csv.writerows(z)


