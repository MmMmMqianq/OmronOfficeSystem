
# import  qsq_01_测试模块1, qsq_02_测试模块2   # 不建议使用这种方法导入多个模块
import qsq_01_测试模块1
import qsq_02_测试模块2

print(qsq_01_测试模块1.global_a)
print(qsq_02_测试模块2.global_a)

qsq_01_测试模块1.test()
qsq_02_测试模块2.test()

dog1 = qsq_01_测试模块1.Dog()
print(dog1)

dog2 = qsq_02_测试模块2.Dog()
print(dog2)