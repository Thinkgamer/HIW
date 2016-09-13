#-*-coding:utf-8-*-
import os
def runmr(jar_path,input_path,output_path,main_class_name):
    local_path = "/opt/jar/"
    #jar name
    jar_name = jar_path.split("/")[-1]
    #download file
    from save.actionhdfs import down_file
    down_file(jar_path,local_path)
    #run jar
    os.system("/opt/bigdata/hadoop/bin/hadoop jar  %s %s %s %s"% (local_path+jar_name,'wordcount',input_path,output_path))
    #print local_path+jar_name,"\t",main_class_name,"\t",input_path,"\t",output_path
    #print "/opt/bigdata/hadoop/bin/hadoop jar  %s %s %s %s" % (local_path+jar_name,'wordcount',input_path,output_path)
    return output_path