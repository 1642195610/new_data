#coding=utf-8
import json
with open("json列表写入.json","r",encoding="utf-8")as file:
    connect = json.load(file)
    print(connect,type(connect))