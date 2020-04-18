import requests
# from dbtools import Db
"""
后台登录接口
""" 


# url = "http://49.235.251.162:2333/adminlogin"
# headers =  {"Content-Type": "application/json"}
# data = {"username":"admin", "password":"admin123" }
# res = requests.post(url=url,headers=headers,json=data)
# token = res.json()["data"]["token"]



# url = "http://49.235.251.162:2333/titleimglist?id=6"
# headers = {"Content-Type": "application/json","token":token}
# res = requests.get(url=url,headers=headers)
# print(res.text)



# url = "http://49.235.251.162:2333/adminlogin"
# headers =  {"Content-Type": "application/json"}
# data = {"username":"admin", "password":"admin123" }
# res = requests.post(url=url,headers=headers,json=data)
# res1 = res.json()
# msg = res1.get("msg")
# if msg == "登录成功！":
#     print("登录成功！测试通过！")
# else:
#     print("登录失败")


# db = Db("192.144.148.91","ljtest","123456","ljtestdb")

# url = "http://192.144.148.91:2333/get_title_img"
# res = requests.get(url)
# data = res.json().get("data")
# num = len(data)
# res = db.chaxun("select count(*) from t_title_img where status = 0;")[0][0]
# if num == res:
#     print("测试通过！")
# else:
#     print("测试失败")



url = "http://49.235.251.162:2333/adminlogin"

payload = "{\"username\":\"admin\",     \"password\":\"admin123\" }"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "cbc7a4c5-6551-4969-b446-f95a147973f8"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)