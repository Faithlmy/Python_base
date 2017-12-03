import http.cookiejar
import urllib.request
import urllib.error
import urllib.parse


def get_urlNext_req(url_login, url_passwd, url_login_next ):#url_login首页url  url_passwd首页密码 url_login_next登录后url
    # 创建cookie
    cookie_file_name = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(cookie_file_name)
    open_hand = urllib.request.HTTPCookieProcessor(cookie)#初始化全局的open
    open_er = urllib.request.build_opener(open_hand)

    #用cookie发送请求
    login = url_login
    passwd = url_passwd
    post_data = urllib.parse.urlencode(passwd).encode('utf-8')
    req = urllib.request.Request(login, post_data)
    try:
        res = open_er.open(req)
        page = res.read().decode()#url_login页面显示
    except urllib.error.URLError as e:
        print(e.code, ':', e.reason)
    cookie.save(ignore_discard=True, ignore_expires=True)#保存登录成功的cookie

    login_next = url_login_next
    req_next = urllib.request.Request(login_next)
    res_next = open_er.open(req_next)#url_login_next页面的显示
    return page, res_next.read().decode()

def login_info(login, username, password, login_next):
    url_login = login
    values = {'username': username,
              'password': password
              }
    url_login_next = login_next
    result_login, result_next = get_urlNext_req(url_login, values, url_login_next)
    return result_login, result_next

# if __name__ == "__main__":
#     url_login = r'http://10.129.4.97:90/ac/login'
#     values = {'username': 'F1330314',
#               'password': 'F1330314'
#               }
#     url_login_next = r'http://10.129.4.97:90/forms/colors'
#     result_login, result_next = get_urlNext_req(url_login, values, url_login_next)
#     # print(result_login)
#     # print('*' * 50)
#     # print(result_next)