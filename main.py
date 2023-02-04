import ctypes, os, sys, time
from pyscreeze import unicode

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

try:
    if is_admin():
        from mainwindow import *
        os.system("pip install -r requirements.txt")

        OnStart()
        os.system('CLS')
        app = QtWidgets.QApplication(sys.argv)
        app.setWindowIcon(QtGui.QIcon('img/icon.png'))

        MainWindow = QtWidgets.QMainWindow()
        MainWindow.setWindowIcon(QtGui.QIcon('img/icon.png'))

        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)

        MainWindow.show()
        sys.exit(app.exec_())
    else:
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)

except Exception as ex:
    print(f'QFARM version is - {readJson("settings/settings.json")["version"]}')
    input(f"{ex}")
    time.sleep(3)