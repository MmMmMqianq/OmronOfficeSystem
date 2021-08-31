def input_password():
    # 输入密码；
    password = input("请输入密码：")
    # 判断密码长度是否 >8，则密码输入符合要求；
    if len(password) > 8:
        # 如果输入的密码长度 <=8，则抛出异常；
        return "您输入的密码为：" + password, password
    else:
        # 如果输入的密码长度 <=8，则抛出异常；
        password_abnormal = Exception("密码长度必须大于8个字符！")  # 用Exception类创建一个抛出的异常对象；
        raise password_abnormal  # 用raise抛出异常；


while True:
    try:
        print(input_password())
        break
    except Exception:
        print("请重新输入密码！")

