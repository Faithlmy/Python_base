"""
build_in type
"""

"""
boolean: and or not
numeric: int float complex
Bitwise: | ^ & ^ ~ >>  << 
"""

def faith_int():
    """
    bit_length()
    to_
    :return:
    """
    n = 200
    b = bin(n)
    print(
        b, '\n',
        n.bit_length(), '\n',
        n.to_bytes(5, byteorder='big'), '\n',
        n.from_bytes(b'\x00\x00\x00\x00\xc8', byteorder='big'), '\n',
    )
def faith_float():
    print(
        (-2.3).is_integer(), '\n',
        (-2.0).is_integer(), '\n',
        (-2.0).hex(), '\n',
        (2.0).hex(), '\n',
        float.fromhex('0x3.a7p10'), '\n',
        bin(2017), '\n',
    )

def faith_it():
    """
    __iter__()
    __nest__()
    :return:
    """
    pass

def faith_common():
    """
    x in y
    x not in y
    x + y
    x * y or y * x
    s[i]
    s[i:j]
    s[i: j: k]
    len(s)
    min(s)
    max(s)
    s.index()
    s.count(x)
    :return:
    """
    pass

def faith_str():
    """
    加 r 表示查找的位置有第一个和最后一个之分
    :return:
    """
    str = 'hi, python!python!{}'
    str1 = "this is\tstring is example....wow is !!!"

    str3 = 'aouie'
    str4 = '12345'
    t = str.maketrans(str3, str4)
    print('maketrans', t)
    print('translate', str.translate(t))# 将str中的元音转换为指定的数字

    print(str.capitalize())  # 将首字母大写
    print(str.center(50, '*'))  # 居中填充
    print(str.count('p'))  # 计算p出现的次数
    print(str.count('python'))
    print('utf-8 ', str.encode('utf-8',)) # 编码格式
    print('endswith() ', str.endswith('py', 4, 6))  # 是否以指定的字符串结尾,数字定位
    print(str1, '\n',
        str1.expandtabs(), '\n',)
    print(str.find('i'))  # 字符串中某一个字符串出现的位置
    print('format(): ', str.format('vic'))  # 字符串中插入到指定位置
    print('format(): ', str)  # 字符串中插入到指定位置
    print('index', str.index('python', 2))  #
    print(str.isalnum())  # 字符串中是否包含数字
    print(str.isalpha())  # 是否包含字母
    print(str.isdigit())  # 是否仅仅包含数字
    print(str.isdecimal())  # 是否包含小数
    print(str.isidentifier())  # 判断字符串是否是合法的标识符，字符串仅包含中文字符合法，实际上这里判断的是变量名是否合法。
    print(str.isprintable())  # 判断字符串所包含的字符是否全部可打印。字符串包含不可打印字符，如转义字符，将返回False。
    print(str.islower())  # 是否全为小写字母
    print(str.isspace())  # s是否均为空白字符
    print(str.istitle())  # 是否首字母大写
    print(str.isupper())  # 是否均为大写字母
    print('joinmy ', '-'.join(str))  # 连接字符串
    print(str.lower())  # 全部转换为小写字母
    print('888faith888'.strip('8'))  # 截取两头指定字符
    print('888faith888'.lstrip('8'))  # 截取左边指定字符
    print('888faith888'.rstrip('8'))  # 截取右边指定字符
    print(str.ljust(50, '0'))  #左对齐，长度不够用指定字符串补齐
    print('split', str.split())  # 分割字符串
    print('partition', str.partition('py'))  #从指定处切割，返回3元组
    print(str1.replace('is', 'are', 3))  # is 被 are替换， 替换次数不超过 3
    print('find()', str.find('n'))  #从左到右返回 'n' 第一次出现的位置
    print('rfind()', str.rfind('n', -1))  #从左到右返回 'n' 最后一次出现的位置
    print(str.split(' ', 1))  # 1 表示切割次数
    print('splitlines(): ', 'ab c\n\nde fg\rkl\r\n'.splitlines(False))#不保留换行符
    print('splitlines(): ', 'ab c\n\nde fg\rkl\r\n'.splitlines(True))# 保留换行符
    print('startswith', str.startswith('hi'))  # 是否以指定字符串开头
    print('startswith', str.startswith('hi', 3, 6))  # 是否以指定字符串开头
    print('swapcase', str.swapcase())  # 大小写互换
    print('upper', str.upper())  # 大小写互换
    print(str.title())  # 字符串首字母大写
    print(len(str))  # 字符串长度

def faith_printf():

    pass

if __name__ == '__main__':
    # faith_int()
    # faith_float()
    faith_str()