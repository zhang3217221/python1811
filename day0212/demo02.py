'''
类方法： 需要使用@classmethod声明 第一个参数为cls 可访问类相关 比如类说明
实例方法：方法的第一个参数是self 用来操作实例属性
静态方法：需要用@staticmethod声明  和类无关
'''

class Person(object):

    def __init__(self,name):
        self.name=name

    def newname(self):
        print("声明类方法newname")

    # 类方法
    @classmethod
    def naee(cls):
        print(cls.__doc__)


    #静态方法
    @staticmethod
    def bb():
        print("静态方法")

a1=Person("abc")
a1.newname()
a1.bb()
a1.naee()


