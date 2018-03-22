from django.shortcuts import render
from functools import wraps
from rest_framework.response import Response
from rest_framework.decorators import api_view
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
def faith(request):
    content = {"payload": [], "status": 0, "errmsg": ""}
    if request.method == 'GET':
        try:
            content['payload'] = 'faith'
        except Exception as e:
            content['errmsg'] = str(e)
    return content

