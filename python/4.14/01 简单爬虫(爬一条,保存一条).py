import re
import urllib.request
import csv
header_csv = ["图片地址","作品名字","作品类型","人气数","点赞数","评论数","作者图片","作者"]
with open("站酷终结版.csv","w",encoding="utf-8-sig",newline="") as file:
    file_csv = csv.DictWriter(file,header_csv)
    file_csv.writeheader()
t = 0
for a in range(1,11):
    url = "https://www.zcool.com.cn/?p=%s#tab_anchor"%(a)
    header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
    request = urllib.request.Request(url,headers= header)
    response = urllib.request.urlopen(request)
    str_data1 = response.read().decode()
    with open("站酷.html","w",encoding="utf-8") as data1:
        data1.write(str_data1)
    import re
    with open("站酷.html","r",encoding="utf-8",newline="")as file1:
        file1 = file1.read()
    p = r'<div class="card-box">(.+?)</div>\s+</div>'
    filem = re.findall(p,file1,re.S)
    for i in filem:
        t += 1
        p = r'(target="_blank" z-st="home_main_card_cover">\s+<img src="(.+?)"\s+srcset=".+?"\s+title="(.+?)" alt="">)|(z-st="content_ad_cover"><img src="(.+?)" title="(.+?)" alt="">)'
        filet = re.findall(p,i,re.S)[0]
        url = filet[1]
        if url == "":
            url = filet[4]
        mz = filet[2]
        if mz == "":
            mz = filet[5]
        p = r'<p class="card-info-type" title="(.+?)">'
        lx = re.findall(p,i,re.S)[0]
        p = r'<span class="statistics-view" title="共(.+?)人气">'
        rqd = re.findall(p,i,re.S)
        if len(rqd) > 0:
            rq = rqd[0]
        else:
            rq = "无"
        p = r'<span class="statistics-comment" title="共(.+?)评论">'
        pld = re.findall(p,i,re.S)
        if len(pld) > 0:
            pl = pld[0]
        else:
            pl = "无"
        p = r'<span class="statistics-tuijian" title="共(.+?)推荐">'
        dzd = re.findall(p,i,re.S)
        if len(dzd) > 0:
            dz = dzd[0]
        else:
            dz = "无"
        p = r'(<div class="card-item">\s+<span class=".+?">\s+<a href=".+?" title="(.+?)" target="_blank" z-st="home_main_card_user">)|(<div class="card-item">\s+<a href=".+?" title="(.+?)")'
        zzd = re.findall(p,i,re.S)[0]
        zz = zzd[1]
        if zz == "":
            zz = zzd[3]
        dic = {
            '图片地址': url,
            '作品名字': mz,
            '作品类型': lx,
            '人气数': rq,
            '评论数': pl,
            '点赞数': dz,
            '作者': zz
        }
        with open("站酷终结版.csv","a",encoding="utf-8-sig",newline="")as file :
            file_csv = csv.DictWriter(file,header_csv)
            file_csv.writerow(dic)
            print("爬取%s条"%(t))
    print("第%s页结束"%(a))
