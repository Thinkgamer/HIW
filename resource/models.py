#-*-coding:utf-8-*_
from django.db import models

# Create your models here.
class node(models.Model):
    ip = models.CharField(blank=True,max_length=15,verbose_name="IP地址")
    hostname=models.CharField(blank=True,max_length=20,verbose_name="机器名字")
    run_neicun = models.IntegerField(blank=True,verbose_name="运行内存")
    disk_neicun = models.IntegerField(blank=True,verbose_name="硬盘内存")
    os = models.CharField(blank=True,max_length=20,verbose_name="操作系统")
    desc = models.TextField(blank=True,verbose_name="机器描述")

    def __str__(self):
        return self.hostname

    class Meta:
        db_table="NodeMess"

