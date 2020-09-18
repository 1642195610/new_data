import urllib.request
import urllib.parse
import csv
from lxml import etree
#请求
def get_html(url,dict = None):
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
    a = urllib.parse.urlencode(dict).encode()
    request = urllib.request.Request(url, headers=header, data=a)
    response = urllib.request.urlopen(request)
    str = response.read().decode()
    return str
if __name__ == "__main__":
    #数据持久化
    def s_html(mz,dic=None,**kwargs):
        if dic == None:
            header_csv = kwargs
            with open("%s" % (mz), "w", encoding="utf-8-sig", newline="") as data:
                data_csv = csv.DictWriter(data, header_csv)
                data_csv.writeheader()
        else:
            header_csv = kwargs
            with open("%s"%(mz), "a", encoding="utf-8-sig", newline="")as data:
                data_csv = csv.DictWriter(data,header_csv)
                data_csv.writerow(dic)
