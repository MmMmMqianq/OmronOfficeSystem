# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TaxiUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Taxi(object):
    def setupUi(self, Taxi):
        Taxi.setObjectName("Taxi")
        Taxi.resize(1037, 908)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(Taxi)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
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
        self.numberEdit = QtWidgets.QLineEdit(Taxi)
        self.numberEdit.setObjectName("numberEdit")
        self.horizontalLayout_2.addWidget(self.numberEdit)
        self.addNameBtn = QtWidgets.QPushButton(Taxi)
        self.addNameBtn.setObjectName("addNameBtn")
        self.horizontalLayout_2.addWidget(self.addNameBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(Taxi)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(22)
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
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.previousBtn = QtWidgets.QPushButton(Taxi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previousBtn.sizePolicy().hasHeightForWidth())
        self.previousBtn.setSizePolicy(sizePolicy)
        self.previousBtn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.previousBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/arrows/previous2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previousBtn.setIcon(icon)
        self.previousBtn.setObjectName("previousBtn")
        self.horizontalLayout_4.addWidget(self.previousBtn)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.diLabel = QtWidgets.QLabel(Taxi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.diLabel.sizePolicy().hasHeightForWidth())
        self.diLabel.setSizePolicy(sizePolicy)
        self.diLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.diLabel.setObjectName("diLabel")
        self.horizontalLayout_3.addWidget(self.diLabel)
        self.pageNumberEdit = QtWidgets.QLineEdit(Taxi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pageNumberEdit.sizePolicy().hasHeightForWidth())
        self.pageNumberEdit.setSizePolicy(sizePolicy)
        self.pageNumberEdit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pageNumberEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pageNumberEdit.setPlaceholderText("")
        self.pageNumberEdit.setObjectName("pageNumberEdit")
        self.horizontalLayout_3.addWidget(self.pageNumberEdit)
        self.yeLabel = QtWidgets.QLabel(Taxi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yeLabel.sizePolicy().hasHeightForWidth())
        self.yeLabel.setSizePolicy(sizePolicy)
        self.yeLabel.setObjectName("yeLabel")
        self.horizontalLayout_3.addWidget(self.yeLabel)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.nextBtn = QtWidgets.QPushButton(Taxi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy)
        self.nextBtn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.nextBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/arrows/next2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextBtn.setIcon(icon1)
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout_4.addWidget(self.nextBtn)
        self.refreshBtn = QtWidgets.QPushButton(Taxi)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshBtn.sizePolicy().hasHeightForWidth())
        self.refreshBtn.setSizePolicy(sizePolicy)
        self.refreshBtn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.refreshBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refreshBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/arrows/loop2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshBtn.setIcon(icon2)
        self.refreshBtn.setIconSize(QtCore.QSize(14, 14))
        self.refreshBtn.setAutoDefault(False)
        self.refreshBtn.setObjectName("refreshBtn")
        self.horizontalLayout_4.addWidget(self.refreshBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(174, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(20, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
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
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.okButton = QtWidgets.QPushButton(Taxi)
        self.okButton.setObjectName("okButton")
        self.verticalLayout_2.addWidget(self.okButton)
        self.saveBtn = QtWidgets.QPushButton(Taxi)
        self.saveBtn.setObjectName("saveBtn")
        self.verticalLayout_2.addWidget(self.saveBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pathEdit = QtWidgets.QLineEdit(Taxi)
        self.pathEdit.setText("")
        self.pathEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pathEdit.setObjectName("pathEdit")
        self.horizontalLayout_5.addWidget(self.pathEdit)
        self.browseBtn = QtWidgets.QPushButton(Taxi)
        self.browseBtn.setObjectName("browseBtn")
        self.horizontalLayout_5.addWidget(self.browseBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 15)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.exportBtn = QtWidgets.QPushButton(Taxi)
        self.exportBtn.setObjectName("exportBtn")
        self.horizontalLayout_6.addWidget(self.exportBtn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(239, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)

        self.retranslateUi(Taxi)
        QtCore.QMetaObject.connectSlotsByName(Taxi)

    def retranslateUi(self, Taxi):
        _translate = QtCore.QCoreApplication.translate
        Taxi.setWindowTitle(_translate("Taxi", "Form"))
        self.nameLineEdit.setToolTip(_translate("Taxi", "姓名"))
        self.numberEdit.setPlaceholderText(_translate("Taxi", "份数:"))
        self.addNameBtn.setToolTip(_translate("Taxi", "添加姓名后请点击保存"))
        self.addNameBtn.setText(_translate("Taxi", "添加姓名"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Taxi", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Taxi", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Taxi", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Taxi", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Taxi", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Taxi", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Taxi", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Taxi", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Taxi", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Taxi", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Taxi", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Taxi", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Taxi", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Taxi", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Taxi", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Taxi", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Taxi", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("Taxi", "18"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("Taxi", "19"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("Taxi", "20"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("Taxi", "21"))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("Taxi", "22"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Taxi", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Taxi", "金额"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Taxi", "份数"))
        self.diLabel.setText(_translate("Taxi", "第"))
        self.pageNumberEdit.setText(_translate("Taxi", "1"))
        self.yeLabel.setText(_translate("Taxi", "页/共0条"))
        self.maximumLabel.setText(_translate("Taxi", "Max:"))
        self.maxValueSpinBox.setToolTip(_translate("Taxi", "输入最大值"))
        self.minimumLabel.setText(_translate("Taxi", "Min:"))
        self.minValueSpinBox.setToolTip(_translate("Taxi", "输入最小值"))
        self.okButton.setText(_translate("Taxi", "生成随机金额"))
        self.saveBtn.setText(_translate("Taxi", "保存"))
        self.pathEdit.setPlaceholderText(_translate("Taxi", "请选择保存路径"))
        self.browseBtn.setText(_translate("Taxi", "浏览"))
        self.exportBtn.setToolTip(_translate("Taxi", "请先选择文件保存路径"))
        self.exportBtn.setText(_translate("Taxi", "生成并导出表格"))