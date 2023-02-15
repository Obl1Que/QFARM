from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from functions import *
from settingswindow import Ui_SettingsWindow
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.itemsToLaunch = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("QMainWindow {"
                                 "background-color: white;"
                                 "}")
        self.MainWindow = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(".QPushButton {"
                                         "border: 0 solid;"
                                         "border-radius: 8px;"
                                         "color: white;"
                                         "font-size: 13px;"
                                         "font-weight: bold;"
                                         "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(178, 99, 252, 255), stop:0.5 rgba(251, 162, 213, 255), stop:1 rgba(182, 242, 221, 255));"
                                         "}"
                                         ".QPushButton:hover {"
                                         "font-size: 14px;"
                                         "}"
                                         ".QListWidget {"
                                         "    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(178, 99, 252, 100), stop:0.5 rgba(251, 162, 213, 100), stop:1 rgba(182, 242, 221, 100));\n"
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
        self.accountsList.setGeometry(QtCore.QRect(445, 21, 331, 281))
        self.accountsList.setObjectName("accountsList")

        self.logList = QtWidgets.QListWidget(self.centralwidget)
        self.logList.setGeometry(QtCore.QRect(25, 320, 751, 261))
        self.logList.setObjectName("logList")

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

        self.LogWrite(OnStartPrintInfo())
        self.opt_stat = False
        self.rew_stat = False
        self.start_stat = False
        self.add_acc_stat = False

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
    def OptimiseT(self):
        if self.opt_stat == False:
            t2 = threading.Thread(target=self.Optimise, daemon=True)
            t2.start()
        else:
            self.LogWrite("Панель уже оптимизирует аккаунты!")

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
            print(f"\033[3m\033[32mДОСТУПНА НОВАЯ ВЕРСИЯ ПАНЕЛИ ({readJson('settings/settings.json')['version']} --> {self.need_update[1]}) ДЛЯ СКАЧИВАНИЯ!\033[0m\n"
                  f"\033[3m\033[32mПЕРЕХОДИ ПО ССЫЛКЕ ЧТОБЫ СКАЧАТЬ: https://github.com/Obl1Que/QFARM\033[0m\n")
            MainWindow.setWindowTitle(_translate("MainWindow", f"QFARM {readJson('settings/settings.json')['version']} | Obl1Que | ВОЗМОЖНО ОБНОВЛЕНИЕ ДО {self.need_update[1]}"))
        else:
            MainWindow.setWindowTitle(_translate("MainWindow", f"QFARM {readJson('settings/settings.json')['version']} | Obl1Que"))
        self.settingsButton.setText(_translate("MainWindow", "НАСТРОЙКИ"))
        self.optimiseButton.setText(_translate("MainWindow", "ОПТИМИЗИРОВАТЬ"))
        self.windowsButton.setText(_translate("MainWindow", ""))
        self.checkAccountsButton.setText(_translate("MainWindow", "ПРОВЕРКА АККАУНТОВ"))
        self.addAccountsButton.setText(_translate("MainWindow", "ДОБАВИТЬ АККАУНТЫ"))
        self.addMaFilesButton.setText(_translate("MainWindow", "ДОБАВИТЬ MAFILE"))
        self.startFarmButton.setText(_translate("MainWindow", "НАЧАТЬ ФАРМ"))

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
        self.itemsToLaunch.clear()
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
        self.optimiseButton.clicked.connect(lambda: self.OptimiseT())

    def Optimise(self):
        self.opt_stat = True
        self.LogWrite("Оптимизация видеонастроек была запущена!")
        NewSettings(self.logList)
        self.opt_stat = False