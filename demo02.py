# a = 1
# b = 2
# if a > b:
#     print("a比b大")
# else:
#     print("b更大")

# grade = int(input("请输入分数："))

# if grade >= 90:
#     print("优秀")
# elif grade >= 80 and grade < 90:
#     print("良好")
# elif grade >= 60 and grade < 80:
#     print("及格")
# else:
#     print("不及格")

# a = 1
# while a < 10:
#     print("hhh")
#     a = a + 1

# a = input("请输入姓名:")
# b = input("请输入成绩")
# if b > 60
# d = {"name":a,"grde":b}

# highchengji = {}
# lowchengji = {}
# studentlist = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# a = 0
# while a < len(studentlist):
#     chengji = int(input("请输入"+studentlist[a]+"的成绩："))
#     if chengji >= 60:
#         highchengji[studentlist[a]] = chengji 
#     else:
#         lowchengji[studentlist[a]] = chengji
#     a = a + 1
# print("大于60的: ",highchengji)
# print("小于60的: ",lowchengji)


# a = ["张三","李四","王麻子","浪晋","流云","希希","小梁","二狗","陈平安","朱珠","亚索"]
# for i in a:


# for i in range(10):
#     if i == 3:
#         continue
#     print("哈哈哈")

# def jianfa(a,b):
#     if type(a) is int and type(b) is int:
#         print(a-b)
#     else:
#         print("输入的数据类型不正确")

# jianfa(55,6)

# try:
#     print(2+"哈哈")
# except:
#     print("上面的代码写错了")


# username = input("请输入用户名")
# password = input("请输入密码")

# def judgeway(username,password):
#     """
#     判断用户输入的账号密码是否符合规范
#     """
#     if len(username) <=8 and len(username) >=5:
#         if username[0] in "qwertyuiopasdfghjklzxcvbnm":
#             if len(password) <=12 and len(password) >=6:
#                 print("ok")
#             else:
#                 print("密码必须6到12位")
#         else:
#             print("用户名必须以小写字母开头")
#     else:
#         print("用户名长度需要5到8位")
# judgeway(username,password)


# username = input("请输入用户名")
# password = input("请输入密码")

# def judgeway(username,password):
#     """
#     判断用户输入的账号密码是否符合规范
#     """
#     if len(username) <=8 and len(username) >=5:
#         if username[0] in "qwertyuiopasdfghjklzxcvbnm":
#             if len(password) <=12 and len(password) >=6:
#                 print("ok")
#             else:
#                 print("密码必须6到12位")
#         else:
#             print("用户名必须以小写字母开头")
#             if len(password) <=12 and len(password) >=6:
#                 print("ok")
#             else:
#                 print("密码必须6到12位")
#     else:
#         print("用户名长度需要5到8位")
#         if username[0] in "qwertyuiopasdfghjklzxcvbnm":
#             if len(password) <=12 and len(password) >=6:
#                 print("ok")
#             else:
#                 print("密码必须6到12位")
#         else:
#             print("用户名必须以小写字母开头")
#             if len(password) <=12 and len(password) >=6:
#                     print("ok")
#             else:
#                 print("密码必须6到12位")
# judgeway(username,password)


# class Car():
#     def __init__(self,pinpai,yanse,neishi,jilun):
#         self.pinpai = pinpai
#         self.yanse = yanse
#         self.neishi = neishi
#         self.jilun = jilun

#     def bianxing(self):
#         print("车子变身喜羊羊！")

#     def fly(self):
#         print("车子开始起飞！")
        

# zhangsan = Car("奥拓","黑色","豪华","四轮车")
# zhangsan.bianxing()


# a = [1,2,3,4]
# x = [10,20,30]
# # b = a.pop(2)
# # print(b)
# # print(a)
# # a.clear()
# a.extend(x)
# a.remove(1)
# print(a)