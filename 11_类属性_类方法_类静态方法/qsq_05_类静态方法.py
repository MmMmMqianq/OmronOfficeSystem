"""
静态方法语法：
@staticmethod
def 方法名():  # 括号里面不要传递任何参数
    pass

注意：1.静态方法不要调用任何类属性和实例属性时可以使用静态方法；
     2.静态方法一般可以用作输出类的说明信息；
"""

class Person(object):
    @staticmethod
    def run():
        print("跑步有利于身体健康")

# 调用静态方法：类名.静态方法名，调用静态方法是不需要对象的；
Person.run()
