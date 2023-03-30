from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget
from functions import *
from settingswindow import Ui_SettingsWindow
from PyQt5.QtWidgets import *
import threading
import autoit
import os




def suspend():
    autoit.run('pssuspend steamwebhelper')
    data = readJson("launched_accounts.json")
    n = 1
    while n < 6:

        for key in data:
            autoit.run(f'pssuspend -r {data[key]["win_csgo_PID"]}')
            autoit.run(f'pssuspend -r {data[key]["win_steam_PID"]}')

            time.sleep(1)

            autoit.run(f'pssuspend {data[key]["win_csgo_PID"]}')
            autoit.run(f'pssuspend {data[key]["win_steam_PID"]}')
suspend()