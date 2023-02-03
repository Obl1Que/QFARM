from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from functions import *
from settingswindow import Ui_SettingsWindow

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

        self.serversButton = QtWidgets.QPushButton(self.centralwidget)
        self.serversButton.setGeometry(QtCore.QRect(180, 260, 141, 41))
        self.serversButton.setStyleSheet("")
        self.serversButton.setObjectName("serversButton")

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

    def goSettingsF(self):
        self.settingsButton.clicked.connect(lambda: self.goSettings())
    def goSettings(self):
        self.SettingsWindow = QtWidgets.QMainWindow()
        ui = Ui_SettingsWindow()
        ui.setupUi(self.SettingsWindow)
        self.SettingsWindow.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", f"QFARM v{readJson('settings/settings.json')['version']} | Obl1Que"))
        self.settingsButton.setText(_translate("MainWindow", "НАСТРОЙКИ"))
        self.serversButton.setText(_translate("MainWindow", "СЕРВЕРА"))
        self.windowsButton.setText(_translate("MainWindow", ""))
        self.checkAccountsButton.setText(_translate("MainWindow", "ПРОВЕРКА АККАУНТОВ"))
        self.addAccountsButton.setText(_translate("MainWindow", "ДОБАВИТЬ АККАУНТЫ"))
        self.addMaFilesButton.setText(_translate("MainWindow", "ДОБАВИТЬ MAFILE"))
        self.startFarmButton.setText(_translate("MainWindow", "НАЧАТЬ ФАРМ"))

    def addAccountsF(self):
        self.addAccountsButton.clicked.connect(lambda: self.addAccounts())
    def addAccounts(self):
        os.system('logpass.txt')
    def addMaFilesF(self):
        self.addMaFilesButton.clicked.connect(lambda: self.addMaFiles())
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

            if self.itemsToLaunch != []:
                self.LogWrite(f'Выбрано аккаунтов для запуска: {len(self.itemsToLaunch)}')
            else:
                self.LogWrite('Ни одного аккаунта не выбрано!')

        elif clItem.background().color().getRgb() == (166, 255, 167, 255):
            info = readJson('launched_accounts.json')
            for pid in info:
                if pid.lower() == clItem.text().lower():
                    os.kill(info[pid]["win_csgo_PID"], signal.SIGTERM)
                    os.kill(info[pid]["win_steam_PID"], signal.SIGTERM)
                    self.LogWrite(f'- {info[pid]["login"]} был выключен.')
            clItem.setBackground(QtGui.QColor(0, 0, 0, 0))
            OnStart()

        self.accountsList.clearSelection()
    def ReWindowF(self):
        self.windowsButton.clicked.connect(lambda: self.ReWindow())
    def ReWindow(self):
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
                posX = 236 * row
                posY = 120 * column

                i.MoveWindow(posX, posY)
                row += 1
                if win_size.width() - 100 < 236 * row:
                    row = 0
                    column += 1
        except Exception as ex:
            print(ex)
    def LogWrite(self, sentense):
        self.logList.addItem(sentense)
        self.logList.scrollToBottom()
    def startFarmF(self):
        self.startFarmButton.clicked.connect(lambda: self.startFarm())
    def startFarm(self):
        if readJson("settings/settings.json")["steam_path"] != "":
            self.steamAccounts = []
            info = readJson('accounts.json')
            for i in self.itemsToLaunch:
                for account in info:
                    if i == account:
                        self.steamAccounts.append(SteamAccount(info[account]["login"], info[account]["password"], info[account]["shared_secret"]))
            self.itemsToLaunch.clear()
            for account in self.steamAccounts:
                account.CSGOLaunch()
                self.checkAccounts()
                for i in range(self.accountsList.count()):
                    if account.login == self.accountsList.item(i).text():
                        self.accountsList.item(i).setBackground(QtGui.QColor(166, 255, 167, 255))
                        self.logList.addItem(f'+ {account.login} - запущен!')
            self.checkAccounts()
        else:
            self.LogWrite("- Не возможно начать фарм. Не указан путь до steam.exe")
            print("\033[31m- Не возможно начать фарм. Не указан путь до steam.exe\033[0m")