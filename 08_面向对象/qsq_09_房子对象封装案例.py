class House:
    def __init__(self, apartment_layout, house_area):
        self.apartment_layout = apartment_layout
        self.house_area = house_area
        self.remaining_area = house_area
        self.bed_area = 4
        self.wardrobe_area = 2
        self.table_area = 1.5
        self.furniture = ["bed", "wardrobe", "table"]

    def add_furniture(self):
        self.remaining_area = self.remaining_area - self.bed_area - self.table_area - self.wardrobe_area

    def __str__(self):
        return "房子的户型是{0:s}，总面积为{1:.2f}，剩余面积为{2:.2f}，房子里家具分别为{3:}、{4:}、{5:}"\
            .format(self.apartment_layout, self.house_area, self.remaining_area, *self.furniture)


house = House("四室一厅", 148.8)
house.add_furniture()
house.add_furniture()
house.add_furniture()
print(house)