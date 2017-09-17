# coding:utf8
'''自定义类Member实现'''


class Member:
    __metaclass__ = type
    member_id = 0  # 成员变量

    def __init__(self, name='song', tel=None, sex=None, age=None):
        self.name = name
        self.tel = tel
        self.sex = sex
        self.age = age

    def __iter__(self):
        return self

    def next(self):
        self.member_id = self.member_id + 1
        if self.member_id > 10:
            raise StopIteration
        return self.member_id

    def getName(self):
        say = 'I am a baby.'
        print(say)
        return self.name
