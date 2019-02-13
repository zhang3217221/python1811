
class Person(object):
    def __init__(self,_name):
        self.name=_name
#通过类名添加类属性
s1=Person("zyp")
print(s1.name)
Person.age=18
print(Person.age)

#通过动态添加
s1.hp=50
print(s1.hp)

#使用__slots__禁止添加其他属性
class AI(object):

    __slots__ = ('hp','mp')
AI.name="zzy"
print(AI.name)
s2=AI()
s2.hp=150
s2.mp=510
print(s2.hp,s2.mp)
s2.age=20
print(s2.age)
