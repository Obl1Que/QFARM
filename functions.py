import os
import json
import signal
import time
import autoit
import requests
import py_win_keyboard_layout
from bs4 import BeautifulSoup
from steampy.guard import generate_one_time_code

class SteamAccount():
    def __init__(self, login, password, shared_secret, win_csgo_PID = None, win_steam_PID = None, status = None, posX = None, posY = None):
        self.login = login
        self.password = password
        self.shared_secret = shared_secret
        self.win_csgo_title = f'[{self.login}] # Counter-Strike: Global Offensive - Direct3D 9'
        self.steam_path = readJson('settings/settings.json')["steam_path"]
        self.will_connected = None
        self.ip = ''

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
    def CSGOLaunch(self, logList):
        try:
            self.status = 'Starting'

            if readJson("settings/settings.json")["server_log_pass"] == "":
                self.will_connected = False
                autoit.run(f'{readJson("settings/settings.json")["steam_path"]} '
                           f'-login {self.login} {self.password} '
                           f'-applaunch 730 '
                           f'-console '
                           f'-d3d9ex '
                           f'+exec qfarm.cfg '
                           f'+fps_max 30 '
                           f'-low '
                           f'-nohltv '
                           f'-nojoy '
                           f'-nomouse '
                           f'-nosound '
                           f'-noubershader '
                           f'-novid '
                           f'-window -w 640 -h 480')
            else:
                self.will_connected = True
                self.ip = readJson("settings/settings.json")["server_log_pass"]
                autoit.run(f'{readJson("settings/settings.json")["steam_path"]} '
                           f'-login {self.login} {self.password} '
                           f'-applaunch 730 '
                           f'-console '
                           f'-d3d9ex '
                           f'+exec qfarm.cfg '
                           f'+fps_max 30 '
                           f'-low '
                           f'-nohltv '
                           f'-nojoy '
                           f'-nomouse '
                           f'-nosound '
                           f'-noubershader '
                           f'-novid '
                           f'-window -w 640 -h 480 '
                           f'+connect {self.ip}')

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
            logList.addItem(f"{self.login} запуск...")
            logList.scrollToBottom()

            while autoit.win_exists(self.steam_lang_guard) == 0:
                pass

            autoit.win_activate(self.steam_lang_guard)
            autoit.win_wait_active(self.steam_lang_guard)
            self.win_steam_PID = autoit.win_get_process(self.steam_lang_guard)
            logList.addItem(f"~ Попытка отправить guard code...")
            logList.scrollToBottom()

            while autoit.win_exists(self.steam_lang_guard):
                try:
                    time.sleep(5)
                    autoit.win_activate(self.steam_lang_guard)
                    for i in range(5):
                        autoit.send('{BACKSPACE}')
                    autoit.send(self.GuardGen())
                    py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x04090409)
                    autoit.send('{Enter}')
                except:
                    pass
                finally:
                    time.sleep(3)
            logList.addItem("+ Guard code успешно введён")
            logList.scrollToBottom()
            autoit.win_wait_close(self.steam_lang_guard)
            logList.addItem("~ Ожидание CS:GO...")
            logList.scrollToBottom()

            while autoit.win_exists(self.win_csgo_title) == 0:
                autoit.win_wait('Counter-Strike: Global Offensive - Direct3D 9')
                autoit.win_activate('Counter-Strike: Global Offensive - Direct3D 9')
                autoit.win_wait_active('Counter-Strike: Global Offensive - Direct3D 9')
                autoit.win_set_title('Counter-Strike: Global Offensive - Direct3D 9', self.win_csgo_title)
            time.sleep(1)
            self.MoveWindow(0, 0)
            self.win_csgo_PID = autoit.win_get_process(self.win_csgo_title)
            self.status = 'Launched'
            self.UpdateAccountsJSON()
            if self.will_connected == True:
                logList.addItem(f"~ Аккаунт {self.login} будет подключен к {self.ip}")
                logList.scrollToBottom()
            logList.addItem(f"+ Аккаунт {self.login} успешно запущен!\n")
            logList.scrollToBottom()
        except Exception as ex:
            if str(ex) == 'run program failed':
                logList.addItem("\nНе правильно указан путь до steam.exe!\nИзмените в настройках.\n")
                logList.scrollToBottom()
            else:
                logList.addItem(ex)
                logList.scrollToBottom()
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
            with open(f'{dir_name}/{item}', 'r') as f:
                info = json.load(f)
                if info['account_name'].lower() == login:
                    return info['shared_secret']
        except (FileNotFoundError, json.JSONDecodeError):
            pass
    return None

def ParceLogPass():
    accounts = {}
    with open('logpass.txt', 'r') as file:
        for account in file:
            if account.strip():
                account_pair = account.strip().split(':')
                accounts[account_pair[0].lower()] = {'login': account_pair[0].lower(),
                                                     'password': account_pair[1]}
    return accounts
def CreateAccounts():
    accounts = ParceLogPass()
    for login in accounts:
        accounts[login]['shared_secret'] = GetSharedSecret(login)

    with open('accounts.json', 'w', encoding='utf-8') as file:
        json.dump(accounts, file, indent=4)

def readJson(path):
    file = open(os.path.abspath(path), encoding='utf-8')
    info = json.loads(file.read())
    file.close()
    return info

