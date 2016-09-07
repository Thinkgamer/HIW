# HIW
基于Django和Hadoop集群进行的大数据分析平台

#基本环境
python3.4
diango1.9.6
pip install hdfs
pip install hdfs[avro,dataframe,kerberos]

#注意事项
远程客户端执行hdfs操作，上传和下载文件时，需要将集群的ip和用户名填写在自己本机的hosts文件里，否则会报错