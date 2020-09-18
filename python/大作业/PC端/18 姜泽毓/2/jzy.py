#coding=utf-8
import requests
from bc.bc import sj_User_Agent,bccsv
from lxml import etree
import time
import csv
import random
def url():
    url = "http://music.taihe.com/"
    response = requests.get(url, headers=sj_User_Agent())
    return response.text
# print(url())
# with open("音乐.html", "w", encoding="utf-8")as file:
#     file = file.write(response.text)