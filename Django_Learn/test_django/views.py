from django.shortcuts import render
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status as status_code
from rest_framework.decorators import api_view
from functools import wraps
from django.conf import settings
from test_django import models
from django.db.models import Q


# Create your views here.
def wrapp(func):
    """
        Response 跨域裝飾器
    """
    @wraps(func)
    def wrappde(*args, **kwargs):
        data = func(*args, **kwargs)
        re = Response(data)
        re['Access-Control-Allow-Origin'] = '*'
        re["Access-Control-Allow-Credentials"] = "true"
        re['Content-Type'] = 'application/json'
        return re

    return wrappde

@api_view(http_method_names=["GET", "PUT", "POST", "DELETE"])
@wrapp
def test_content(request):
    """
    此接口包含以下方面：
    1. 要加跨域裝飾器，原因：
    2. 不引入python的解釋器， models.TbCustomerPaper將不能點出object
    3. 接口輸出格式的潛逃使用
    4. 接口輸出格式的的類型
    :param request:
    :return:
    """
    content = {"payload": [], "status": 1, "errmsg": None}
    content_new = {"payload": {}, "status": 1, "errmsg": None}
    content['payload'] = {'content_info':[], 'models_info':{}}
    content['payload']['content_info'] = {'content_info_next':{}, 'models_info_next':{}}
    content['payload']['content_info']['content_info_next'] = {'content_info_next_next':{}, 'models_info_next':{}}
    if request.method == 'GET':
        content_info ={
            'type_content':str(type(content)),
            'type_content["payload"]':str(type(content["payload"])),
            'type_content_new["payload"]':str(type(content_new["payload"])),
            'type_content["status"]':str(type(content["status"])),
            'type_content["errmsg"]':str(type(content["errmsg"])),
            }
        models_info = {
            'models.TbCustomerPaper': str(models.TbCustomerPaper),
        }
        content['payload']['content_info'] = content_info
        content['payload']['content_info']['content_info_next'] = {1:2}
        content['payload']['content_info']['content_info_next']['content_info_next_next'] = {3:4}#嵌套使用
        content['payload']['models_info'] = models_info
    return content


