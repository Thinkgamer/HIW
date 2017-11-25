#-*-coding:utf-8-*-
'''
>>> from hdfs.client import Client
>>> client = Client("http://localhost:50070")  # 50070: Hadoop默认namenode
>>> dir(client)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__',
 '__module__', '__new__', '__reduce__', '__reduce_ex__', '__registry__', '__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', '__weakref__', '_append', '_append_1', '_create', '_create_1', '_delete',
  '_get_content_summary', '_get_file_checksum', '_get_file_status', '_get_home_directory', '_list_status',
   '_mkdirs', '_open', '_rename', '_request', '_session', '_set_owner', '_set_permission', '_set_replication',
    '_set_times', '_timeout', 'checksum', 'content', 'delete', 'download', 'from_options', 'list', 'makedirs',
     'parts', 'read', 'rename', 'resolve', 'root', 'set_owner', 'set_permission', 'set_replication', 'set_times',
      'status', 'upload', 'url', 'walk', 'write']
'''
from hdfs import *
# connect hdfs
def connect():
    client = Client("http://192.168.1.105:50070")
    return client
#将字典转化为类
def dict2obj(args):
    '把字典递归转化为类'
    class obj(object):
        def __init__(self, d):
            for a, b in d.items():
                if isinstance(b, (list, tuple)):
                    setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
                else:
                    setattr(self, a, obj(b) if isinstance(b, dict) else b)
    return obj(args)

#get all file
def get_all_file(path):
    client = connect()
    mess_list = []
    if path=="/":
        pass
    else:
        path=path+"/"
    child_list = client.list(path)
    for child in child_list:
        one_dic = client.status(path+child)
        filepath = path+child
        one_dic["path"]=filepath
        dict2obj(one_dic)
        mess_list.append(dict2obj(one_dic))
    return mess_list

#more
def show_more(path):
    client = connect()
    return client.status(path)
#delete
def delete_path(path):
    client = connect()
    return client.delete(path,recursive=True)

#makedirs
def mkdir_path(path):
    client = connect()
    return client.makedirs(path)

#重命名
def rename_path(old_path,new_path):
    client = connect()
    return client.rename(old_path,new_path)

#下载文件
def down_file(hdfs_path,local_path):
    client = connect()
    return client.download(hdfs_path,local_path,overwrite=True)

#上传文件
def upload_file(hdfs_path,local_path):
    client = connect()
    return client.upload(hdfs_path,local_path,overwrite=True)

#login模块使用
#在hdfs的根目录下创建一个当前用户的文件夹,如果存在则不创建
def login_mkdir(name):
    client = connect()
    dict_list = client.list("/")
    if name not in dict_list:
        client.makedirs("/%s" % name)