from django.shortcuts import render
from rest_framework.response import Response
from django.db import transaction
from rest_framework import status as status_code
from rest_framework.decorators import api_view
from functools import wraps
from django.conf import settings
from test_django import models


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
def test_pass(request):
    content = {"payload": [], "status": 1, "errmsg": None}
    if request.method == 'GET':
        print(1)
    return content