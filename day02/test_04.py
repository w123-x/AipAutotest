'''
fixture默认是函数级别的
测试前置和后置：fixture的方式（用的比较多的方式）
1.命名比较灵活，不用setup、teardown找各种固定的命名
2.使用方便，扩文件使用时，不用import
'''


import pytest

#在普通的函数上增加fixture的注释，表示是测试前置
@pytest.fixture()
def login():
    print("登录系统")
    yield#yield之前的内容是测试前置，yield之后的内容是测试后置
    print("退出登录")


#当autouse=True时，表示测试用例会自动使用（在每个测试用例之前都会执行一次）
@pytest.fixture(autouse=True)
def data():
    print("准备测试数据")

def test_query():
    print("测试查询功能，不需要登录")


#在需要使用前置的地方，方式一；作为参数使用
def test_add(login):#在需要使用前置的地方，将被设置为测试前置的函数的函数名作为参数传进去
    print("测试添加的功能，需要登录")


#在需要使用前置的地方，方式二：使用usefixture注释
@pytest.mark.usefixtures('login')
def test_delete():
    print("测试删除的功能，需要登录")

