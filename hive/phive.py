#-*-coding:utf-8-*-
from impala.dbapi import connect

def conn():
    con = connect(host="192.168.132.27",port=10000,auth_mechanism="PLAIN")
    cur = con.cursor()
    return cur

#查看数据库
def show_databases():
    cur = conn()    
    cur.execute("show databases")
    return cur.fetchall()
   
#查看表
def show_tables(database):
    cur=conn()
    cur.execute("use %s" % database)
    cur.execute("show tables")
    return cur.fetchall()

#执行HQL语句
def run_hql(sql):
    sql_list = sql[:-1].split(";")
    cur=conn()
    for s in sql_list:
        cur.execute(s)
    result=cur.fetchall()
    return result

if __name__=="__main__":
    #db=show_databases()
    sql="show databases;use default;show tables;"
    print run_hql(sql)  
