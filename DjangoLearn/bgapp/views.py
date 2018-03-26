from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from functools import wraps
from rest_framework import status as status_code
from .models import *
# Create your views here.

def wrapp(func):
    """
        Response 跨域裝飾器
    """

    @wraps(func)
    def wrappde(*args,**kwargs):
        data=func(*args,**kwargs)
        re = Response(data)
        re['Access-Control-Allow-Origin'] = '*'
        re["Access-Control-Allow-Credentials"] = "true"
        re['Content-Type'] = 'application/json'
        return re
    return wrappde


@api_view(http_method_names=["GET", "PUT", "POST", "DELETE"])
@wrapp
def faithmy(request):
    content = {}
    m = {}
    if request.method == 'GET':
        content['error'] = ''
        try:
            print(type(request.META))
            data1 = faith.objects.values()
            data2 = hellomy.objects.values()
            content['data2'] = data2
            content['data1'] = data1
            content['code'] = status_code.HTTP_200_OK
        except Exception as e:
            content['code'] = status_code.HTTP_202_ACCEPTED
            content['error'] = str(e)
        finally:
            return content, str(request.META)

# 兩種post提交方式
#     if request.method == 'POST':
#         try:
#             name = request.POST['name']
#             age = request.POST['age']
#             sex = request.POST['sex']
#             print(name)
#             hellomy.objects.create(name=name, age=age, sex=sex)
#         except Exception as e:
#             print(e)

    # if request.method == 'POST':#delete
    #     try:
    #         name = request.POST['name']
    #         id = request.POST['id']
    #         print(name)
    #         hellomy.objects.filter(name=name).delete()
    #         hellomy.objects.filter(id=id).delete()
    #     except Exception as e:
    #         print(e)

    if request.method == 'POST':  # delete
        try:
            name = request.POST['name']
            newname= request.POST['newname']
            # print(name)
            # f = hellomy.objects.get(id=9)
            f = hellomy.objects.all().values('name')
            print(f)
            hellomy.objects.filter(name=name).update(sex=newname)
        except Exception as e:
            print(e)



    # if request.method == 'POST':
    #     data = request.data
    #     print(list(data))#<class 'django.http.request.QueryDict'>
    #     print(dict(data))#<class 'django.http.request.QueryDict'>
    #     name = data['name']
    #     age = data['age']
    #     sex = data['sex']
    #     s = hellomy()
    #     s.name = name
    #     s.age = age
    #     s.sex = sex
    #     s.save()

    #
    # if request.method == 'POST':
    #     con = {}
    #     try:
    #         d = request.data
    #         print('d', d)
    #         name = d['name']
    #         age = d['age']
    #         sex = d['sex']
    #         s = hellomy()
    #         s.name = name
    #         s.age = age
    #         s.sex = sex
    #         print('s.objects ', s.objects)
    #         s.save()
    #         con['code'] = status_code.HTTP_200_OK
    #         con['data'] = 'add success'
    #         return con
    #     except Exception as e:
    #         con['code'] = status_code.HTTP_202_ACCEPTED
    #         con['error'] = str(e)
    #         return con
