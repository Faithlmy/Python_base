"""my_hellopro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
import helloapp.views as m
import my_hellopro.test_django
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^my/$', m.index, name='index'),
    url(r'^my/$', m.index, name='index'),
    #url(r'a=(\d+)&b=(\d+)', m.home, name='home'),
    #url(r'^m/$', m.home, {'a': 5, 'b': 3}),
    url(r'^add/$', m.add, name='add'),
    url(r'^success/$', m.success, name='success'),
    url(r'^addstring/$', m.addstring, name='addstring'),
    url(r'^addlist/$', m.addlist, name='addlist'),
    url(r'^adddict/$', m.adddict, name='addict'),
    url(r'^addcra/$', m.addcra, name='addcra'),
    # url(r'^addcra1/$', m.urlnext, name='addcra'),
    #url(r'^addsum1/$', m.addsum1, name='addsum1'),
    url(r'^adds/$', m.adds, name='adds')

]
