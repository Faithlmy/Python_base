class person():
    def __init__(self):
        pass
    def __call__(self, friend, age):
        self.friend = friend
        self.age = age
        #print('name is : %s, %s' %(self.name, self.age))
        print('friend is : %s, %s' %(friend, age))
p = person()
p('n','23')