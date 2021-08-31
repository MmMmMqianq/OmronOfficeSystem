import business_card_tool

while True:
    # 1.显示启动界面主菜单
    business_card_tool.menu()

    # 2.用户选择想要执行的操作
    action = input("选择执行的操作：")

    # 3. 当用户输入不同数字时，执行对应的操作
    if action =="1":
        # 新建名片
        business_card_tool.new_business_card()

    elif action == "2":
        # 显示所有名片
        business_card_tool.show_all_business_card()

    elif action == "3":
        # 查询名片
        business_card_tool.search_for_business_card()
    elif action == "0":
        # 退出系统
        break
    else:
        # 输入的命令错误，请重新输入
        print("输入错误请重新输入！")