def OnStart():
    info = readJson('launched_accounts.json')
    to_remove = []
    for account, details in info.items():
        if autoit.win_exists(details["win_csgo_title"]):
            continue
        else:
            try:
                os.kill(details["win_steam_PID"], signal.SIGTERM)
            except OSError:
                pass
            to_remove.append(account)
    for account in to_remove:
        info.pop(account)
    with open('launched_accounts.json', 'w', encoding='utf-8') as file:
        json.dump(info, file, indent=4)


def OnStartPrintInfo():
    actual_version = readJson("settings/settings.json")["version"]

    return (f'QFARM Panel by Obl1Que {actual_version}\n\n'
            f'Спасибо за использование и тестировку данной бесплатной панели, если вы хотите как-то помочь улучшить панель,\n'
            f'либо обратиться за помощью, или же просто сказать спасибо - вы всегда можете присоединиться к нашему дружному\n'
            f'tg каналу @QFARMPANEL!\n\n'
            f''
            f'Что нового в этой версии панели?\n'
            f'- Обновлена версия панели до v2.5.2T\n'
            f'- Добавлена возможность выбирать все аккаунты, либо же снимать выделение 1-ой кнопкой\n'
            f'- Небольшой баг-фикс\n'
            f'\n'
            f'Github: https://github.com/Obl1Que\n'
            f'Donate: https://steamcommunity.com/tradeoffer/new/?partner=242071350&token=_u728zwQ\n'
            f'Feedback: https://zelenka.guru/threads/4559961/\n')

def NewSettings(logList):
    CreateOptomisations(logList)

    userdata_path = readJson("settings/settings.json")["steam_path"][:-10] + "\\userdata"

    for user in os.listdir(userdata_path):
        video = open(os.path.abspath("settings/video.txt")).read()
        videodefaults = open(os.path.abspath("settings/videodefaults.txt")).read()
        path = userdata_path + "\\" + user + "\\730\\local\\cfg"

        if not os.path.exists(userdata_path + "\\" + user + "\\730\\local\\cfg\\video.txt"):
            try:
                os.makedirs(path)
                open(userdata_path + "\\" + user + "\\730\\local\\cfg\\video.txt", "w")
                open(userdata_path + "\\" + user + "\\730\\local\\cfg\\videodefaults.txt", "w")
            except:
                logList.addItem(f"+ Папка настроек аккаунта {user} была создана!")
                logList.scrollToBottom()
            finally:
                if open(userdata_path + "\\" + user + "\\730\\local\\cfg\\video.txt").read() != video:
                    new_video = open(userdata_path + "\\" + user + "\\730\\local\\cfg\\video.txt", "w")
                    new_video.write(video)
                    new_video.close()
                    new_videodefaults = open(userdata_path + "\\" + user + "\\730\\local\\cfg\\videodefaults.txt", "w")
                    new_videodefaults.write(videodefaults)
                    new_videodefaults.close()
                    logList.addItem(f"+ Настройки аккаунта {user} были загружены!")
                    logList.scrollToBottom()

def CreateQFarmexec(logList):
    try:
        cfg_path = os.path.join(readJson("settings/settings.json")["csgo_path"], "csgo/cfg")
        cfg_settings = open(os.path.abspath("settings/qfarm.cfg")).read()
        try:
            exist_cfg_info = open(os.path.join(cfg_path, "qfarm.cfg")).read()

            if exist_cfg_info == cfg_settings:
                logList.addItem("Файл qfarm.cfg уже существует!")
            else:
                os.remove(os.path.join(cfg_path, "qfarm.cfg"))
                raise Exception("Удалите файл qfarm.cfg и попробуйте снова!")
        except FileNotFoundError:
            cfg_file = open(os.path.join(cfg_path, "qfarm.cfg"), "w")
            cfg_file.write(cfg_settings)
            cfg_file.close()
            logList.addItem("Файл qfarm.cfg создан!\n")
        logList.scrollToBottom()
    except:
        logList.addItem("Путь до cfg не содержится в папке Steam!\n")
        logList.scrollToBottom()

def GetActualVersion():
    soup = BeautifulSoup(requests.get("https://github.com/Obl1Que/QFARM/blob/master/README.md").text, 'html.parser')
    soup_v = soup.find_all('p')[0].get_text()
    return [True, soup_v] if readJson("settings/settings.json")["version"] != soup_v else [False]

def GetUID(login):
    dir_name = os.path.abspath("./maFiles")
    for item in os.listdir(dir_name):
        try:
            info = readJson(f'{dir_name}/{item}')

            if login == info["account_name"]:
                return info["Session"]["SteamID"]
        except:
            return None
def commid_to_steamid(commid):
    steamid64ident = 76561197960265728
    return commid - steamid64ident
def CreateOptomisations(logList):
    CreateQFarmexec(logList)
    accountID_dirs = os.listdir(readJson("settings/settings.json")["steam_path"][:-10] + "\\userdata")
    info = readJson("accounts.json")

    for account in info:
        if info[account]["shared_secret"]:
            this_acc = str(commid_to_steamid(GetUID(account)))
            try:
                steam_path = readJson("settings/settings.json")["steam_path"][:-10]
                os.makedirs(os.path.join(steam_path, "userdata", this_acc))
                logList.addItem(f"\033[32m+ Папка настроек аккаунта {account} была создана!\033[0m")
                logList.scrollToBottom()
            except:
                logList.addItem(f"~ Аккаунт {account} уже имеет папку с настройками!")
                logList.scrollToBottom()
        else:
            logList.addItem(f"- У аккаунта {account} нет maFile'ов!")
            logList.scrollToBottom()
