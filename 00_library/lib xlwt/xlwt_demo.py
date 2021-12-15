"""
xlwt写入Excel步骤：
1. 创建工作簿
2. 添加工作表
3. 填充工作表内容(也为图片bitmap)
4.保存文件
"""
import xlwt


# 初始化样式
tittleStyle = xlwt.XFStyle()  # 初始化字体样式
# 设置字体样式
tittleFont = xlwt.Font()
tittleStyle.font = tittleFont

tittleFont.name = "宋体"  # 设置字体
tittleFont.bold = True  # 是否加粗
tittleFont.height = 15*20  # 字体大小，Excel里选择的字号乘以20
tittleFont.colour_index = 0x0F  # 设置字体颜色，可在xlwt.XFStyle中检索_colour_map_text
tittleFont.underline = xlwt.Font.UNDERLINE_SINGLE  # 设置下划线
tittleFont.italic = True  # 是否为斜体
tittleFont.struck_out = True  # 是否叫删除线
# 设置对齐方式
tittleAlignment = xlwt.Alignment()
tittleStyle.alignment = tittleAlignment

tittleAlignment.horz = xlwt.Alignment.HORZ_CENTER  # 设置水平对齐方式，按住ctrl点击方法名可以查看，
tittleAlignment.vert = xlwt.Alignment.VERT_CENTER  # 设置垂直对齐方式

# 设置边框
tittleBorders = xlwt.Borders()
tittleStyle.borders = tittleBorders

tittleBorders.bottom = xlwt.Borders.DASHED  # 设置边框底部线的样式
tittleBorders.right = 0x04  # 设置边框右侧线的样式，也可以通过没值来设置

# 设置背景色
tittleBackground = xlwt.Pattern()
tittleStyle.pattern = tittleBackground

tittleBackground.pattern = xlwt.Pattern.SOLID_PATTERN
tittleBackground.pattern_fore_colour = 0x36

# 1.创建工作簿
wb = xlwt.Workbook()

# 2. 添加工作表
ws1: xlwt.Worksheet
ws1 = wb.add_sheet("sheet1")

# 3. 填充工作表内容
ws1.write_merge(0, 1, 0, 5, "合并单元格", tittleStyle)  # 合并单元格后再写入数据
ws1.write(2, 0, "你好阿")  # 指定row和column向对应的单元格写入数据
ws1.insert_bitmap("11.bmp", 3, 0)  # 指定单元格插入图片

# 4. 保存文件
wb.save("demo.xls")

