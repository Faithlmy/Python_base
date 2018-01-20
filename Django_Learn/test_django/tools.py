import re
import time
def input_value(value):
    """
    處理get/post/put到的字符串:
    1.結果返回去掉str的原本的屬性
    :param value:
    :return:
    """
    if isinstance(value, str):
        # null_list = ["null", "NULL",
        #              "Null", "nUll", "nuLl", "nulL",
        #              "NUll", "NuLl", "NulL", "nULl", "nUlL", "nuLL",
        #              "NULl", "NUlL", "nULL", ]
        # for n in null_list:
        #     if n in value:
        #         value = value.replace(n, "None").replace('，', ',')
        reg = re.compile(re.escape('null'), re.IGNORECASE)
        value = reg.sub('None',value)
        l = len(value)
        if value.startswith('[', 0) and value.startswith(']', l - 1):
            # value = value.strip('[]').split(',')#用eval也可以
            value = eval(value)
        elif value.startswith('{', 0) and value.startswith('}', l - 1):
            value = eval(value)
        elif value.isdigit():
            value = int(value)
    return value



def put_value(value):
    """
    處理get/post/put到的字符串:
    1.結果返回去掉str的原本的屬性
    :param value:
    :return:
    """
    if isinstance(value, str):
        null_list = ["null", "NULL",
                     "Null", "nUll", "nuLl", "nulL",
                     "NUll", "NuLl", "NulL", "nULl", "nUlL", "nuLL",
                     "NULl", "NUlL", "nULL", ]
        for n in null_list:
            if n in value:
                value = value.replace(n, "None").replace('，', ',')
        # reg = re.compile(re.escape('null'), re.IGNORECASE)
        # value = reg.sub('None',value)
        l = len(value)
        if value.startswith('[', 0) and value.startswith(']', l - 1):
            # value = value.strip('[]').split(',')#用eval也可以
            value = eval(value)
        elif value.startswith('{', 0) and value.startswith('}', l - 1):
            value = eval(value)
        elif value.isdigit():
            value = int(value)
    return value

if __name__ == "__main__":
    # value = '{"kk" : null}'
    # value = '["pp", "null"]'
    # value = '[2,3,4]'
    list1 = ['pp', 'kk', 'null']
    list2 = [1, 'pp', None, 'null']
    list3 = ['pp', {1:2}]
    list4 = ['p', {1,2}]
    list5 = ['ii', {1:'null'}]
    list6 = ['yy', '{23:null}']
    list7 = ['pp', ['tt', 'uu', 'null']]
    d1 = {2:'pp', 'uu':'null'}
    d2 = {2:['pp','yy']}
    d3 = {2:{7:'tt'}}
    d4 = {2:{9:'Null'}}
    d5 = {}
    for i in range(500000):
        d5.update({
            i:{9:"Null"}
        })
    value = str(d5)
    # print(value)
    # print(eval(value))
    # value = '23'

    # print(value)
    # value = value.replace('，', ',').replace('k','K')
    # print(value)
    # v = input_value(value)
    # print(type(v))
    # print(v)
    s = time.time()
    # for i in range(1):
    v = put_value(value)
    e = time.time()
    print(e-s)
    # p = value.strip('{}').split(',')
    # print(p)
    # print(type(p))