#-*-coding:utf-8-*-
from django.contrib import admin
from resource.models import node
# Register your models here.

class NodeAdmin(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("ip", "hostname", "run_neicun","disk_neicun","os",)
    # 添加search bar，在指定的字段中search
    search_fields = ("ip", "hostname", "run_neicun","disk_neicun","os",)
    # 页面右边会出现相应的过滤器选项
    list_filter = ("ip", "hostname", "run_neicun","disk_neicun","os",)
    # 排序
    ordering = ("-ip",)

admin.site.register(node, NodeAdmin)