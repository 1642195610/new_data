# import re
# import csv
# with open("18 姜泽毓.html","r",encoding="utf-8",newline="") as file:
#     file_h = file.read()
#     # print(file_h)
#     # p =r'target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)"'
#     # f_url = re.findall(p,file_h,re.S)
#     # print(f_url,len(f_url))
#
#     # p = r'z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt=""></a>'
#     # f_url = re.findall(p, file_h, re.S)
#     # print(f_url, len(f_url))
#
#     p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)")|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt=""></a>)'
#     f_url = re.findall(p, file_h, re.S)
#     z = []
#     for i in f_url:
#         url = {}
#         if i[0] != "":
#             url["图片地址"] = i[1]
#             url["作品名字"] = i[2]
#             z.append(url)
#         else:
#             url["图片地址"] = i[4]
#             url["作品名字"] = i[5]
#             z.append(url)
#     # print(z,len(z))
#     p = r'<p class="card-info-type" title="(.+?)">'
#     f_url = re.findall(p, file_h, re.S)
#     # print(f_url,len(f_url))
#     lx = []
#     for i in f_url:
#         url = {}
#         url["作品类型"] = i
#         lx.append(url)
#         # print(lx,len(lx))
#     p = r'<span class="statistics-view" title="共(.+?)人气">.+?</span>\s+<span class="statistics-comment" title="共(.+?)评论">.+?</span>\s+<span class="statistics-tuijian" title="共(.+?)推荐">.+?</span>'
#     f_url = re.findall(p, file_h, re.S)
#     # print(f_url)
#     zp = []
#     for i in f_url:
#         if i != "":
#             url = {}
#             url["人气数"] = i[0]
#             url["评论数"] = i[1]
#             url["点赞数"] = i[2]
#             zp.append(url)
#         else:
#             zp.append("无")
#     # print(zp,len(zp))
#     p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)")|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
#     f_url = re.findall(p, file_h, re.S)
#     # print(f_url,len(f_url))
#     # p = r'<div class="card-item">\s+<a href=".+?" title="(.+?)"'
#     f_url = re.findall(p, file_h, re.S)
#     # print(f_url,len(f_url))
#     zz = []
#     for i in f_url:
#         url = {}
#         url["作者"] = i[1]
#         zz.append(url)
#     # print(zz,len(zz))


import re
z = []
with open("18 姜泽毓.html","r",encoding="utf-8",newline="")as file:
    file = file.read()
p = r'<div class="card-box">(.+?)</div>\s+</div>'
file_m = re.findall(p,file,re.S)
for i in file_m:
    p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)")|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt=""></a>)'
    f_url = re.findall(p,i,re.S)[0]
    fz_url = f_url[1]
    if fz_url == "":
        fz_url = f_url[4]
    fz_t = f_url[2]
    if fz_t == "":
        fz_t = f_url[5]
    p = r'<p class="card-info-type" title="(.+?)">'
    f_l = re.findall(p,i,re.S)[0]
    p = r'<span class="statistics-view" title="共(.+?)人气">'
    f_p = re.findall(p,i,re.S)
    if len(f_p) > 0:
        f_pr = f_p[0]
    else:
        f_pr = '无'
    p = r'<span class="statistics-comment" title="共(.+?)评论">'
    f_pp= re.findall(p, i, re.S)
    if len(f_pp) > 0:
        fppl = f_pp[0]
    else:
        fppl = '无'
    p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
    f_pz = re.findall(p, i, re.S)
    if len(f_pz) > 0:
        f_pzz = f_pz[0]
    else:
        f_pzz = '无'
    p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)")|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
    fj_z = re.findall(p,i,re.S)[0]
    f_z = fj_z[1]
    if len(f_z) > 0:
        f_z = f_z
    else:
        f_z = fj_z[3]
    dic = {
        '图片地址': fz_url,
        '作品名称': fz_t,
        '作品类型': f_l,
        '人气': f_pr,
        '评论数': fppl,
        '点赞数': f_pzz,
        '作者': f_z
    }
    z.append(dic)
import csv
header = ['图片地址','作品名称','作品类型','人气','评论数','点赞数','作者']
with open('站酷.csv','w',encoding='utf-8-sig',newline='') as file:
    csv_file = csv.DictWriter(file,header)
    csv_file.writeheader()
    csv_file.writerows(z)










