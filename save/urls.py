"""HIW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from save.views import hdfsfile,more,file,delete,mkdir,rename,down,upload

urlpatterns = [
    url(r'^hdfsfile/(\w+)/$', hdfsfile),
    url(r'^more/(\w+)/(.+)/$', more),
    url(r'^file/(\w+)/(.+)/$', file),
    url(r'^delete/(\w+)/(.+)/$', delete),
    url(r'^mkdir/(\w+)/(.+)/$', mkdir),
    url(r'^rename/(\w+)/(.+)/$', rename),
    url(r'^down/(\w+)/(.+)/$', down),
    url(r'^upload/(\w+)/(.+)/$', upload),
]
