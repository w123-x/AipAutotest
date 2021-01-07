'''fixture作用域
函数级（默认）、模块级、类级、Session级别的（跨文件的）'''
import pytest

#scope='function' 函数级别，即每个调用db的函数的地方都执行测试前置和测试后置。（用例2、4都执行db测试前置和后置）
#scope='module' 模块级别，即首次调用login的地方执行测试前置，等整个文件执行完后，再执行测试后置。（用例2执行前置，用例4执行后置）
@pytest.fixture(scope="module")
def login():
    print("前置：登录系统")
    yield
    print("后置：退出登录")

@pytest.fixture(scope='function')
def db():
    print("前置：连接数据库")
    yield
    print("后置：断开数据库连接")

def test_01():
    print("用例1")
def test_02(login,db):
    print("用例2")
def test_03(login):
    print("用例3")
def test_04(login,db):
    print("用例4")