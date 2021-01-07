import pytest
import requests


#注册功能的测试数据，列表中的测试数据可以是任意类型的
# @pytest.fixture(params=[{"data": {"mobilephone": 15129983478, "pwd": 123456},
#                          "expect":{"status": 0 ,"code": "20110","data": None, "msg": "手机号码已被注册"}},
#                         {"data": {"mobilephone": 1801235358, "pwd": 12345},
#                          "expect":{"status": 0, "code": "20108", "data": None, "msg": "密码长度必须为6~18"}}])
#
#
# def register_data1(request):#request是pytest中的关键字
#     return request.param#通过request.param返回每一组数据，固定写法
#
#
# #数据驱动测试
# #注册功能的测试脚本
# def test_regsiter_002(register_data1):
#     url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
#     print(f"注册功能，测试数据为：{register_data1['data']}")
#     r = requests.post(url, data=register_data1['data'])
#     print(r.text)
#     assert r.json()['msg'] == register_data1['expect']['msg']
#     assert r.json()['status'] == register_data1['expect']['status']
#     assert r.json()['code'] == register_data1['expect']['code']




print("===============================================分割线========================================")





#注册功能的测试数据，列表中的测试数据可以是任意类型的
@pytest.fixture(params=[{"mobilephone": 15129983478, "pwd": 123456, "msg": "手机号码已被注册"},
                        {"mobilephone": 1801235358, "pwd": 12345, "msg": "密码长度必须为6~18"},
                        {"mobilephone": 1801235358, "pwd": "", "msg": "密码不能为空"},
                        {"mobilephone": 123, "pwd": 123456, "msg": "手机号码格式不正确"}])

def register_data(request):#request是pytest中的关键字
    return request.param#通过request.param返回每一组数据，固定写法


# 数据驱动测试
# 注册功能的测试脚本
def test_regsiter_001(register_data):
    url = "http://192.168.150.222:8081/futureloan/mvc/api/member/register"
    print(f"注册功能，测试数据为：{register_data}")
    r = requests.post(url, data=register_data)
    print(r.text)
    assert r.json()['msg'] == register_data['msg']














