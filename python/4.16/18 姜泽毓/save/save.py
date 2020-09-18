def save(file_name,content=None):
    import csv
    header_csv = ["图片地址", "作品名字", "作品类型", "人气数", "评论数", "点赞数", "作者图案", "作者","二级图片地址"]
    if content == None :
        with open(file_name, "w", encoding="utf-8-sig", newline="") as data:
            data = csv.DictWriter(data, header_csv)
            data.writeheader()
    else:
        with open(file_name, "a", encoding="utf-8-sig", newline="") as data:
            data = csv.DictWriter(data, header_csv)
            data.writerow(content)

def h():
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}
    return header

