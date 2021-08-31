class Cat:
    def __init__(self, new_name):  # 对象被创建的时候会自动调用该方法
        self.name = new_name
        print("{0:s}来了".format(new_name))

    def __del__(self):
        # 在对象被删除之前系统会自动调用该方法
        print("{0:s}去了".format(self.name))


# tom是个全局变量
tom = Cat("Tom")
print(tom.name)
# del tom  如果使用del关键删除对象，那么在删除tom这个对象之前会自动调用tom._del_方法，所以Tom去了会在横上方输出。
print("-" * 50) # Tom去了会在横杠下方输出。因为tom是个全局变量在所有的代码执行完成之后才会将所有的变量回收，
                # 所以Tom去了才会在横杠下方输出