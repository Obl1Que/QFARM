import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from functions import *
from settingswindow import Ui_SettingsWindow
from PyQt5.QtWidgets import *
import threading
import autoit
import os
import re
import win32gui
import win32con





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.itemsToLaunch = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("QMainWindow {"
                                 "background-color: dim-gray;"
                                 "}")
        self.MainWindow = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QPushButton {"
                                         "border: 0 solid;"
                                         "border-radius: 8px;"
                                         "color: white;"
                                         "font-size: 11px;"
                                         "font-weight: bold;"
                                         "background-color: rgba(79, 79, 79, 1);"
                                         "}"
                                         ".QPushButton:hover {"
                                         "font-size: 14px;"
                                         "}"
                                         ".QListWidget {"
                                         "    background-color: rgba(79, 79, 79, 1);\n"
                                         "color: white;"
                                         "    border-radius: 8px}")
        self.centralwidget.setObjectName("centralwidget")

        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        self.settingsButton.setGeometry(QtCore.QRect(20, 260, 141, 41))
        self.settingsButton.setStyleSheet("")
        self.settingsButton.setObjectName("settingsButton")

        self.optimiseButton = QtWidgets.QPushButton(self.centralwidget)
        self.optimiseButton.setGeometry(QtCore.QRect(180, 260, 141, 41))
        self.optimiseButton.setStyleSheet("")
        self.optimiseButton.setObjectName("optimiseButton")

        self.windowsButton = QtWidgets.QPushButton(self.centralwidget)
        self.windowsButton.setGeometry(QtCore.QRect(340, 260, 81, 41))
        self.windowsButton.setStyleSheet("")
        self.windowsButton.setObjectName("windowsButton")
        self.windowsButton.setIcon(QtGui.QIcon('img/win_icon.png'))
        self.windowsButton.setIconSize(QtCore.QSize(20, 20))

        self.checkAccountsButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkAccountsButton.setGeometry(QtCore.QRect(20, 20, 401, 41))
        self.checkAccountsButton.setStyleSheet("")
        self.checkAccountsButton.setObjectName("checkAccountsButton")

        self.allAccountsButton = QtWidgets.QPushButton(self.centralwidget)
        self.allAccountsButton.setGeometry(QtCore.QRect(430, 140, 140, 41))
        self.allAccountsButton.setStyleSheet("")
        self.allAccountsButton.setObjectName("allAccountsButton")

        self.addAccountsButton = QtWidgets.QPushButton(self.centralwidget)
        self.addAccountsButton.setGeometry(QtCore.QRect(20, 80, 401, 41))
        self.addAccountsButton.setStyleSheet("")
        self.addAccountsButton.setObjectName("addAccountsButton")

        self.addMaFilesButton = QtWidgets.QPushButton(self.centralwidget)
        self.addMaFilesButton.setGeometry(QtCore.QRect(20, 140, 401, 41))
        self.addMaFilesButton.setStyleSheet("")
        self.addMaFilesButton.setObjectName("addMaFilesButton")

        self.startFarmButton = QtWidgets.QPushButton(self.centralwidget)
        self.startFarmButton.setGeometry(QtCore.QRect(20, 200, 401, 41))
        self.startFarmButton.setStyleSheet("")
        self.startFarmButton.setObjectName("startFarm")

        self.accountsList = QtWidgets.QListWidget(self.centralwidget)
        self.accountsList.setGeometry(QtCore.QRect(575, 21, 200, 281))
        self.accountsList.setObjectName("accountsList")

        self.logList = QtWidgets.QListWidget(self.centralwidget)
        self.logList.setGeometry(QtCore.QRect(25, 380, 751, 201))
        self.logList.setObjectName("logList")

        self.eyeButton = QPushButton("Toggle", self.centralwidget)
        self.eyeButton.setCheckable(True)
        self.eyeButton.setGeometry(QtCore.QRect(430, 80, 140, 41))
        self.eyeButton.setStyleSheet("")
        self.eyeButton.setObjectName("eye")
        self.eyeButton.clicked.connect(self.do_something)
        self.eyeButton.setStyleSheet("font-size: 14px;")

        self.batButton = QPushButton("Toggle", self.centralwidget)
        self.batButton.setCheckable(True)
        self.batButton.setGeometry(QtCore.QRect(430, 20, 140, 41))
        self.batButton.setStyleSheet("")
        self.batButton.setObjectName("bat")

        self.killButton = QPushButton("Toggle", self.centralwidget)
        self.killButton.setCheckable(True)
        self.killButton.setGeometry(QtCore.QRect(430, 260, 140, 41))
        self.killButton.setStyleSheet("")
        self.killButton.setObjectName("kill")

        self.clearButton = QPushButton("Toggle", self.centralwidget)
        self.clearButton.setCheckable(True)
        self.clearButton.setGeometry(QtCore.QRect(430, 200, 140, 41))
        self.clearButton.setStyleSheet("")
        self.clearButton.setObjectName("clear")

        self.hideButton = QPushButton("Toggle", self.centralwidget)
        self.hideButton.setCheckable(True)
        self.hideButton.setGeometry(QtCore.QRect(20, 320, 141, 41))
        self.hideButton.setStyleSheet("")
        self.hideButton.setObjectName("hideButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.checkAccounts()
        self.addAccountsF()
        self.addMaFilesF()
        self.checkAccountsF()
        self.chooseItems()
        self.startFarmF()
        self.ReWindowF()
        self.goSettingsF()
        self.OptimiseF()
        self.chooseAllItems()
        self.batF()
        self.killa()
        self.hidea()
        self.clearF()
        self.blur_effect = QGraphicsBlurEffect()
        self.accountsList.setGraphicsEffect(self.blur_effect)

        self.LogWrite(OnStartPrintInfo())
        self.itemsToLaunch = []
        self.opt_stat = False
        self.rew_stat = False
        self.start_stat = False
        self.add_acc_stat = False
        self.all_accs_choosen = False

    def StartFarmT(self):
        try:
            if self.start_stat == False:
                t1 = threading.Thread(target=self.startFarm, daemon=True)
                t1.start()
            else:
                thCh = threading.Thread(target=self.checkAccounts, daemon=True)
                thCh.start()
                self.LogWrite("Панель уже запускает аккаунты!")
        except:
            t1 = threading.Thread(target=self.startFarm, daemon=True)
            t1.start()

    def ReWindowT(self):
        if self.rew_stat == False:
            t2 = threading.Thread(target=self.ReWindow, daemon=True)
            t2.start()
        else:
            self.LogWrite("Панель уже перемещает аккаунты!")

    def addMaFilesT(self):
        th = threading.Thread(target=self.addMaFiles, daemon=True)
        th.start()

    def addAccountsT(self):
        if self.add_acc_stat == False:
            th = threading.Thread(target=self.addAccounts, daemon=True)
            th.start()
        else:
            self.LogWrite("Файл logpass.txt уже запущен!")
    def goSettingsF(self):
        self.settingsButton.clicked.connect(lambda: self.goSettings())
    def goSettings(self):
        self.SettingsWindow = QtWidgets.QMainWindow()
        ui = Ui_SettingsWindow()
        ui.setupUi(self.SettingsWindow)
        self.SettingsWindow.show()

    def retranslateUi(self, MainWindow):
        self.need_update = GetActualVersion()
        _translate = QtCore.QCoreApplication.translate

        if self.need_update[0]:
            self.LogWrite(f"ДОСТУПНА НОВАЯ ВЕРСИЯ ПАНЕЛИ ({readJson('settings/settings.json')['version']} --> {self.need_update[1]}) ДЛЯ СКАЧИВАНИЯ!\n"
                          f"ПЕРЕХОДИ ПО ССЫЛКЕ ЧТОБЫ СКАЧАТЬ: https://github.com/Obl1Que/QFARM")
            MainWindow.setWindowTitle(_translate("MainWindow", f"QFARM {readJson('settings/settings.json')['version']} | Obl1Que | ВОЗМОЖНО ОБНОВЛЕНИЕ ДО {self.need_update[1]}"))
        else:
            MainWindow.setWindowTitle(_translate("MainWindow", f"QFARM {readJson('settings/settings.json')['version']} | Obl1Que"))
        self.settingsButton.setText(_translate("MainWindow", "НАСТРОЙКИ"))
        self.optimiseButton.setText(_translate("MainWindow", "ОПТИМИЗИРОВАТЬ"))
        self.windowsButton.setText(_translate("MainWindow", ""))
        self.allAccountsButton.setText(_translate("MainWindow", "ВЫБРАТЬ ВСЕ"))
        self.checkAccountsButton.setText(_translate("MainWindow", "ПРОВЕРКА АККАУНТОВ"))
        self.addAccountsButton.setText(_translate("MainWindow", "ДОБАВИТЬ АККАУНТЫ"))
        self.addMaFilesButton.setText(_translate("MainWindow", "ДОБАВИТЬ MAFILE"))
        self.startFarmButton.setText(_translate("MainWindow", "НАЧАТЬ ФАРМ"))
        self.batButton.setText(_translate("MainWindow", """ЗАПУСТИТЬ/ЗАКРЫТЬ
        СЕРВЕР"""))
        self.eyeButton.setText(_translate("MainWindow", "Blur"))
        self.clearButton.setText(_translate("MainWindow", "suspend"))
        self.killButton.setText(_translate("MainWindow", "закрыть все"))
        self.hideButton.setText(_translate("MainWindow", "hide/show окна"))

    def addAccountsF(self):
        self.addAccountsButton.clicked.connect(lambda: self.addAccountsT())
    def addAccounts(self):
        self.add_acc_stat = True
        os.system(os.path.abspath('logpass.txt'))
        self.add_acc_stat = False
    def addMaFilesF(self):
        self.addMaFilesButton.clicked.connect(lambda: self.addMaFilesT())
    def addMaFiles(self):
        path = os.path.abspath('maFiles')
        autoit.run(f'explorer.exe {os.path.abspath(path)}')
    def checkAccountsF(self):
        self.checkAccountsButton.clicked.connect(lambda: self.checkAccounts())
    def checkAccounts(self):
        OnStart()
        CreateAccounts()
        self.itemsToLaunch = []
        self.accountsList.clear()

        info = readJson('accounts.json')
        info2 = readJson('launched_accounts.json')

        for account in info:
            self.accountsList.addItem(account.lower())

        for accountInfo in info:
            for accountView in range(self.accountsList.count()):
                if info[accountInfo]["shared_secret"] is None and accountInfo.lower() == self.accountsList.item(accountView).text():
                    self.accountsList.item(accountView).setBackground(QtGui.QColor(255, 166, 166, 255))

        for accountInfo in info2:
            for accountView in range(self.accountsList.count()):
                if self.accountsList.item(accountView).text() == accountInfo:
                    self.accountsList.item(accountView).setBackground(QtGui.QColor(166, 255, 167, 255))

    def chooseAllItems(self):
        self.allAccountsButton.clicked.connect(lambda: self.chooseAllItemsF())

    def chooseAllItemsF(self):
        if not self.all_accs_choosen:
            self.itemsToLaunch = []
            self.all_accs_choosen = True

            for account in range(self.accountsList.count()):
                if self.accountsList.item(account).background().color().getRgb() != (255, 166, 166, 255) and self.accountsList.item(account).background().color().getRgb() != (166, 255, 167, 255):
                    self.itemsToLaunch.append(self.accountsList.item(account).text())
                    self.accountsList.item(account).setBackground(QtGui.QColor(235, 242, 255, 150))

        else:
            self.all_accs_choosen = False
            self.itemsToLaunch = []
            self.checkAccounts()

        self.LogWrite(f"Выбраны все возможные аккаунты для запуска ({len(self.itemsToLaunch)})")

    def chooseItems(self):
        self.accountsList.itemClicked.connect(self.choosenItems)
    def choosenItems(self, clItem):
        if clItem.background().color().getRgb() != (255, 166, 166, 255) and clItem.background().color().getRgb() != (166, 255, 167, 255):
            if clItem.text() not in self.itemsToLaunch:
                self.itemsToLaunch.append(clItem.text())
                clItem.setBackground(QtGui.QColor(235, 242, 255, 150))

            else:
                self.itemsToLaunch.remove(clItem.text())
                clItem.setBackground(QtGui.QColor(0, 0, 0, 0))

        elif clItem.background().color().getRgb() == (166, 255, 167, 255):
            info = readJson('launched_accounts.json')
            for pid in info:
                if pid.lower() == clItem.text().lower():
                    os.kill(info[pid]["win_csgo_PID"], signal.SIGTERM)
                    os.kill(info[pid]["win_steam_PID"], signal.SIGTERM)
                    self.LogWrite(f'- {info[pid]["login"]} был выключен')
            clItem.setBackground(QtGui.QColor(0, 0, 0, 0))
            OnStart()
        self.accountsList.clearSelection()
    def ReWindowF(self):
        self.windowsButton.clicked.connect(lambda: self.ReWindowT())
    def ReWindow(self):
        self.rew_stat = True
        self.steamAccounts = []
        info = readJson('launched_accounts.json')
        for i in info:
            self.steamAccounts.append(SteamAccount(login=info[i]["login"],
                                                 password=info[i]["password"],
                                                 shared_secret=info[i]["shared_secret"],
                                                 win_csgo_PID=info[i]["win_csgo_PID"],
                                                 win_steam_PID=info[i]["win_steam_PID"],
                                                 status=info[i]["status"],
                                                 posX=info[i]["posX"],
                                                 posY=info[i]["posY"]))
        try:
            win_size = QDesktopWidget().availableGeometry()
            row = 0
            column = 0

            for i in self.steamAccounts:
                matsetvideomod = readJson("settings/settings.json")
                posX = matsetvideomod["win_w"] * row
                posY = matsetvideomod["win_h"] * column

                i.MoveWindow(posX, posY)
                row += 1
                if win_size.width() - matsetvideomod["win_w"] < matsetvideomod["win_w"] * row:
                    row = 0
                    column += 1
        except Exception as ex:
            self.LogWrite(ex)
        self.rew_stat = False
    def LogWrite(self, sentense):
        self.logList.addItem(sentense)
        self.logList.scrollToBottom()
    def startFarmF(self):
        self.startFarmButton.clicked.connect(lambda: self.StartFarmT())
    def startFarm(self):
        self.start_stat = True
        this_itemsToLaunch = self.itemsToLaunch
        thCh = threading.Thread(target=self.checkAccounts, daemon=True)
        thCh.start()
        if this_itemsToLaunch != []:
            if readJson("settings/settings.json")["steam_path"] != "":
                self.steamAccounts = []
                info = readJson('accounts.json')
                for i in this_itemsToLaunch:
                    for account in info:
                        if i == account:
                            self.steamAccounts.append(SteamAccount(info[account]["login"], info[account]["password"], info[account]["shared_secret"]))
                this_itemsToLaunch.clear()
                for account in self.steamAccounts:
                    account.CSGOLaunch(self.logList)
                    self.checkAccounts()

                    for i in range(self.accountsList.count()):
                        if account.login == self.accountsList.item(i).text():
                            self.accountsList.item(i).setBackground(QtGui.QColor(166, 255, 167, 255))
                self.checkAccounts()
            else:
                self.LogWrite("\033[31m- Не возможно начать фарм. Не указан путь до steam.exe\033[0m\n")
        else:
            self.LogWrite("Выберите аккаунты для запуска!")
        self.start_stat = False

    def OptimiseF(self):
        self.optimiseButton.clicked.connect(lambda: self.Optimise())

    def Optimise(self):
        self.opt_stat = True
        self.LogWrite("Оптимизация видеонастроек была запущена!")
        NewSettings(self.logList)
        self.opt_stat = False
    def do_something(self):
        if self.eyeButton.isChecked() == True:
            self.blur_effect.setEnabled(False)
        else:
             self.blur_effect.setEnabled(True)

    def batF(self):
        self.batButton.clicked.connect(lambda: self.bat())
    def bat(self):
        with open(rf'{readJson("settings/settings.json")["server_path"]}' + '\csgo\cfg\server.cfg', encoding='utf-8') as f:
            match = re.search(r'"(.+)"', f.read().split('\n')[0])
            if match:
                result = match.group(1)
        if autoit.win_exists(result):
            os.system("taskkill /im srcds.exe /f")
            os.system('taskkill /F /IM memreduct.exe')
        else:
            autoit.run(rf'{readJson("settings/settings.json")["server_path"]}'+ '/srcds.exe ' + rf'{readJson("settings/settings.json")["server_parametrs"]}')
            autoit.run(rf'{readJson("settings/settings.json")["memreduct_path"]} ')


    def clearF(self):
        self.clearButton.clicked.connect(lambda: self.clear())
    def clear(self):
        if self.clearButton.isChecked() == True:
            global susp
            susp = 1
            t = MyThread()
            t.start()
        else:
            susp = 7




    def killa(self):
        self.killButton.clicked.connect(lambda: self.kill())
    def kill(self):
        data = readJson("launched_accounts.json")
        for key in data:
            os.kill(data[key]["win_csgo_PID"], signal.SIGTERM)
            os.kill(data[key]["win_steam_PID"], signal.SIGTERM)
            data[key]["win_csgo_PID"] = 0
            data[key]["win_steam_PID"] = 0
            data[key]["status"] = 0
        self.checkAccounts()
    def hidea(self):
        self.hideButton.clicked.connect(lambda: self.hide())

    def hide(self):
        if self.hideButton.isChecked() == True:
            data = readJson("launched_accounts.json")
            for key in data:
                time.sleep(1)
                hwnd = win32gui.FindWindow(None, data[key]["win_csgo_title"])
                win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
        else:
            data = readJson("launched_accounts.json") 
            for key in data:
                hwnd = win32gui.FindWindow(None, data[key]["win_csgo_title"])
                win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
                autoit.shutdown(13)

class MyThread(threading.Thread):
    def run(self):
        autoit.run('pssuspend steamwebhelper')
        data = readJson("launched_accounts.json")
        global susp
        while susp < 6:

            for key in data:
                autoit.run(f'pssuspend -r {data[key]["win_csgo_PID"]}')
                autoit.run(f'pssuspend -r {data[key]["win_steam_PID"]}')

                time.sleep(1)

                autoit.run(f'pssuspend {data[key]["win_csgo_PID"]}')
                autoit.run(f'pssuspend {data[key]["win_steam_PID"]}')
        autoit.run('pssuspend -r steamwebhelper')
        autoit.run('pssuspend -r Steam')
        autoit.run('pssuspend -r csgo')
