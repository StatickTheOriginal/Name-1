# Form implementation generated from reading ui file 'help_list.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_help_list_window(object):
    def setupUi(self, help_list_window):
        help_list_window.setObjectName("help_list_window")
        help_list_window.resize(1280, 720)
        help_list_window.setStyleSheet("font: 14pt \"Calibri\";\n"
"background-color: #F6F6F6;")
        self.centralwidget = QtWidgets.QWidget(parent=help_list_window)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(12, 72, 1261, 541))
        self.listWidget.setStyleSheet("background-color: #FFFFFF;")
        self.listWidget.setObjectName("listWidget")
        self.label_hotkeys = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_hotkeys.setGeometry(QtCore.QRect(528, 12, 181, 49))
        self.label_hotkeys.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_hotkeys.setObjectName("label_hotkeys")
        self.frame_ok = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_ok.setGeometry(QtCore.QRect(12, 636, 1261, 80))
        self.frame_ok.setStyleSheet("QFrame#frame_ok{\n"
"    border-color: #EBEBEB;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #D9D9D9;\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200);\n"
"}")
        self.frame_ok.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_ok.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_ok.setObjectName("frame_ok")
        self.ok_button = QtWidgets.QPushButton(parent=self.frame_ok)
        self.ok_button.setGeometry(QtCore.QRect(1104, 12, 150, 60))
        self.ok_button.setStyleSheet("color: rgb(0, 0, 0);")
        self.ok_button.setObjectName("ok_button")
        help_list_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(help_list_window)
        QtCore.QMetaObject.connectSlotsByName(help_list_window)

    def retranslateUi(self, help_list_window):
        _translate = QtCore.QCoreApplication.translate
        help_list_window.setWindowTitle(_translate("help_list_window", "MainWindow"))
        self.label_hotkeys.setText(_translate("help_list_window", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Горячие клавиши</span></p></body></html>"))
        self.ok_button.setText(_translate("help_list_window", "ОК"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    help_list_window = QtWidgets.QMainWindow()
    ui = Ui_help_list_window()
    ui.setupUi(help_list_window)
    help_list_window.show()
    sys.exit(app.exec())