'''
fixture作用域；类级别的
每个类，首次调用login的地方执行前置，类中用例执行完执行后置
'''

import pytest


@pytest.fixture(scope='class')#在首次调用login的地方执行测试前置，整个类结束的地方执行测试后置
def login():
    print("登录系统")
    yield
    print("退出系统")

class TestQuery:
    def test_001(self):
        print("用例1")
    def test_002(self,login):#执行前置
        print("用例2")
    def test_003(self):
        print("用例3")
    def test_004(self):#执行后置
        print("用例4")


class TestAdd:
    def test_001(self):
        print("用例1")

    def test_002(self):
        print("用例2")

    def test_003(self,login):#执行前置
        print("用例3")

    def test_004(self):#执行后置
        print("用例4")



