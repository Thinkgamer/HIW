# HIW
基于Django和Hadoop集群进行的大数据分析平台

#基本环境
python3.4<br/>
diango1.9.6<br/>
pip install hdfs<br/>
pip install hdfs[avro,dataframe,kerberos]

#注意事项
远程客户端执行hdfs操作，上传和下载文件时，需要将集群的ip和用户名填写在自己本机的hosts文件里，否则会报错<br/>
集群的hiveserver2服务要启动

#搭建平台参考文章
VM+CentOS+hadoop2.7搭建hadoop完全分布式集群<br />
<a href="http://blog.csdn.net/gamer_gyt/article/details/51991893">http://blog.csdn.net/gamer_gyt/article/details/51991893</a><br />
基于hadoop集群的Hive1.2.1、Hbase1.2.2、Zookeeper3.4.8完全分布式安装<br />
<a href="http://blog.csdn.net/gamer_gyt/article/details/52032579">http://blog.csdn.net/gamer_gyt/article/details/52032579</a><br />
基于hadoop2.7集群的Spark2.0，Sqoop1.4.6，Mahout0.12.2完全分布式安装
<a href="http://blog.csdn.net/gamer_gyt/article/details/52045663">http://blog.csdn.net/gamer_gyt/article/details/52045663</a><br />
三台PC服务器部署Hadoop HA（Hadoop 高可用性架构）
<a href="http://blog.csdn.net/gamer_gyt/article/details/52350528">http://blog.csdn.net/gamer_gyt/article/details/52350528</a><br />
