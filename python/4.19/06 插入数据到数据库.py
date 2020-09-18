# import pymysql
#
# db = pymysql.connect('localhost','root','','python')
# # 创建游标对象,执行sql
# cursor = db.cursor()
# for i in range(0,100):
#     # sql语句
#     sql = "insert into people (姓名,性别,身高,职业,薪资) values ('zs','男','180','上单','1000')"
#     # 执行sql
#     cursor.execute(sql)
#
# # 提交动作
# db.commit()
# # 关闭数据库
# db.close()
#
#
# import pymysql
# db = pymysql.connect('localhost','root','','百度贴吧')
# cursor = db.cursor()
# sql = "insert into baidutieba (标题,主题作者,内容,内容图片地址,时间) values ('每天三','吃布丁的胖丁','有兴趣的私我哟','http://tiebapic.baidu.com/forum/w%3D580%3B/sign=1ff73b600830e924cfa49c397c336c06/730e0cf3d7ca7bcb12b9e147a9096b63f724a893.jpg,','4-19')"
# cursor.execute(sql)
# print("插入成功")
# db.commit()
# db.close()