@api_view(http_method_names=["GET", "PUT", "POST", "DELETE"])
@wrapp
def test_models(request):
    """
    此接口展示models的各種類型:
    1. name = request.GET.get('name')沒有值傳入,將會是None
    2. 多值之間用test_models?version=pp&name=name&type=y 連接
    3. 一個save將會保存一條數據
    4. 用 models.TbCustomerPaper.objects.create(ecn_no=name, st_site=version)也可以保存數據,一個create保存一條
    5. models.TbCustomerPaper.objects.filter().delete()慎用，不填條件，將會刪除數據庫裏面的所有值
    :param request:
    :return:
    """
    content = {"payload": {}, "status": 1, "errmsg": None}
    if request.method == "GET":
        #从url获取值, 對應值的類型
        # 傳入的值是str型， int型轉化數字， eval轉化list 和 dict
        #eval 的值裏面有null， 將會報錯,故用replace來代替
        version = request.GET.get('version')#從url欄獲取值
        name = request.GET.get('name')
        c_type = request.GET.get('type')
        # print(c_type)
        # print(type(c_type))
        # print(eval(c_type))

        c_type = str(c_type).replace('null','None')
        print(c_type)
        print(type(eval(c_type)))
        for k, v in eval(c_type).items():
            print(v)
        # print('type(version)',type(version), int(version))
        # print('name=',name)
        # print('type(name)',type(name))
        # print('eval(name)',eval(name))
        # print('type(eval(name))',type(eval(name)))
        # if name == 'null':
        #     print(1)
        # elif 2 in eval(name):
        #     print(2)

        # 0X01 ===============創建數據================================================================
        # 0b01--> 給數據庫直接添加數據(方法1)
        # b = models.TbCustomerPaper(version="version", p_name="p_name", c_name="c_name")
        # b.save()

        # #0b02-->方法二: 替换值并保存
        # c = models.TbCustomerPaper(ecn_no=name, st_site=version)
        # c.save()
        # c.ecn_no = 'meng'
        # c.save()

        # # 0b03-->方法三: create()
        # create = models.TbCustomerPaper.objects.create(ecn_no=name, st_site=version)
        # create = models.TbCustomerPaper.objects.create(ecn_no=name, st_site=version, c_type=c_type)

        # # 0b04 -->  方法四: 返回值是元组(object, True/False), 若有元组,将不会被创建
        # get_create = models.TbCustomerPaper.objects.get_or_create(ecn_no=name)

        # # 0b05--> get用于将符合条件的对象查询出来, 单独修改值,即的save()
        # get = models.TbCustomerPaper.objects.get(id=26)
        # get.ecn_no = 'zhongguo'
        # get.save()

        # 0X02 ================查找=======================================================
        # # 0b01 --> all():返回数据库所有对象, 用len(all)查询一共有多少條數據
        # all = models.TbCustomerPaper.objects.all()
        #
        # ob02--> all().get()
        # all_get = models.TbCustomerPaper.objects.all().get(id=26)

        # # 0b03--> filter: filter之后的值是 QuerySet， QuerySet 迭代出来的是 dict, exclude 和 filter輸出結果類型一樣， 結果相反
        #filter过滤的条件有：
        """
        id__gt : 大于
        id__gte : 大于等於
        id__lt: 小於
        id__lte: 小於等於
        id__startswith: 以...開頭 
        id__istartswith: 以...開頭  忽略大小寫
        id__endswith: 以...結尾
        id__iendswith: 以...結尾 忽略大小寫
        __year:
        __month:
        __day:
        id__in=[22,23,24] : 在一個list範圍內
        id__range: 在一個範圍之內
        id__exact : 精确于
        id__iexact : 精确于 忽略大小写
        id__contains : 包含
        id__icontains : 包含 忽略大小写

        filter(pub_date__gte=datetime.date.today())
        """
        # filter = models.TbCustomerPaper.objects.filter(id__gt=20, id__lt=23)
        # for k in filter.values('id', 'ecn_no'):
        #     print(type(k))
        #     print(k)
        #
        # exclude = models.TbCustomerPaper.objects.exclude(id__gt=20,id__lt=23)
        # for i in exclude.values('id', 'ecn_no'):
        #     print(i)

        # # 0b04--> 去重複
        # distinct = models.TbCustomerPaper.objects.values('ecn_no').distinct()
        # print(distinct)

        # # 0b05--> 或關係的表示
        #from django.db.models import Q
        # res = models.TbCustomerPaper.objects.filter(Q(id=23) | Q(id=24))
        # for i in res.values():
        #     print(type(res.values()))
        #     print(type(i))
        #     print(i)

        # 0X03 =========查詢結果的處理=================================================
        # # 0b01--> 刪除
        # models.TbCustomerPaper.objects.filter().delete()
        # models.TbCustomerPaper.objects.exclude().delete()

        # # 0b02--> 替換
        # models.TbCustomerPaper.objects.filter().update()

        # # 0b03--> 排序
        # models.TbCustomerPaper.objects.filter().order_by()
        # ob = models.TbCustomerPaper.objects.filter()
        # for i in ob:
        #     print(i.id, i.ecn_no, i.version)

        # # 0b04--> 另一種 或 的表達方式
        # a = models.TbCustomerPaper.objects.filter(id=1)
        # b = models.TbCustomerPaper.objects.filter(id=5)
        # c = a or b
        # print(type(c))
        # for i in c:
        #     print(i.id)

        models_dict = {
            'type_models.TbCustomerPaper': str(type(models.TbCustomerPaper)),
            'origin_models.TbCustomerPaper': str(models.TbCustomerPaper),
            'origin_models.TbCustomerPaper.objects':str(models.TbCustomerPaper.objects),
            'type_models.TbCustomerPaper.objects':str(type(models.TbCustomerPaper.objects)),
            'models.TbCustomerPaper.objects.all()':str(models.TbCustomerPaper.objects.all()),
            'type_models.TbCustomerPaper.objects.all()':str(type(models.TbCustomerPaper.objects.all())),
            # 'create': str(create),
            # 'type_create': str(type(create)),
            # 'type_name':str(type(name)),
            # 'name':name,
            # 'type':str(c_type),
            # 'type_type':str(type(c_type)),
            # 'get':str(get),
            # 'type_get':str(type(get)),
            # 'all': str(all[:3]),
            # 'len_all':len(all),
            # 'type_all':str(type(all)),
            # 'all_get':int(all_get.id),
            'models.TbCustomerPaper.objects.filter(id=22)':str(models.TbCustomerPaper.objects.filter(id=22)),
            'type_models.TbCustomerPaper.objects.filter(id=22)':str(type(models.TbCustomerPaper.objects.filter(id=22))),
            'models.TbCustomerPaper.objects.filter(id=22).values("ecn_no")': str(models.TbCustomerPaper.objects.filter(id=22).values("ecn_no")),
            'type_models.TbCustomerPaper.objects.filter(id=22).values("ecn_no")': str(type(models.TbCustomerPaper.objects.filter(id=22).values("ecn_no"))),
            'models.TbCustomerPaper.objects.exclude(id__gt=20,id__lt=23)':str(models.TbCustomerPaper.objects.exclude(id__gt=20,id__lt=23)),
            'type_models.TbCustomerPaper.objects.exclude(id__gt=20,id__lt=23)':str(type(models.TbCustomerPaper.objects.exclude(id__gt=20,id__lt=23))),
        }
        content['payload'] = models_dict
    return content

@api_view(http_method_names=["GET", "PUT", "POST", "DELETE"])
@wrapp
def cache(request):
    """

    :param request:
    :return:
    """
    pass
