# 用于记录所有名片字典的列表
all_business_card_list = []


# 显示主菜单
def menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)


def new_business_card():
    name_str = input("输入姓名：")
    tel_str = input("输入号码：")
    QQ_str = input("输入QQ：")
    mail_str = input("输入邮箱：")

    business_card_infomation = {"name":name_str,
                              "tel":tel_str,
                              "QQ":QQ_str,
                              "mail":mail_str}

    all_business_card_list.append(business_card_infomation)


def show_all_business_card():
    # 判断名片列表是否空列表
    if len(all_business_card_list) == 0:
        print("未添加任何名片，请新建名片！")
    else:
        print("所有名片信息如下：")
        print("=" * 80)
        print("   {: <1５s}{: <1５s}{: <16s}{: <1５s}".format("姓名", "电话", "QQ", "邮箱"))
        line_num = 0
        for all_business_card_dict in all_business_card_list:
            line_num += 1
            print("{0}. {1: <16s}".format(line_num, all_business_card_dict["name"]), end="")
            print("{: <16s}".format(all_business_card_dict["tel"]), end="")
            print("{: <16s}".format(all_business_card_dict["QQ"]), end="")
            print("{: <16s}".format(all_business_card_dict["mail"]))
        else:
            print("=" * 80)


def search_for_business_card():
    while True:
        search_for_name = input("输入要搜索的姓名：")
        counts = 0  # 用于判断是否搜索到了名片
        business_card_list = []  # 此列表用于保存搜索的名片字典
        for business_card_dict in all_business_card_list:
            if business_card_dict["name"] == search_for_name:
                business_card_list.append(business_card_dict)
                counts += 1
                if counts == 1:
                    print("查询 %s 名片信息如下：" % search_for_name)
                    print("=" * 80)
                    print("   {: <1５s}{: <1５s}{: <16s}{: <1５s}".format("姓名", "电话", "QQ", "邮箱"))
                print("{0}. {1: <16s}".format(counts, business_card_dict["name"]), end="")
                print("{: <16s}".format(business_card_dict["tel"]), end="")
                print("{: <16s}".format(business_card_dict["QQ"]), end="")
                print("{: <16s}".format(business_card_dict["mail"]))
        else:
            if counts == 0:
                print("未查到此名片，您可以选择新建该名片！")
            else:
                print("=" * 80)
                print("【1】修改  【2】删除  【0】返回主菜单")
                deal_with_business_card_information(business_card_list)
                break


def deal_with_business_card_information(deal_with_list):
    while True:
        business_card_action = input("输入您要执行的操作：")

        if business_card_action == "1":
            # 修改名片
            deal_with_list_dict = choice_business_card_dict(deal_with_list)
            deal_with_list_dict["name"] = input_information(deal_with_list_dict, "姓名", "name")
            deal_with_list_dict["tel"] = input_information(deal_with_list_dict, "电话", "tel")
            deal_with_list_dict["QQ"] = input_information(deal_with_list_dict, "QQ", "QQ")
            deal_with_list_dict["mail"] = input_information(deal_with_list_dict, "邮箱", "mail")
            break
        elif business_card_action == "2":
            # 删除名片
            all_business_card_list.remove(choice_business_card_dict(deal_with_list))
            break
        elif business_card_action == "0":
            # 返回主菜单
            break
        else:
            print("输入错误，请重新输入！")


def choice_business_card_dict(deal_with_list1):
    num_list = []  # 该列表用于保存查询后显示名片前面的编号集合
    for index in deal_with_list1:
        deal_with_list1.index(index)
        num_list.append(str(deal_with_list1.index(index) + 1))
    if len(deal_with_list1) == 1:
        deal_with_list1_dict = deal_with_list1[0]
    if len(deal_with_list1) > 1:
        while True:
            choice_dict_num = input("输入要处理名片编号：")
            if choice_dict_num in num_list:
                deal_with_list1_dict = deal_with_list1[int(choice_dict_num) - 1]
                break
            else:
                print("输入的名片编号错误，请重新输入！")

    return deal_with_list1_dict


def input_information(deal_with_list_dict1, information1, information2):
    change_information = input("输入要修改的%s：" % information1)
    if len(change_information) == 0:
        change_information = deal_with_list_dict1[information2]
    return change_information

