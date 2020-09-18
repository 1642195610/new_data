# shuru = input("请输入7个号码:")
shuru = "1,1,35,4,5,6,7"
shuru = shuru.split(",")
print(shuru)
first = shuru[:6]
print(first)
red_l =[]
while len(red_l) != 6:
    count = 0
    for i in first:
        if int(i) >= 1 and int(i) <= 33:
            if i not in red_l:
                red_l.append(i)
            else:
                count += 1
        else:
            count += 1
    if count > 0:
        print("红球中有%s个超出范围,或者重复的号码!!!" % (count))
        a = input("请输入1-33的号码:")
        first.append(a)
    print("红球号码为:", ",".join(red_l))

