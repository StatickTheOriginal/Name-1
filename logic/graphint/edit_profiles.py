# Form implementation generated from reading ui file 'edit_profile.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Edit_profiles(object):
    def setupUi(self, Edit_profiles):
        Edit_profiles.setObjectName("Edit_profiles")
        Edit_profiles.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/Size=16, Type=Light.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Edit_profiles.setWindowIcon(icon)
        Edit_profiles.setStyleSheet("\n"
"\n"
"font: 12pt \"intel\";\n"
"background-color :#F6F6F6;\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=Edit_profiles)
        self.centralwidget.setStyleSheet("QPushButton {\n"
"    background-color:#E2E2E2;\n"
"    border-radius: 10px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D9D9D9;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_profile = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_profile.setGeometry(QtCore.QRect(12, 12, 349, 577))
        self.frame_profile.setStyleSheet("QFrame#frame_profile{\n"
"    background-color: #FFFFFF;\n"
"border: solid #D9D9D9;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"intel\";\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QCheckBox#checkBox_work_emulation{\n"
"    background-color: rgb(236, 236, 236);\n"
"}\n"
"")
        self.frame_profile.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_profile.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_profile.setObjectName("frame_profile")
        self.label_profile = QtWidgets.QLabel(parent=self.frame_profile)
        self.label_profile.setGeometry(QtCore.QRect(12, 12, 97, 25))
        self.label_profile.setObjectName("label_profile")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_profile)
        self.label_2.setGeometry(QtCore.QRect(12, 48, 73, 25))
        self.label_2.setStyleSheet("font: 9pt \"Calibri\";\n"
"color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.lineEdit_profile_name = QtWidgets.QLineEdit(parent=self.frame_profile)
        self.lineEdit_profile_name.setGeometry(QtCore.QRect(12, 84, 313, 37))
        self.lineEdit_profile_name.setStyleSheet("background-color: #FFFFFF;\n"
"border: solid #D9D9D9;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Calibri\";")
        self.lineEdit_profile_name.setObjectName("lineEdit_profile_name")
        self.label_comands_blueprint = QtWidgets.QLabel(parent=self.frame_profile)
        self.label_comands_blueprint.setGeometry(QtCore.QRect(12, 132, 133, 25))
        self.label_comands_blueprint.setStyleSheet("font: 9pt \"Calibri\";\n"
"color: rgb(0, 0, 0);")
        self.label_comands_blueprint.setObjectName("label_comands_blueprint")
        self.comboBox_params_type = QtWidgets.QComboBox(parent=self.frame_profile)
        self.comboBox_params_type.setGeometry(QtCore.QRect(12, 168, 313, 37))
        self.comboBox_params_type.setStyleSheet("background-color: #FFFFFF;\n"
"border: solid #D9D9D9;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Calibri\";")
        self.comboBox_params_type.setObjectName("comboBox_params_type")
        self.comboBox_params_type.addItem("")
        self.comboBox_params_type.addItem("")
        self.checkBox_work_emulation = QtWidgets.QCheckBox(parent=self.frame_profile)
        self.checkBox_work_emulation.setGeometry(QtCore.QRect(12, 216, 145, 37))
        self.checkBox_work_emulation.setStyleSheet("font: 9pt \"Calibri\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.checkBox_work_emulation.setObjectName("checkBox_work_emulation")
        self.pushButton_export = QtWidgets.QPushButton(parent=self.frame_profile)
        self.pushButton_export.setGeometry(QtCore.QRect(216, 528, 121, 37))
        self.pushButton_export.setStyleSheet("color: rgb(0, 0, 0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/upload.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_export.setIcon(icon1)
        self.pushButton_export.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_export.setObjectName("pushButton_export")
        self.pushButton_clone = QtWidgets.QPushButton(parent=self.frame_profile)
        self.pushButton_clone.setGeometry(QtCore.QRect(24, 528, 181, 37))
        self.pushButton_clone.setStyleSheet("color: rgb(0, 0, 0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/copy.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_clone.setIcon(icon2)
        self.pushButton_clone.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_clone.setObjectName("pushButton_clone")
        self.checkBox_EOL_str_end = QtWidgets.QCheckBox(parent=self.frame_profile)
        self.checkBox_EOL_str_end.setGeometry(QtCore.QRect(12, 252, 181, 37))
        self.checkBox_EOL_str_end.setStyleSheet("font: 9pt \"Calibri\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.checkBox_EOL_str_end.setCheckable(True)
        self.checkBox_EOL_str_end.setChecked(True)
        self.checkBox_EOL_str_end.setObjectName("checkBox_EOL_str_end")
        self.frame_list_com = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_list_com.setGeometry(QtCore.QRect(384, 12, 877, 577))
        self.frame_list_com.setStyleSheet("QFrame#frame_list_com{\n"
"    background-color: #FFFFFF;\n"
"border: solid #D9D9D9;\n"
"border-width: 1px;\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"intel\";\n"
"    \n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"    background-color: rgb(236, 236, 236);\n"
"}\n"
"\n"
"QCheckBox#checkBox_work_emulation{\n"
"    background-color: rgb(236, 236, 236);\n"
"}\n"
"")
        self.frame_list_com.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_list_com.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_list_com.setObjectName("frame_list_com")
        self.label_com_list = QtWidgets.QLabel(parent=self.frame_list_com)
        self.label_com_list.setGeometry(QtCore.QRect(24, 12, 109, 25))
        self.label_com_list.setStyleSheet("font: 9pt \"Calibri\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.label_com_list.setObjectName("label_com_list")
        self.lineEdit_commands = QtWidgets.QLineEdit(parent=self.frame_list_com)
        self.lineEdit_commands.setGeometry(QtCore.QRect(24, 48, 313, 37))
        self.lineEdit_commands.setStyleSheet("background-color: #FFFFFF;\n"
"border: solid #D9D9D9;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Calibri\";")
        self.lineEdit_commands.setObjectName("lineEdit_commands")
        self.pushButton_add_command = QtWidgets.QPushButton(parent=self.frame_list_com)
        self.pushButton_add_command.setGeometry(QtCore.QRect(632, 24, 217, 49))
        self.pushButton_add_command.setStyleSheet("color: rgb(0, 0, 0);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/add.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_add_command.setIcon(icon3)
        self.pushButton_add_command.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_add_command.setObjectName("pushButton_add_command")
        self.listView_commands = QtWidgets.QListView(parent=self.frame_list_com)
        self.listView_commands.setGeometry(QtCore.QRect(24, 96, 829, 457))
        self.listView_commands.setStyleSheet("background-color: rgb(200, 200, 200);\n"
"font: 14pt \"Calibri\";\n"
"background-color: #FFFFFF;\n"
"border: solid #D9D9D9;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Calibri\";")
        self.listView_commands.setObjectName("listView_commands")
        self.frame_ok_canc = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_ok_canc.setGeometry(QtCore.QRect(12, 607, 1249, 97))
        self.frame_ok_canc.setStyleSheet("QFrame#frame_ok_canc{\n"
"    background-color: #FFFFFF;\n"
"    border-radius: 10px\n"
"}\n"
"\n"
"")
        self.frame_ok_canc.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_ok_canc.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_ok_canc.setObjectName("frame_ok_canc")
        self.pushButton_cancel = QtWidgets.QPushButton(parent=self.frame_ok_canc)
        self.pushButton_cancel.setGeometry(QtCore.QRect(1104, 24, 133, 49))
        self.pushButton_cancel.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_ok = QtWidgets.QPushButton(parent=self.frame_ok_canc)
        self.pushButton_ok.setGeometry(QtCore.QRect(948, 24, 133, 49))
        self.pushButton_ok.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_ok.setObjectName("pushButton_ok")
        Edit_profiles.setCentralWidget(self.centralwidget)

        self.retranslateUi(Edit_profiles)
        QtCore.QMetaObject.connectSlotsByName(Edit_profiles)

    def retranslateUi(self, Edit_profiles):
        _translate = QtCore.QCoreApplication.translate
        Edit_profiles.setWindowTitle(_translate("Edit_profiles", "EditProfiles"))
        self.label_profile.setText(_translate("Edit_profiles", "Профиль"))
        self.label_2.setText(_translate("Edit_profiles", "Название:"))
        self.label_comands_blueprint.setText(_translate("Edit_profiles", "Шаблон команды:"))
        self.comboBox_params_type.setItemText(0, _translate("Edit_profiles", "<Команда>.<Параметр>"))
        self.comboBox_params_type.setItemText(1, _translate("Edit_profiles", "<Команда>"))
        self.checkBox_work_emulation.setText(_translate("Edit_profiles", "Эмуляция работы"))
        self.pushButton_export.setText(_translate("Edit_profiles", "Экспорт"))
        self.pushButton_clone.setText(_translate("Edit_profiles", "Клонировать"))
        self.checkBox_EOL_str_end.setText(_translate("Edit_profiles", "Ожидание конца строки"))
        self.label_com_list.setText(_translate("Edit_profiles", "Список команд"))
        self.lineEdit_commands.setInputMask(_translate("Edit_profiles", "Поиск"))
        self.pushButton_add_command.setText(_translate("Edit_profiles", "Добавить команду"))
        self.pushButton_cancel.setText(_translate("Edit_profiles", "Отмена"))
        self.pushButton_ok.setText(_translate("Edit_profiles", "ОК"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Edit_profiles = QtWidgets.QMainWindow()
    ui = Ui_Edit_profiles()
    ui.setupUi(Edit_profiles)
    Edit_profiles.show()
    sys.exit(app.exec())
