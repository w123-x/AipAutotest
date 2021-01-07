'''
注册的测试脚本
'''
#注册失败的测试脚本
import pytest
from zonghe.baw import Member, Db
from zonghe.caw import DataRead, Asserts


#pytest 数据驱动的方式
#从yaml中读取测试数据
# @pytest.fixture(params=DataRead.read_yaml(r"data_case\register_fail.yaml"))
# def fail_data(request):
#     return request.param
#
# def test_register_fail(url, baserequests, fail_data):
#     #下发注册的请求
#     r = Member.register(url, baserequests, fail_data['data'])
#     #断言响应的结果
#     print(r.text)
#     assert r.json()['code'] == fail_data['except']['code']
#     assert r.json()['msg'] == fail_data['except']['msg']
#     assert r.json()['status'] == fail_data['except']['status']

#把注册成功的数据写在register_pass.yaml
#注册成功的脚本，下发请求，断言响应的结果
#注册成功的测试脚本
# @pytest.fixture(params=DataRead.read_yaml(r"data_case\register_pass.yaml"))
# def pass_data(request):
#     return request.param

# def test_register_pass(url, baserequests, pass_data, db):
#     mobilephone = pass_data['data']['mobilephone']
#     print(mobilephone)
    #下发注册请求
    # r = Member.register(url, baserequests, pass_data['data'])
    # #断言响应的结果
    # print(r.text)
    # assert r.json()['code'] == pass_data['expect']['code']
    # assert r.json()['msg'] == pass_data['expect']['msg']
    # assert r.json()['status'] == pass_data['expect']['status']
    #调用查询接口，在查询的结果中能找到本次注册的手机号
    # r = Member.list(url, baserequests)
    # print(r.text)
    # assert str(mobilephone) in r.text
    # print(r.text)
    # #清理环境：删除注册的用户
    # Db.delete_user(db,mobilephone)


# （7）重复注册的步骤：
#         一、下发注册的请求，注册成功
#         二、下发注册的请求，重复注册
#         三、接口返回值的检查



@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_repeat.yaml"))
def repeat_data(request):
    return request.param


def test_register_repeat(url, baserequests, repeat_data,db):
    mobilephone = repeat_data['data1']['mobilephone']
    # Db.delete_user(db,repeat_data['data']['mobilephone'])
    #下发注册请求
    r = Member.register(url, baserequests, repeat_data['data1'])
    # assert r.json()['code'] == repeat_data['expect1']['code']
    # assert r.json()['msg'] == repeat_data['expect1']['msg']
    # assert r.json()['status'] == repeat_data['expect1']['status']
    # Asserts.check(r.json(),repeat_data['expect'],"code,msg,status")
    Asserts.check(r.json(), repeat_data['expect1'], "code,msg,status")
    #重复注册
    r = Member.register(url, baserequests, repeat_data['data2'])
    # assert r.json()['code'] == repeat_data['expect2']['code']
    # assert r.json()['msg'] == repeat_data['expect2']['msg']
    # assert r.json()['status'] == repeat_data['expect2']['status']
    Asserts.check(r.json(), repeat_data['expect2'], "code,msg,status")
    print(r.json()['code'])
    # 清理环境：删除注册的用户
    Db.delete_user(db,mobilephone)



























# def test_list(url,baserequests,pass_data):
#     r = Member.list(url,baserequests,pass_data['data'])
#     # print(r.text)
#     s=[]
#     i=r.json()['data']
#     for j in i:
#         s.append(j['mobilephone'])
#     print(s)
#     if str(pass_data['data']['mobilephone']) in s:
#         print('True')
#     else:
#         print('False')
#     print(pass_data['data']['mobilephone'])






