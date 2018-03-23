class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def print_title(self):
        if self.sex == "male":
            print("man")
        elif self.sex == "female":
            print("woman")


class Child(Person):  # Child 继承 Person
    """
    只是继承 Person 里面的方法
    """
    pass


class SubChild(Person):

    def __init__(self, name, age, sex):
        super(SubChild, self).__init__(name, age)
        self.name = name
        self.age = age
        self.sex = sex

    def modify(self, name):
        self.name = name

    def print_title(self):
        if self.sex == "male":
            print("boy")
        elif self.sex == "female":
            print("girl")


class SubChildD(SubChild):
    """
    可以通过继承 SubChild 来访问到 Person 里面的变量和方法
    """
    pass


class SChild(Person):# Child 继承 Person
    def __init__(self, name, sex, mother, father):
        super(SChild, self).__init__(name, sex)
        self.name = name
        self.sex = sex
        self.mother = mother
        self.father = father


if __name__ == "__main__":
    p = Person("meng", "male")
    # p.print_title()
    # p.sex = "female"
    # p.print_title()

    # c = Child("faith", "male")
    # c.print_title()

    # sub = SubChild("meng", 25, "male")
    # # p.print_title()
    # sub.print_title()
    # print(sub.name)
    # sub.modify("yao")
    # print(sub.name)
    sd = SubChildD("meng", 25, "male")
    k = sd.print_title()
    print(isinstance(sd, SubChildD))  # Ture
    print(isinstance(sd, SubChild))  # Ture
    print(isinstance(sd, Person))  # Ture
    print(isinstance(p, Person))  # Ture
    print(isinstance(p, SubChildD))  # False

