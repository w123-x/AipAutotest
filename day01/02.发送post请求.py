'''post请求'''
import requests
#发送post请求，表单类型的参数，使用data传参
#登录接口
# url = "http://192.168.150.222:8081/futureloan/mvc/api/member/login"
# cs = {"mobilephone": "15129983478", "pwd": "123456"}
# r = requests.post(url, data=cs)
# print(r.text)
# assert r.json()['msg'] == "登录成功"

#发送post请求。json类型的参数，使用json传参
url = "http://www.httpbin.org/post"
cs = {"username": "123123123", "pwd": "123123123", "email": "1234567@qq.com"}
r = requests.post(url, json=cs)
print(r.text)
assert r.json()['json']['username'] == "123123123"


#发送post请求，带请求头
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36 "
}
r=requests.post(url,json=cs,headers=head)
print(r.text)

