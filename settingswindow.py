from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from functions import *

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(600, 320)
        SettingsWindow.setMinimumSize(QtCore.QSize(600, 320))
        SettingsWindow.setMaximumSize(QtCore.QSize(600, 320))
        SettingsWindow.setWindowIcon(QtGui.QIcon('img/icon.png'))
        SettingsWindow.setStyleSheet("QMainWindow {\n"
"    background-color: white;\n"
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
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(178, 99, 252, 255), stop:0.5 rgba(251, 162, 213, 255), stop:1 rgba(182, 242, 221, 255));\n"
"}\n"
".QPushButton:hover {\n"
"    font-size: 12px;\n"
"}\n"
".QListWidget {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(178, 99, 252, 100), stop:0.5 rgba(251, 162, 213, 100), stop:1 rgba(182, 242, 221, 100));\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
".QLabel {\n"
"    font-size: 13px;\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(178, 99, 252, 100), stop:0.5 rgba(251, 162, 213, 100), stop:1 rgba(182, 242, 221, 100));\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
".labelPathToSteam {\n"
"    padding-left: 12px;\n"
"}\n"
"\n"
".QLineEdit {\n"
"    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(178, 99, 252, 100), stop:0.5 rgba(251, 162, 213, 100), stop:1 rgba(182, 242, 221, 100));\n"
"    border-radius: 8px;\n"
"    padding-left: 12px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")

        self.gomainwin = QtWidgets.QPushButton(self.centralwidget)
        self.gomainwin.setGeometry(QtCore.QRect(20, 20, 561, 41))
        self.gomainwin.setStyleSheet("")
        self.gomainwin.setObjectName("gomainwin")

        self.linePathToSteam = QtWidgets.QLineEdit(self.centralwidget)
        self.linePathToSteam.setGeometry(QtCore.QRect(230, 140, 351, 41))
        self.linePathToSteam.setText("")
        self.linePathToSteam.setObjectName("linePathToSteam")

        self.labelPathToSteam = QtWidgets.QLabel(self.centralwidget)
        self.labelPathToSteam.setGeometry(QtCore.QRect(20, 140, 191, 41))
        self.labelPathToSteam.setAlignment(QtCore.Qt.AlignCenter)
        self.labelPathToSteam.setObjectName("labelPathToSteam")

        self.langSteamRU = QtWidgets.QPushButton(self.centralwidget)
        self.langSteamRU.setGeometry(QtCore.QRect(230, 80, 161, 41))
        self.langSteamRU.setStyleSheet("")
        self.langSteamRU.setObjectName("langSteamRU")

        self.langSteamEN = QtWidgets.QPushButton(self.centralwidget)
        self.langSteamEN.setGeometry(QtCore.QRect(410, 80, 171, 41))
        self.langSteamEN.setStyleSheet("")
        self.langSteamEN.setObjectName("langSteamEN")

        self.labelLangSteam = QtWidgets.QLabel(self.centralwidget)
        self.labelLangSteam.setGeometry(QtCore.QRect(20, 80, 191, 41))
        self.labelLangSteam.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLangSteam.setObjectName("labelLangSteam")

        self.addServersButton = QtWidgets.QPushButton(self.centralwidget)
        self.addServersButton.setGeometry(QtCore.QRect(20, 260, 191, 41))
        self.addServersButton.setStyleSheet("")
        self.addServersButton.setObjectName("addServersButton")

        self.cfgRedactorButton = QtWidgets.QPushButton(self.centralwidget)
        self.cfgRedactorButton.setGeometry(QtCore.QRect(20, 200, 561, 41))
        self.cfgRedactorButton.setStyleSheet("")
        self.cfgRedactorButton.setObjectName("cfgRedactorButton")

        self.serverLabel = QtWidgets.QLabel(self.centralwidget)
        self.serverLabel.setGeometry(QtCore.QRect(230, 260, 351, 41))
        self.serverLabel.setText("")
        self.serverLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.serverLabel.setObjectName("serverLabel")

        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

        self.goMainF()
        self.ChangeLangF()
        self.ChangePath()

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Obl1Que\'s Panel CS:GO"))
        self.gomainwin.setText(_translate("SettingsWindow", "СОХРАНИТЬ НАСТРОЙКИ И ВЫЙТИ"))
        self.labelPathToSteam.setText(_translate("SettingsWindow", "ПУТЬ ДО STEAM:"))
        self.langSteamRU.setText(_translate("SettingsWindow", "РУССКИЙ"))
        self.langSteamEN.setText(_translate("SettingsWindow", "ENGLISH"))
        self.labelLangSteam.setText(_translate("SettingsWindow", "ЯЗЫК КЛИЕНТА STEAM:"))
        self.addServersButton.setText(_translate("SettingsWindow", "ДОБАВИТЬ СЕРВЕР"))
        self.cfgRedactorButton.setText(_translate("SettingsWindow", "РЕДАКТИРОВАТЬ ФАЙЛ КОНФИГА"))

    def goMainF(self):
        self.gomainwin.clicked.connect(lambda: self.goMain())
    def goMain(self):
        info = readJson("settings/settings.json")
        info["steam_path"] = self.linePathToSteam.text()
        file = open("settings/settings.json", "w", encoding="utf-8")
        file.write(json.dumps(info, indent=4, ensure_ascii=False))
        file.close()
        self.SettingsWindow.close()

    def ChangeLangF(self):
        self.langSteamRU.clicked.connect(lambda: self.ChangeLang(self.langSteamRU.text()))
        self.langSteamEN.clicked.connect(lambda: self.ChangeLang(self.langSteamEN.text()))
    def ChangeLang(self, butText):
        info = readJson('settings/settings.json')
        info["steam_language"] = butText.lower()
        file = open('settings/settings.json', 'w', encoding='utf-8')
        file.write(json.dumps(info, indent=4, ensure_ascii=False))
        file.close()
        print(f'Язык изменён на {butText}')
    def ChangePath(self):
        self.linePathToSteam.setText(readJson("settings/settings.json")["steam_path"])