import requests
s = requests.session()
url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
#
data = [{"mobilephone": "1512998327"+str(i),
         "pwd": "12345"+str(i),
         "regname": "呼呼呼呼或或或或或哈哈哈哈哈哈哈哈哈哈或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或或"+str(i)} for i in range(5)]
for i in data:
    r = s.post(url, data=i)
    print(r.text)
# url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# data = [{"mobilephone": '1512998347'+str(i),
#        "pwd": '12345'+str(i)} for i in range(5)]
# for i in data:
#     r = s.post(url, data=i)
#     print(r.text)






