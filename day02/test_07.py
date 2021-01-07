'''
fixture带参数
'''
import pytest

# 登录功能的测试数据，列表中的测试数据可以是任意类型的
@pytest.fixture(params=[{"mobilephone": 15129983478, "pwd": 123456 },
                        {"mobilephone": 1801235358, "pwd": 12345},
                        {"mobilephone": 1801235358, "pwd": ""},
                        {"mobilephone": 123, "pwd": 123456}])

def login_data(request):#request是pytest中的关键字
    return request.param#通过request.param返回每一组数据，固定写法




# 登录功能的测试脚本
def test_login(login_data):
    #f：格式化输出，输出的是值，如果不加f的话，会输出字符串
    print(f"登录功能，测试数据为：{login_data}")
    print(f"手机号：{login_data['mobilephone']}")
    print(f"密码：{login_data['pwd']}")
















