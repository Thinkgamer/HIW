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
    client = Client("http://192.168.132.27:50070")
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
    child_list = client.list(path)
    for child in child_list:
        one_dic = client.status(path+child)
        filepath = "/"+child
        one_dic["path"]=filepath
        dict2obj(one_dic)
        mess_list.append(dict2obj(one_dic))
    return mess_list
