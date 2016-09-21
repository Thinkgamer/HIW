#-*-coding:utf-8-*-
from django.contrib import admin
from hive.models import Session
# Register your models here.

class SessionAdmin(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("uname","time","sessionname", "context",)
    # 添加search bar，在指定的字段中search
    search_fields = ("uname","time","sessionname",)
    # 页面右边会出现相应的过滤器选项
    list_filter = ("uname","time", "sessionname",)
    # 排序
    ordering = ("-time",)


admin.site.register(Session, SessionAdmin)
