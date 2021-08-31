"""
导入模块中工具语法：
from 模块名 import 工具名
from 模块名 import *  # 可以将所有工具都导入，和 import 模块名 导入是一样的，区别在于前者可以直接使用工具名；
                     # 但是如果用*导入所有工具，如果多个模块中存在相同工具名就会出现问题，所以不推荐使用；
注意：1.如果两个模块里有相同的工具名，要使用as重命名，否则程序执行是以下面的import导入的工具执行，后导入的工具会覆盖掉之前的工具；
     2.导入之后可以在程序中直接使用工具名---全局变量、函数、类

     3.模块的搜索顺序：首先Python会在当前的目录下查找模块，如果有就会直接导入。如果当前目录没有找到，再到系统的的目录查找对应的模块。
"""
from qsq_01_测试模块1 import Dog as Dog1, test as test1, global_a as global_a1
from qsq_02_测试模块2 import Dog as Dog2, test as test2, global_a as global_a2

print(global_a1)
print(global_a2)

test1()
test2()

dog1 = Dog1()
print(dog1)

dog2 = Dog2()
print(dog2)