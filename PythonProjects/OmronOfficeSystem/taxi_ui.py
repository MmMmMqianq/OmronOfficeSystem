# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taxi_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Taxi(object):
    def setupUi(self, Taxi):
        Taxi.setObjectName("Taxi")
        Taxi.resize(749, 615)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(Taxi)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(12, -1, 12, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nameLineEdit = QtWidgets.QLineEdit(Taxi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLineEdit.sizePolicy().hasHeightForWidth())
        self.nameLineEdit.setSizePolicy(sizePolicy)
        self.nameLineEdit.setText("")
        self.nameLineEdit.setPlaceholderText("请输入姓名：")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.horizontalLayout_2.addWidget(self.nameLineEdit)
        self.addNameButton = QtWidgets.QPushButton(Taxi)
        self.addNameButton.setToolTip("")
        self.addNameButton.setObjectName("addNameButton")
        self.horizontalLayout_2.addWidget(self.addNameButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(Taxi)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(18)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.maximumLabel = QtWidgets.QLabel(Taxi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maximumLabel.sizePolicy().hasHeightForWidth())
        self.maximumLabel.setSizePolicy(sizePolicy)
        self.maximumLabel.setObjectName("maximumLabel")
        self.gridLayout.addWidget(self.maximumLabel, 1, 0, 1, 1)
        self.maxValueSpinBox = QtWidgets.QSpinBox(Taxi)
        self.maxValueSpinBox.setMaximum(399)
        self.maxValueSpinBox.setProperty("value", 399)
        self.maxValueSpinBox.setObjectName("maxValueSpinBox")
        self.gridLayout.addWidget(self.maxValueSpinBox, 1, 1, 1, 1)
        self.minimumLabel = QtWidgets.QLabel(Taxi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimumLabel.sizePolicy().hasHeightForWidth())
        self.minimumLabel.setSizePolicy(sizePolicy)
        self.minimumLabel.setObjectName("minimumLabel")
        self.gridLayout.addWidget(self.minimumLabel, 0, 0, 1, 1)
        self.minValueSpinBox = QtWidgets.QSpinBox(Taxi)
        self.minValueSpinBox.setMaximum(399)
        self.minValueSpinBox.setProperty("value", 350)
        self.minValueSpinBox.setObjectName("minValueSpinBox")
        self.gridLayout.addWidget(self.minValueSpinBox, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.okButton = QtWidgets.QPushButton(Taxi)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Taxi)
        QtCore.QMetaObject.connectSlotsByName(Taxi)

    def retranslateUi(self, Taxi):
        _translate = QtCore.QCoreApplication.translate
        Taxi.setWindowTitle(_translate("Taxi", "Form"))
        self.nameLineEdit.setToolTip(_translate("Taxi", "姓名"))
        self.addNameButton.setText(_translate("Taxi", "添加姓名"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Taxi", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Taxi", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Taxi", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Taxi", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Taxi", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Taxi", "5"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Taxi", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Taxi", "7"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Taxi", "8"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Taxi", "9"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Taxi", "10"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Taxi", "11"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Taxi", "12"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Taxi", "13"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Taxi", "14"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Taxi", "15"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Taxi", "16"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Taxi", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Taxi", "金额"))
        self.maximumLabel.setText(_translate("Taxi", "Max:"))
        self.maxValueSpinBox.setToolTip(_translate("Taxi", "输入最大值"))
        self.minimumLabel.setText(_translate("Taxi", "Min:"))
        self.minValueSpinBox.setToolTip(_translate("Taxi", "输入最小值"))
        self.okButton.setText(_translate("Taxi", "生成随机金额"))
