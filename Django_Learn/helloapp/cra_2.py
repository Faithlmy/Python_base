import http.cookiejar
import urllib.request
import urllib.parse
from collections import OrderedDict
import json

# #创建session对象
# reqSe = requests.session()
# #提取csrf标记
# login = "http://10.129.4.97:90/ac/login"
# result = reqSe.get(login)
# tree = html.fromstring(result.text)
# at = list(set(tree.x))
#设置cookie
# def set_cookie():
#     #初始一个cookiejar来处理cookie
#     cookie = http.cookiejar.CookieJar()
#     cookieProc = urllib.request.HTTPCookieProcessor(cookie)
#     #实例化一个全局opener
#     opener = urllib.request.build_opener(cookieProc)
#     urllib.request.install_opener(opener)
#打开网页
def get_url_req(open_url, post_data):
    post_data = urllib.parse.urlencode(post_data)
    post_data = post_data.encode(encoding='utf-8')
    req = urllib.request.Request(url=open_url, data=post_data)
    return urllib.request.urlopen(req).read().decode('utf-8')

def login_my(userName, passWord, url_loGin, url_login_Success):
    username = userName
    password = passWord
    url_login = url_loGin
    url_login_success = url_login_Success
    login_params = {
        "username": username,
        "password": password
    }
    get_url_req(url_login, login_params)
    result = get_url_req(url_login_success, login_params)
    return result

if __name__ == "__main__":
    dict_res = login_my(userName='F1330314',
                        passWord='F1330314',
                        url_loGin=r'http://10.129.4.97:90/ac/login',
                        url_login_Success=r'http://10.129.4.97:90/ac/login?format=json')
    print(type(dict_res))
    print(dict_res)
    # username = "F1330314"
    # password = "F1330314"
    # #发送请求的网站
    # url_login = r'http://10.129.4.97:90/ac/login'
    # #登录成功跳转的网址
    # url_login_success = r'http://10.129.4.97:90/ac/login?format=json'
    # #url_login_success = r'http://10.129.4.97:90/ac/login'
    # #登录需要提交的数据
    # login_params = {
    #      "username": username,
    #      "password": password
    #  }
    # #登录
    # get_url_req(url_login, login_params)
    #
    # #登录成功跳转的页面
    # result = get_url_req(url_login_success, login_params)
    # re_json = eval(result)
    # key = []
    # value = []
   # print(type(re_json))
   # print(re_json.get('id'))
   #  for k, v in re_json.items():
   #      key.append(k)
   #      value.append(v)
   #
   #  print(key)
   #  print(value)