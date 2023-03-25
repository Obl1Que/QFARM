from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from functions import *
import autoit
import time

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(700, 495)
        SettingsWindow.setMinimumSize(QtCore.QSize(700, 495))
        SettingsWindow.setMaximumSize(QtCore.QSize(700, 495))
        SettingsWindow.setWindowIcon(QtGui.QIcon('img/icon.png'))
        SettingsWindow.setStyleSheet("QMainWindow {\n"
                                     "    background-color: dim-gray;\n"
                                     "}")
        self.SettingsWindow = SettingsWindow

        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setStyleSheet(".QPushButton {\n"
                                         "    border: 0 solid;\n"
                                         "    border-radius: 8px;\n"
                                         "    color: white;\n"
                                         "    font-size: 13px;\n"
                                         "    font-weight: bold;\n"
                                         "    \n"
                                         "    background-color: rgba(79, 79, 79, 1);\n"
                                         "}\n"
                                         ".QPushButton:hover {\n"
                                         "    font-size: 12px;\n"
                                         "}\n"
                                         ".QListWidget {\n"
                                         "    color: white;\n"
                                         "    background-color: rgba(79, 79, 79, 1);\n"
                                         "    border-radius: 8px;\n"
                                         "}\n"
                                         "\n"
                                         ".QLabel {\n"
                                         "    font-size: 13px;\n"
                                         "    background-color: rgba(79, 79, 79, 1);\n"
                                         "    border-radius: 8px;\n"
                                         "}\n"
                                         "\n"
                                         ".labelPathToSteam {\n"
                                         "    padding-left: 12px;\n"
                                         "}\n"
                                         "\n"
                                         ".QLineEdit {\n"
                                         "    background-color: rgba(79, 79, 79, 1);\n"
                                         "    border-radius: 8px;\n"
                                         "    padding-left: 12px;\n"
                                         "}")
        self.centralwidget.setObjectName("centralwidget")

        self.gomainwin = QtWidgets.QPushButton(self.centralwidget)
        self.gomainwin.setGeometry(QtCore.QRect(20, 20, 661, 41))
        self.gomainwin.setStyleSheet("")
        self.gomainwin.setObjectName("gomainwin")

        self.linePathToSteam = QtWidgets.QLineEdit(self.centralwidget)
        self.linePathToSteam.setGeometry(QtCore.QRect(230, 140, 451, 41))
        self.linePathToSteam.setText("")
        self.linePathToSteam.setObjectName("linePathToSteam")

        self.labelPathToSteam = QtWidgets.QLabel(self.centralwidget)
        self.labelPathToSteam.setGeometry(QtCore.QRect(20, 140, 191, 41))
        self.labelPathToSteam.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPathToSteam.setObjectName("labelPathToSteam")

        self.linePathToCSGO = QtWidgets.QLineEdit(self.centralwidget)
        self.linePathToCSGO.setGeometry(QtCore.QRect(230, 380, 451, 41))
        self.linePathToCSGO.setText("")
        self.linePathToCSGO.setObjectName("linePathToCSGO")

        self.labelPathToCSGO = QtWidgets.QLabel(self.centralwidget)
        self.labelPathToCSGO.setGeometry(QtCore.QRect(20, 380, 191, 41))
        self.labelPathToCSGO.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPathToCSGO.setObjectName("labelPathToCSGO")

        self.linePathToServer = QtWidgets.QLineEdit(self.centralwidget)
        self.linePathToServer.setGeometry(QtCore.QRect(230, 80, 451, 41))
        self.linePathToServer.setText("")
        self.linePathToServer.setObjectName("linePathToServer")

        self.labelPathToServer = QtWidgets.QLabel(self.centralwidget)
        self.labelPathToServer.setGeometry(QtCore.QRect(20, 80, 191, 41))
        self.labelPathToServer.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPathToServer.setObjectName("labelPathToServer")

        self.linePathToServerparametrs = QtWidgets.QLineEdit(self.centralwidget)
        self.linePathToServerparametrs.setGeometry(QtCore.QRect(230, 440, 451, 41))
        self.linePathToServerparametrs.setText("")
        self.linePathToServerparametrs.setObjectName("linePathToServerparametrs")

        self.labelPathToServerparametrs = QtWidgets.QLabel(self.centralwidget)
        self.labelPathToServerparametrs.setGeometry(QtCore.QRect(20, 440, 191, 41))
        self.labelPathToServerparametrs.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPathToServerparametrs.setObjectName("labelPathToServerparametrs")

        self.addServersButton = QtWidgets.QLabel(self.centralwidget)
        self.addServersButton.setGeometry(QtCore.QRect(20, 260, 191, 41))
        self.addServersButton.setAlignment(QtCore.Qt.AlignCenter)
        self.addServersButton.setObjectName("addServersButton")

        self.linePathToMemreduct = QtWidgets.QLineEdit(self.centralwidget)
        self.linePathToMemreduct.setGeometry(QtCore.QRect(230, 320, 451, 41))
        self.linePathToMemreduct.setText("")
        self.linePathToMemreduct.setObjectName("linePathToMemreduct")

        self.labelPathToMemreduct = QtWidgets.QLabel(self.centralwidget)
        self.labelPathToMemreduct.setGeometry(QtCore.QRect(20, 320, 191, 41))
        self.labelPathToMemreduct.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPathToMemreduct.setObjectName("labelPathToMemreduct")

        self.cfgRedactorButton = QtWidgets.QPushButton("Toggle",self.centralwidget)
        self.cfgRedactorButton.setCheckable(True)
        self.cfgRedactorButton.setGeometry(QtCore.QRect(20, 200, 661, 41))
        self.cfgRedactorButton.setStyleSheet("")
        self.cfgRedactorButton.setObjectName("cfgRedactorButton")

        self.serverLabel = QtWidgets.QLineEdit(self.centralwidget)
        self.serverLabel.setGeometry(QtCore.QRect(230, 260, 451, 41))
        self.serverLabel.setText("")
        self.serverLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.serverLabel.setObjectName("serverLabel")

        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

        self.goMainF()
        self.ChangePath()
        self.ExecConfigure()
        self.cfgRedactorF()

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Obl1Que\'s Panel CS:GO"))
        self.gomainwin.setText(_translate("SettingsWindow", "СОХРАНИТЬ НАСТРОЙКИ И ВЫЙТИ"))
        self.labelPathToSteam.setText(_translate("SettingsWindow", "ПУТЬ ДО STEAM:"))
        self.labelPathToCSGO.setText(_translate("SettingsWindow", "ПУТЬ ДО CSGO:"))
        self.labelPathToServer.setText(_translate("SettingsWindow", "ПУТЬ ДО СЕРВЕРА:"))
        self.labelPathToServerparametrs.setText(_translate("SettingsWindow", "ПАРАМЕТРЫ СЕРВЕРА:"))
        self.labelPathToMemreduct.setText(_translate("SettingsWindow", "ПУТЬ ДО MEMREDUCT:"))
        self.addServersButton.setText(_translate("SettingsWindow", "ДОБАВИТЬ СЕРВЕР"))
        self.cfgRedactorButton.setText(_translate("SettingsWindow", "РЕДАКТИРОВАТЬ ФАЙЛ КОНФИГА"))

    def goMainF(self):
        self.gomainwin.clicked.connect(lambda: self.goMain())
    def goMain(self):
        info = readJson("settings/settings.json")
        info["steam_path"] = self.linePathToSteam.text()
        info["csgo_path"] = self.linePathToCSGO.text()
        info["server_path"] = self.linePathToServer.text()
        info["server_parametrs"] = self.linePathToServerparametrs.text()
        info["server_log_pass"] = self.serverLabel.text()
        info["memreduct_path"] = self.linePathToMemreduct.text()
        file = open("settings/settings.json", "w", encoding="utf-8")
        file.write(json.dumps(info, indent=4, ensure_ascii=False))
        file.close()
        self.SettingsWindow.close()
    def ChangePath(self):
        self.linePathToSteam.setText(readJson("settings/settings.json")["steam_path"])
        self.linePathToServer.setText(readJson("settings/settings.json")["server_path"])
        self.linePathToServerparametrs.setText(readJson("settings/settings.json")["server_parametrs"])
        self.linePathToMemreduct.setText(readJson("settings/settings.json")["memreduct_path"])
        self.linePathToCSGO.setText(readJson("settings/settings.json")["csgo_path"])
        self.serverLabel.setText(readJson("settings/settings.json")["server_log_pass"])

    def ExecConfigure(self):
        self.cfgRedactorButton.clicked.connect(lambda: self.ExecConfigureF())

    def ExecConfigureF(self):
        path_to_cfg = os.path.abspath("settings/qfarm.cfg")
        os.system(path_to_cfg)
        self.linePathToMemreduct.setText(readJson("settings/settings.json")["memreduct_path"])
    def cfgRedactorF(self):
        self.cfgRedactorButton.clicked.connect(lambda: self.cfgRedactor())
    def cfgRedactor(self):
        if self.cfgRedactorButton.isChecked() == False:
            autoit.run('pssuspend steamwebhelper')
            n = 1
            while n < 6:
                self.suspend()
                time.sleep(45)
                self.unsuspend()
                time.sleep(3)
        else:
            autoit.run('pssuspend -r steamwebhelper')
            n = 7
            self.unsuspend()

    def suspend(self):
        autoit.run('pssuspend Steam')
        autoit.run('pssuspend csgo')

    def unsuspend(self):
        autoit.run('pssuspend -r Steam')
        autoit.run('pssuspend -r csgo')