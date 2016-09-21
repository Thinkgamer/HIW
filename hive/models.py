#-*-coding:utf-8-*-
from django.db import models

# Create your models here.
class Session(models.Model):
    uname = models.CharField(blank=False,max_length=15,verbose_name="用户名")
    time = models.DateTimeField(blank=True,verbose_name="时间")
    sessionname = models.CharField(blank=True,max_length=20,unique=True,verbose_name="事务名")
    context = models.TextField(blank=True,verbose_name="提交的内容")

    def __str__(self):
        return self.sessionname

    class Meta:
        db_table = "session"
