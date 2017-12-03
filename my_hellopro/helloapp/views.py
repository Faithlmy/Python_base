from django.shortcuts import render
from django.http import HttpResponse
from helloapp.cra_2 import login_my
from .form import AddForms
from helloapp.cra_9add import get_urlNext_req
import os
# Create your views here.
def index(request):
    return HttpResponse(u'lmy')

def home(request, a, b):
    return HttpResponse(str(int(a) + int(b)))

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(int(c))

def success(request):
    return render(request, 'home.html')
def addstring(request):
    string = u'learn'
    return render(request, 'home.html', {'string': string})

def addlist(request):
    stulist = ['html','css', 'java']
    return render(request, 'home.html', {'stulist':stulist})


def adddict(request):
    add_dict = {'1': u'django', '2': u'html', '3': u'python'}
    return render(request, 'dict.html', {'add_dict': add_dict})

def addcra(request):
    dict_res = login_my(userName='F1330314',
                        passWord='F1330314',
                        url_loGin=r'http://10.129.4.97:90/ac/login',
                        url_login_Success=r'http://10.129.4.97:90/ac/login?format=json')
    dict_result = eval(dict_res)
    return render(request, 'addcra.html', {'dict_result': dict_result})

# def urlnext(request):
#     url_login = r'http://10.129.4.97:90/ac/login'
#     values = {'username': 'F1330314',
#               'password': 'F1330314'
#               }
#     url_login_next = r'http://10.129.4.97:90/forms/logos'
#     result_login, result_next = get_urlNext_req(url_login, values, url_login_next)
#     result_login = eval(result_login)
#     result_next = eval(result_next)
#     return render(request, 'addcra1.html', {'result_next': result_next})
#
# def urlnext(request):
#     app = request.GET.get('app')
#     if app == 'calc':
#         result_next = os.system('open /my_hellopro/cookie.txt')
#         #result_next = os.system('open /collectapi/manageapi/cra_9add.py')
#         # url_login = r'http://10.129.4.97:90/ac/login'
#         # values = {'username': 'F1330314',
#         #           'password': 'F1330314'
#         #           }
#         # url_login_next = r'http://10.129.4.97:90/forms/logos'
#         # result_login, result_next = get_urlNext_req(url_login, values, url_login_next)
#         # result_login = eval(result_login)
#         # result_next = eval(result_next)
#         return render(request, 'my_project.html', {'result_next': result_next})


def adds(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForms(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            userName = form.cleaned_data['userName']
            passWord = form.cleaned_data['passWord']
            url_login = form.cleaned_data['url_login']
            url_next = form.cleaned_data['url_next']
            values = {'username': userName,
                      'password': passWord
                      }
            result_login, result_next = get_urlNext_req(url_login, values, url_next)

            result_next_e = eval(result_next)
            result_login_e = eval(result_login)
            print(type(result_login_e))
            return render(request, 'cra.html', {'result_login_e': result_login_e, 'result_next_e': result_next_e, 'form': form})
    else:  # 当正常访问时
        form = AddForms()
        return render(request, 'cra.html', {'form': form})

# def addsum1(request):
#     if request.method == 'POST':  # 当提交表单时
#
#         form = AddForms(request.POST)  # form 包含提交的数据
#
#         if form.is_valid():  # 如果提交的数据合法
#             a = form.cleaned_data['a']
#             b = form.cleaned_data['b']
#             d = str(int(a) + int(b))
#             return render(request, 'button.html', {'d': d, 'form': form})
#     else:  # 当正常访问时
#         form = AddForms()
#         return render(request, 'button.html', {'form': form})

# import helloapp.models as m
#
# # import os, django
# # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_hellopro.settings")# project_name 项目名称
# # django.setup()
# p1 = m.HelloappMyInfoA(username='李逵', password='1234', age=2, sex=True)
# p1.save()
# p2 = m.HelloappMyInfoA(username='lili', password='1234a', age=3, sex=False)
# p2.save()


