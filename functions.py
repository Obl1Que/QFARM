import os
import json
import signal
import time
import autoit
from steampy.guard import generate_one_time_code

class SteamAccount():
    def __init__(self, login, password, shared_secret, win_csgo_PID = None, win_steam_PID = None, status = None, posX = None, posY = None):
        self.login = login
        self.password = password
        self.shared_secret = shared_secret
        self.win_csgo_title = f'[{self.login}] # Counter-Strike: Global Offensive - Direct3D 9'
        self.steam_path = readJson('settings/settings.json')["steam_path"]

        if readJson("settings/settings.json")["steam_language"] != "":
            self.steam_lang = readJson("settings/settings.json")["steam_language"]
            self.steam_lang_guard = readJson("settings/steam_lang.json")["guard_wait"][self.steam_lang]
        else:
            self.steam_lang = None


        if win_csgo_PID is not None and \
                win_steam_PID is not None and \
                status is not None and \
                posX is not None and \
                posY is not None:
            self.win_steam_PID = win_steam_PID
            self.win_csgo_PID = win_csgo_PID
            self.status = status
            self.posX = posX
            self.posY = posY
        else:
            self.win_steam_PID = 0
            self.win_csgo_PID = 0
            self.status = 'Off'
            self.posX = 0
            self.posY = 0
    def GuardGen(self):
        return generate_one_time_code(self.shared_secret)
    def CSGOLaunch(self):
        try:
            self.status = 'Starting'
            autoit.run(f'{readJson("settings/settings.json")["steam_path"]} '
                       f'-login {self.login} {self.password} '
                       f'-applaunch 730 '
                       f'-low '
                       f'-nohltv '
                       f'-no-browser '
                       f'-novid '
                       f'-nosound '
                       f'-window -w 640 -h 480 '
                       f'+exec autoexec.cfg')

            if self.steam_lang == None:
                while autoit.win_exists("Вход в Steam") == 0 and autoit.win_exists("Steam Sign In") == 0:
                    pass
                if autoit.win_exists("Вход в Steam"):
                    info = readJson("settings/settings.json")
                    info["steam_language"] = "русский"
                    file = open(os.path.abspath("settings/settings.json"), "w", encoding="utf-8")
                    file.write(json.dumps(info, indent=4))
                    file.close()
                    self.steam_lang = "русский"
                elif autoit.win_exists("Steam Sign In"):
                    info = readJson("settings/settings.json")
                    info["steam_language"] = "english"
                    file = open(os.path.abspath("settings/settings.json"), "w", encoding="utf-8")
                    file.write(json.dumps(info, indent=4))
                    file.close()
                    self.steam_lang = "english"
                self.steam_lang_guard = readJson('settings/steam_lang.json')["guard_wait"][self.steam_lang]
            print(f"\033[43m{self.login} starting...\033[0m\n[{self.steam_lang.title()} language]")
            autoit.win_wait(self.steam_lang_guard)
            autoit.win_activate(self.steam_lang_guard)
            autoit.win_wait_active(self.steam_lang_guard, 5)
            self.win_steam_PID = autoit.win_get_process(self.steam_lang_guard)
            while autoit.win_exists(self.steam_lang_guard):
                try:
                    autoit.win_activate(self.steam_lang_guard)
                    autoit.send(self.GuardGen())
                    autoit.send('{Enter}')
                    print(f"~ Try send {self.GuardGen()}...")
                except:
                    pass
                finally:
                    time.sleep(3)
            print("+ Guard active")
            autoit.win_wait_close(self.steam_lang_guard)
            print("~ Waiting CS:GO...")
            autoit.win_wait('Counter-Strike: Global Offensive - Direct3D 9')
            autoit.win_activate('Counter-Strike: Global Offensive - Direct3D 9')
            autoit.win_wait_active('Counter-Strike: Global Offensive - Direct3D 9')

            while autoit.win_exists(self.win_csgo_title) == 0:
                autoit.win_activate('Counter-Strike: Global Offensive - Direct3D 9')
                autoit.win_wait_active('Counter-Strike: Global Offensive - Direct3D 9')
                autoit.win_set_title('Counter-Strike: Global Offensive - Direct3D 9', self.win_csgo_title)
            print("+ CS:GO renamed")
            self.MoveWindow(0, 0)
            print("+ CS:GO moved")
            self.win_csgo_PID = autoit.win_get_process(self.win_csgo_title)
            self.status = 'Launched'
            self.UpdateAccountsJSON()
            print(f"\033[32m+ Account {self.login} has been launched!\033[0m\n")
        except Exception as ex:
            if str(ex) == 'run program failed':
                print('\nНе правильно указан путь до папки Steam!\nИзмените в настройках.\n')
    def MoveWindow(self, posX, posY):
        autoit.win_activate(self.win_csgo_title)
        autoit.win_move(self.win_csgo_title, posX, posY)
        self.posX = posX
        self.posY = posY
        self.UpdateAccountsJSON()
    def UpdateAccountsJSON(self):
        info = readJson('launched_accounts.json')
        if self.status == 'Off':
            info.pop(self.login)
        else:
            info[self.login] = {
                'login': self.login,
                'password': self.password,
                'shared_secret': self.shared_secret,
                'win_csgo_title': self.win_csgo_title,
                'win_csgo_PID': self.win_csgo_PID,
                'win_steam_PID': self.win_steam_PID,
                'status': self.status,
                'posX': self.posX,
                'posY': self.posY
            }
        file = open('launched_accounts.json', 'w', encoding='utf-8')
        file.write(json.dumps(info, indent=4))
        file.close()
    def CloseAccount(self):
        os.kill(self.win_csgo_PID, signal.SIGTERM)
        os.kill(self.win_steam_PID, signal.SIGTERM)
        self.win_csgo_PID = 0
        self.win_steam_PID = 0
        self.status = 'Off'
        self.UpdateAccountsJSON()

def GetSharedSecret(login):
    dir_name = os.path.abspath("./maFiles")
    for item in os.listdir(dir_name):
        try:
            info = readJson(f'{dir_name}/{item}')
            if info['account_name'].lower() == login:
                return info['shared_secret']
        except:
            return None

def ParceLogPass():
    accounts = {}
    file = open('logpass.txt')

    for account in file:
        if account != '\n':
            account_pair = account.split(':')
            accounts[account_pair[0].lower()] = {'login': account_pair[0].lower(),
                                                 'password': account_pair[1].replace('\n', '')}
    file.close()
    return accounts

def CreateAccounts():
    accounts = ParceLogPass()
    for login in accounts:
        accounts[login]['shared_secret'] = GetSharedSecret(login)

    file = open('accounts.json', 'w', encoding='utf-8')
    file.write(json.dumps(accounts, indent=4))
    file.close()

def readJson(path):
    file = open(os.path.abspath(path), encoding='utf-8')
    info = json.loads(file.read())
    file.close()
    return info

def OnStart():
    os.system('CLS')
    info = readJson('launched_accounts.json')
    for account in info.copy():
        if autoit.win_exists(info[account]["win_csgo_title"]) == 1:
            continue
        else:
            info.pop(account)
    file = open('launched_accounts.json', 'w', encoding='utf-8')
    file.write(json.dumps(info, indent=4))
    file.close()