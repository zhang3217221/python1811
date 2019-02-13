import types
class Person(object):
    '''
    说明
    '''
    def __init__(self,_age):
        self.age=_age
#定义实例方法
def move(self,new):
    self.age=new
s1=Person(18)
s1.move=types.MethodType(move,s1)
s1.move(20)
print(s1.age)


class AI(object):
    '''
        说明
        '''
    def __init__(self):
        pass
#添加类方法
@classmethod
def lei(cls):
    return cls.__doc__
s2=AI()
AI.l=lei
print(AI.l())

#添加静态方法
@staticmethod
def dead():
    print('静态方法')

s3=AI()
AI.d=dead
AI.d()

