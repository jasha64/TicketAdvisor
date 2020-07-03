# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shishiku.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
all_train_detail = [
    ('1', '上海虹桥', '-', '19:00', '00:00', '0', 'G8'),
    ('2', '南京南', '20:07', '20:09', '01:07', '295', 'G8'),
    ('3', '北京南', '23:49', '23:49', '04:49', '1318', 'G8'),
]

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 450)
        Form.setWindowIcon(QtGui.QIcon('12306.png'))
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 581, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(82869)
        self.tableWidget.setColumnWidth(0, 105)  # 车次
        self.tableWidget.setColumnWidth(1, 43)  # 站序
        self.tableWidget.setColumnWidth(2, 82)  # 站名
        self.tableWidget.setColumnWidth(3, 48)  # 到时
        self.tableWidget.setColumnWidth(4, 48)  # 发时
        self.tableWidget.setColumnWidth(5, 48)  # 运行时间
        self.tableWidget.setColumnWidth(6, 43)  # 里程
        self.tableWidget.setHorizontalHeaderLabels(['车次', '站序', '站名', '到时', '发时', '运行时间', '里程'])
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.set_table_content(self.tableWidget, all_train_detail)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "全国铁路所有车次(按Ctrl+F查找)"))

    def set_table_content(self, table, data):
        table.setRowCount(len(data))
        for i in range(len(data)):
            table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(data[i][6])))
            for j in range(1, 7):
                table.setItem(i, j, QtWidgets.QTableWidgetItem(str(data[i][j-1])))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
