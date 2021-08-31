# 1.从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
# 2.电脑随机出拳 —— 先假定电脑只会出石头，完成整体代码功能比较胜负

# 规则：
# 1.石头 胜 剪刀
# 2.剪刀 胜 布
# 3.布 胜 石头

# 小技巧：代码太长可以用括号括起来按回车分行，
# 例如：If () or () or () or () or ():
# 可以写为：If (()
#               or ()
#               or ()
#               or ()):

# 注意：在导入工具包的时候要将语句放在代码的顶部。
# 因为这样方便下方带码使用，在任何时候都能使用工具包中的工具
import random  # 导入随机函数

computer = random.randint(1, 3)
player = int(input("玩家输入要出的拳（石头（1）／剪刀（2）／布（3））："))

print("玩家出的拳是 %d，电脑出的拳是 %d" % (player,computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家胜！牛逼啊！")
elif ((player == 1 and computer == 1)
      or (player == 2 and computer == 2)
      or (player == 3 and computer == 3)):
    print("平局，势均力敌啊！")
else:
    print("电脑胜！玩家再接再厉！")