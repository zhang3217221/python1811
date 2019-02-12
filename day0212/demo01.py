class Person(object):
    #类属性
    name = "zyp"

    def __init__(self,_age):
        #实例属性
        self.age=_age
# s1=Person.name
# s2=Person.name
# print(s1,s2)

# s1=Person(1)
# s2=Person(1)
# Person.name="ZZY"
# print(s1.name,s2.name)

# s1=Person()
# print(s1.age)

s1=Person(10)
s2=Person(20)
Person.age=30
print(s1.name,s2.name)
print(s1.age,s2.age)