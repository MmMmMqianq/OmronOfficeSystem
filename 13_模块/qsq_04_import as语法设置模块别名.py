"""
import 模块名 as 别名
注意：模块的别名要满足大驼峰命名法
"""
import qsq_01_测试模块1 as TestModule1
import qsq_02_测试模块2 as TestModule2

print(TestModule1.global_a)
print(TestModule2.global_a)

TestModule1.test()
TestModule2.test()

dog1 = TestModule1.Dog()
print(dog1)

dog2 = TestModule2.Dog()
print(dog2)