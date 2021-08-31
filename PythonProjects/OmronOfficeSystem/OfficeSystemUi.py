from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget
import threading
import HandleTaxiData


class OfficeSystem:

    def __init__(self):
        self.taxi_data = list()
        self.get_add_name_text = str()
        self.get_line_edit_upper_limit_text = str()
        self.get_line_edit_lower_limit_text = str()
        self.get_line_edit_upper_limit_int = 350
        self.get_line_edit_lower_limit_int = 400

        self.ui = QUiLoader().load('Ui.ui')
        self.ui.lineEdit_name.setPlaceholderText('请输入名字：')
        self.ui.lineEdit_upperlimit.setPlaceholderText('请输入上限值：')
        self.ui.lineEdit_lowerlimit.setPlaceholderText('请输入下限值：')

        # 部件显示和隐藏
        self.ui.widget_taxi.setVisible(False)
        self.ui.widget_application.setVisible(False)
        self.ui.widget_manual.setVisible(False)
        self.ui.widget_servo.setVisible(False)
        self.ui.widget_plc.setVisible(True)
        self.ui.label_isnumber_upper.setVisible(False)
        self.ui.label_isnumber_lower.setVisible(False)

        # TableWidget_money属性设置
        self.ui.tableWidget_money.setEditTriggers(QTableWidget.NoEditTriggers)  # 不可编辑
        self.ui.tableWidget_money.setSelectionBehavior(QTableWidget.SelectRows)  # 单击选中一行

    def all_function(self):
        # 显示和影藏相应的菜单
        self.ui.pushButton_taxi.clicked.connect(self.widget_taxi_visible)
        self.ui.pushButton_application.clicked.connect(self.widget_application_visible)
        self.ui.pushButton_servo.clicked.connect(self.widget_manual_visible)
        self.ui.pushButton_manual.clicked.connect(self.widget_servo_visible)
        self.ui.pushButton_plc.clicked.connect(self.widget_plc_visible)
        # TAXI菜单中的功能
        self.ui.pushButton_taxi.clicked.connect(self.display_information)
        self.ui.pushButton_addname.clicked.connect(self.get_line_edit_name)
        self.ui.pushButton_addname.clicked.connect(self.add_name)
        self.ui.pushButton_addname.clicked.connect(self.display_information)
        self.ui.pushButton_money.clicked.connect(self.random_amount)
        self.ui.pushButton_money.clicked.connect(self.display_information)
        self.ui.lineEdit_upperlimit.textChanged.connect(self.get_line_edit_upper_limit)
        self.ui.lineEdit_upperlimit.textChanged.connect(self.str_to_upper_number)
        self.ui.lineEdit_lowerlimit.textChanged.connect(self.get_line_edit_lower_limit)
        self.ui.lineEdit_lowerlimit.textChanged.connect(self.str_to_lower_number)

    def display_information(self):
        """将Excel表格里的内容显示到QTableWidget"""
        self.taxi_data = HandleTaxiData.read_excel()
        for i in range(len(self.taxi_data)):
            table_widget_money_item = QTableWidgetItem()
            table_widget_money_item.setText(str(self.taxi_data[i][0]))
            self.ui.tableWidget_money.setItem(i, 0, table_widget_money_item)
        for i in range(len(self.taxi_data)):
            table_widget_money_item = QTableWidgetItem()
            table_widget_money_item.setText(str(self.taxi_data[i][1]))
            self.ui.tableWidget_money.setItem(i, 1, table_widget_money_item)

    def add_name(self):
        HandleTaxiData.append_name(self.get_add_name_text)

    def get_line_edit_name(self):
        self.get_add_name_text = self.ui.lineEdit_name.text()

    def get_line_edit_upper_limit(self):
        self.get_line_edit_upper_limit_text = self.ui.lineEdit_upperlimit.text()

    def get_line_edit_lower_limit(self):
        self.get_line_edit_lower_limit_text = self.ui.lineEdit_lowerlimit.text()
        print(self.get_line_edit_lower_limit_text)

    def str_to_upper_number(self):
        try:
            self.get_line_edit_upper_limit_int = int(self.get_line_edit_upper_limit_text)
            print(self.get_line_edit_upper_limit_int)
        except ValueError:
            self.ui.label_isnumber_upper.setVisible(True)
            self.ui.pushButton_money.setEnabled(False)
            print("出错啦 uu")
        else:
            self.ui.label_isnumber_upper.setVisible(False)
            self.ui.pushButton_money.setEnabled(True)

    def str_to_lower_number(self):
        try:
            self.get_line_edit_lower_limit_int = int(self.get_line_edit_lower_limit_text)
            print(self.get_line_edit_lower_limit_int)
        except ValueError:
            self.ui.label_isnumber_lower.setVisible(True)
            self.ui.pushButton_money.setEnabled(False)
            print("出错啦 LL")
        else:
            self.ui.label_isnumber_lower.setVisible(False)
            self.ui.pushButton_money.setEnabled(True)

    def random_amount(self):
        HandleTaxiData.random_invoice_amount(upper_limit=self.get_line_edit_upper_limit_int,
                                             lower_limit=self.get_line_edit_lower_limit_int)
        # import time
        # time.sleep(10) # 用于测试子线程
        # self.display_information()

    def widget_taxi_visible(self):
        self.ui.widget_taxi.setVisible(True)
        self.ui.widget_application.setVisible(False)
        self.ui.widget_manual.setVisible(False)
        self.ui.widget_servo.setVisible(False)
        self.ui.widget_plc.setVisible(False)

    def widget_application_visible(self):
        self.ui.widget_taxi.setVisible(False)
        self.ui.widget_application.setVisible(True)
        self.ui.widget_manual.setVisible(False)
        self.ui.widget_servo.setVisible(False)
        self.ui.widget_plc.setVisible(False)

    def widget_manual_visible(self):
        self.ui.widget_taxi.setVisible(False)
        self.ui.widget_application.setVisible(False)
        self.ui.widget_manual.setVisible(True)
        self.ui.widget_servo.setVisible(False)
        self.ui.widget_plc.setVisible(False)

    def widget_servo_visible(self):
        self.ui.widget_taxi.setVisible(False)
        self.ui.widget_application.setVisible(False)
        self.ui.widget_manual.setVisible(False)
        self.ui.widget_servo.setVisible(True)
        self.ui.widget_plc.setVisible(False)

    def widget_plc_visible(self):
        self.ui.widget_taxi.setVisible(False)
        self.ui.widget_application.setVisible(False)
        self.ui.widget_manual.setVisible(False)
        self.ui.widget_servo.setVisible(False)
        self.ui.widget_plc.setVisible(True)

    def sub_thread(self):
        sub = threading.Thread(target=self.random_amount)
        sub.start()


app = QApplication([])
office_system = OfficeSystem()
office_system.all_function()
office_system.ui.show()
app.exec()
