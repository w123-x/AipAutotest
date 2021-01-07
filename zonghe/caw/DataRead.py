'''读文件相关的方法'''
import configparser
import os
import yaml


def get_project_path():
    '''
    获取当前工程的路径
    ：return:'''
    #当前文件路径
    cp = os.path.realpath(__file__)#D:\ApiAutoTest\zonghe\caw\DataRead.py
    print(cp)
    cd = os.path.dirname(cp)#D:\ApiAutoTest\zonghe\caw
    print(cd)
    print(os.path.dirname(cd)+"\\")
    return os.path.dirname(cd)+"\\" #D:\ApiAutoTest\zonghe\
def read_ini(file_path,key):
    '''
    读取ini配置文件
    :param file_path: 配置文件的路径
    :param key: key值
    :return: key对应的value
    '''
    file_path = get_project_path() + file_path
    config = configparser.ConfigParser()
    config.read(file_path)
    return config.get("env",key)#这里的env对应的是ini文件中的[env]

def read_yaml(file_path):
    '''
    读取yaml文件
    :param file_path: 文件路径
    :return: 文件内容
    '''
    file_path = get_project_path()+file_path
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        return yaml.load(content, Loader=yaml.FullLoader)


#测试代码用完可以删除
if __name__ == '__main__':
    get_project_path()
    # url = read_ini(r"data_env\env.ini","url")
    # print(url)
    # db = read_ini(r"data_env\env.ini","db")
    # print(db)
    # print(type(db))
    # db = eval(db)#eval：解析db原本的类型，即将自付出解析为字典
    # print(db)
    # print(type(db))
    #
    # # c = read_yaml(r"data_case\register_fail.yaml")
    # # print(c)
    # # c = read_yaml(r"data_case\register_pass.yaml")
    # # print(c)
    # c = read_yaml(r"data_case\register_repeat.yaml")
    # print(c)