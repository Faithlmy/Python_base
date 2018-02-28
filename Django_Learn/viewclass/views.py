from django.shortcuts import render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, generics
from functools import wraps
from rest_framework.response import Response
import viewclass.models as models
from viewclass.serializers import CpSerializer

# Create your views here.

# import os
# os.environ.update({"DJANGO_SETTINGS_MODULE": "config.settings"})


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


class CustomerPaper(
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                    generics.GenericAPIView,
                    ):
    """
    這裏可以做接口提示
    """
    queryset = models.TbCustomerPaper.objects.all()
    serializer_class = CpSerializer
    content = {"errmsg": ""}

    @wrapp
    def get(self, request):
        """
        不用將接口分開,判斷是否有值輸入,用兩個if完成是否分頁
        :param request:
        :return:
        """
        id = request.GET.get("id")
        #  不輸入 id , id 的值爲 None
        if id:
            #print(type(id))  # 輸入的id的類型爲 str
            m = models.TbCustomerPaper.objects.filter(id=int(id))
            my_list = []
            for i in m.values():
                i['st_site'] = "faith"  # 賦值
                i['site'] = i.pop('enabled')  # 改值
                i.pop('alter_cause')  # 刪除一個值
                my_list.append(i)  # 生成新的列表
            self.content["payload"] = my_list
        elif id is None:
            #print(id)
            #print(type(id))  # 類型爲 NoneType
            m = models.TbCustomerPaper.objects.filter()
            my_list = []
            for i in m.values():
                i['st_site'] = "faith"  # 賦值
                i['site'] = i.pop('enabled')  # 改值
                my_list.append(i)  # 生成新的列表
            self.content["payload"] = my_list
        # k = self.get_serializer()
        # print(k)

        # self.content["payload"] = m.values()
        self.content['status'] = 1
        return self.content

    @wrapp
    def post(self, request):
        st_site = request.POST.get('st_site')
        current = request.POST.get('current')
        if current and isinstance(eval(current), int):
            #print('current', type(eval(current)))
            ecn_no = request.POST.get('ecn_no')
            models.TbCustomerPaper.objects.create(st_site=st_site, current=current, ecn_no=ecn_no)
            self.content['payload'] = " create success."
        else:
            self.content['errmsg'] = '類型錯誤!'
        return self.content

    @wrapp
    def put(self, request):
        return self.content

    @wrapp
    def delete(self, request):
        return self.content
