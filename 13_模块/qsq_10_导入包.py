"""
什么是包：
1.包是一个包含多个模块的特殊目录；
2.目录下有一个特殊的文件__inti__.py;
3.包名的命名方式和变量名一致，小写字母 + _;

好处：使用 import 包名 可以一次性导入包中的所有模块

包建立步骤：
1.先建立包；
2.新建文件_init_.py，用from . import 模块文件名字 在该文件下添加模块文件；
3.在主程序中用import 包名 导入包；

案例演练：
1.新建一个 qsq_message的包；
2.在目录下，新建两个文件send_message和receive_massage;
3.在send_message文件中定义一个send函数；
4.在receive_message文件中定义一个receive函数；
5.在外部直接导入qsq_message的包
"""
import qsq_massage

qsq_massage.send_massage.send("Hello World")
text = qsq_massage.receive_massage.receive()
print(text)
