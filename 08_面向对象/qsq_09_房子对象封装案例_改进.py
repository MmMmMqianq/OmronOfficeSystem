class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area


class House:
    def __init__(self, apartment, area):
        self.apartment = apartment
        self.area = area
        self.remaining_area = area
        self.furniture_list = []
        self.print_furniture = ""

    def add_furniture(self, furniture):
        if self.remaining_area < furniture.area + 70:
            print("不能再添加家具了")
            return
        self.remaining_area = self.remaining_area - furniture.area
        self.furniture_list.append(furniture.name)
        self.print_furniture = ""
        for furniture_name in self.furniture_list:
            if self.furniture_list.index(furniture_name) + 1 != len(self.furniture_list):
                self.print_furniture = self.print_furniture + "{0:}, ".format(furniture_name)
            else:
                self.print_furniture = self.print_furniture + "{0:}".format(furniture_name)

    def __str__(self):
        return "户型为：{0:s}，总面积为：{1:.2f}，剩余面积为{2:.2f}，房子内的家具有：{3:}"\
            .format(self.apartment, self.area, self.remaining_area, self.print_furniture)


bed = Furniture("席梦思", 3.8)
wardrobe = Furniture("衣柜", 3)
dining_table = Furniture("餐桌", 3.6)

house = House("四室一厅", 145.8)

house.add_furniture(bed)
house.add_furniture(wardrobe)
house.add_furniture(dining_table)
print(house)

