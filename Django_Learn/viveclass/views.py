from django.shortcuts import render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import mixins, generics
from functools import wraps
from rest_framework.response import Response
from viveclass.serializers import CpSerializer

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


class CustomerPaper(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                    generics.GenericAPIView
                    ):
    content = {"errmsg": ""}

    @wrapp
    def get(self, request):
        data = request.GET.get("data")
        self.content["payload"] = data
        self.content['status'] = 1
        return self.content
