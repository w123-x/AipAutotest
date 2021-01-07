'''
使用requests 做接口测试
'''
# 导入包
import requests

# 发送一个get请求
from requests import head

r = requests.get("http://www.baidu.com")
print(r.text)  # 文本格式的返回值
print(r.status_code)  # 相应状态码
print(r.raw)  # 无格式的相应
# 接口测试，构造不同的参数，发送请求，对相应的结果做断言
# 获取用户列表
# http://jy001:8081：测试环境
# futureloan/mvc/api/member/list接口地址
# url = "http://192.168.150.222:8081/futureloan/mvc/api/member/list"
# r = requests.get(url)
# # print(r.text)
# # 检查ststus_code，响应码是不是200
# assert r.status_code == 200
# # 响应体式json格式的，取里边的code，检查是不是10001
# assert r.json()['code'] == '10001'
#
# # f发送的请求带参数
# # 注册用户
# # 方式一：拼接到url后面
# url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=18012345678&pwd=123456"
# r = requests.get(url)
# print(r.text)
# assert r.status_code == 200
# assert r.json()['code'] == '20110'  # 已被注册的返回码
# assert r.json()['msg'] == "手机号码已被注册"
# assert r.json()['status'] == 0  # 异常
#
# url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=180123458&pwd=123456"
# r = requests.get(url)
# print(r.text)
# assert r.json()['msg'] == "手机号码格式不正确"
#
# url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register?mobilephone=18012345678&pwd="
# r = requests.get(url)
# print(r.text)
# assert r.json()['msg'] == "密码不能为空"
#
# # 方式二：使用params传参
# #params传参时，放在url里边
# #data和json传参时，放在方法体里边传参
#
# url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
# data = {"mobilephone": 18012345678, "pwd": "12345", "rename": "requests"}
# r = requests.get(url, data)
# print(r.text)
# assert r.json()['msg'] == "密码长度必须为6~18"
#
# # 练习：淘宝查询手机号码归属地的接口
# # 参数tel：手机号码
# url = "https://tcc.taobao.com/cc/json/mobile_tel_segment.htm"
# data = {"tel": 13227020783}
# r = requests.get(url, data)
# print(r.text)
# assert "陕西联通" in r.text
#
#发送请求，设置请求头
#测试的网站，不管发送什么请求，服务器把请求的内容封装成json格式的返回
#/get get方法。/post post方法
head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
url = "http://www.httpbin.org/get"
r = requests.get(url,headers=head)
# r = requests.get(url)
print(r.text)

