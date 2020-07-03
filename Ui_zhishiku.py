# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zhishiku.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

major_station_str = '''(
    # Wuhan Railway Bureau
    '武汉', '宜昌', '襄阳', '麻城',    '信阳',

    # Beijing
    '北京', '天津',
    '石家庄', '唐山', '秦皇岛', '山海关', '衡水', '邯郸',    '德州',

    # Shanghai
    '上海',
    '杭州', '金华', '宁波', '湖州', '温州',  # '衢州',
    '南京', '徐州', '苏州', '无锡',
    '合肥', '阜阳', '蚌埠', '芜湖', '六安', '铜陵', '安庆', '宣城',

    # Jinan
    '济南', '青岛', '淄博', '菏泽', '聊城', '曲阜', '枣庄',

    # Chengdu
    '成都', '达州',  # '广元',
    '重庆',
    '贵阳', '六盘水',

    # Kunming
    '昆明', '广通',

    # Zhengzhou
    '郑州', '洛阳', '商丘', '新乡', '焦作', '漯河',

    # Guangzhou Railway Group
    '长沙', '株洲', '怀化', '衡阳', '娄底',
    '广州', '深圳', '东莞', '潮汕', '韶关', '珠海',
    '海口', '三亚',

    # Shenyang
    '沈阳', '大连', '丹东', '本溪', '锦州',
    '长春', '吉林', '四平',    '通辽',

    # Harbin
    '哈尔滨', '齐齐哈尔', '牡丹江', '佳木斯',

    # Nanchang
    '南昌', '上饶', '鹰潭', '九江', '赣州', '吉安', '向塘',
    '福州', '厦门', '泉州', '莆田', '漳州', '三明', '龙岩',

    # Nanning
    '南宁', '柳州', '桂林',

    # Xi'an
    '西安', '宝鸡', '安康', '渭南',

    # Lanzhou
    '兰州', '天水', '武威',
    '银川',

    # Qinghai-Tibet Railway Company
    '西宁', '格尔木',
    '拉萨',

    # Urumqi
    '乌鲁木齐', '吐鲁番', '奎屯',

    # Taiyuan
    '太原', '大同', '长治',

    # Hohhot
    '呼和浩特', '包头', '临河', '集宁南',
)
'''


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 299)
        Form.setWindowIcon(QtGui.QIcon('12306.png'))  # added
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 381, 281))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "全国铁路枢纽城市列表"))

    def setContent(self, string):
        self.textEdit.setText(string)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    ui.setContent(major_station_str)
    MainWindow.show()
    sys.exit(app.exec_())