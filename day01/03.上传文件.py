'''
上传文件：
    本地文件上传到服务器上，比如上传头像，上传附件等
上传文件的接口是post接口
'''
import requests

#上传文件的接口
url = "http://www.httpbin.org/post"
#要上传的文件（本地磁盘上的文件）
filePath = "d:/test.txt"
filePath2 = "d:/haha.jpg"
#'name': file-tuple
#file-tuple`` can be a 2-tuple ``('filename', fileobj)``,
# 3-tuple ``('filename', fileobj, 'content_type')``
#a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)

with open(filePath, 'rb') as f:
    with open(filePath2, 'rb') as f2:
        file = {
            # f:要打开的文件对象
            "file1": (filePath, f), #2-tuple('filename',fileobj)
            #content_type MIME 类型，大类型/子类型 text/plain image/jpg application/json......
            "file2": (filePath2, f2,"image/jpg")  # 3-tuple('filename',fileobj,'content_type')
        }
        r = requests.post(url, files=file)
        print(r.text)
