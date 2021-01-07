'''
fixture作用域为session级别时
1.公共的方法放到conftest.py文件中
2.pytest是根据文件名字找到这些方法，不需要import
3.整个执行过程，测试前置和后置执行一次
4。conftest.py一个工程可以存在多个，并且conftest.py对所在目录及其子目录生效
'''
import pytest

#测试前置和后置
@pytest.fixture(scope='session')
def login():
    print("登录系统")
    yield
    print("退出登录")