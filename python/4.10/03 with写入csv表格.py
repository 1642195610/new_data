# import csv
# header = ["id","name","age","addr"]
# data = [
# 	{'id': 1001,'name': 'zs1','age': 28,'addr': '北京'},
# 	{'id': 1002,'name': 'zs2','age': 29,'addr': '东京'},
# 	{'id': 1003,'name': 'zs3','age': 20,'addr': '南京'},
# 	{'id': 1004,'name': 'zs4','age': 18,'addr': '西京'},
# 	{'id': 1005,'name': 'zs5','age': 38,'addr': '天津'}
# ]
# with open("数据.csv","w",encoding="utf-8-sig",newline="") as file:
# 	csv_file = csv.DictWriter(file,header)
# 	csv_file.writeheader()
# 	csv_file.writerows(data)

# import csv
# header = ["序号","姓名","年龄","地址"]
# i = header
# data = [
# 	{i[0]: 1001,i[1]: 'zs1',i[2]: 28,i[3]: '北京'},
# 	{i[0]: 1002,i[1]: 'zs2',i[2]: 29,i[3]: '东京'},
# 	{i[0]: 1003,i[1]: 'zs3',i[2]: 20,i[3]: '南京'},
# 	{i[0]: 1004,i[1]: 'zs4',i[2]: 18,i[3]: '西京'},
# 	{i[0]: 1005,i[1]: 'zs5',i[2]: 38,i[3]: '天津'}
# ]
# with open("数据.csv","w",encoding="utf-8-sig",newline="") as file:
# 	csv_file = csv.DictWriter(file,header)
# 	csv_file.writeheader()
# 	csv_file.writerows(data)