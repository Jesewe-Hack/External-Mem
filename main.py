import os
import ctypes
import time
import pymem
import re
import requests, version, webbrowser
import colorama
from colorama import init, Fore
init(autoreset=True)

ctypes.windll.kernel32.SetConsoleTitleW("External Memory | By Jesewe Hack")

def check_version():
    os.system('cls')
    print(Fore.MAGENTA + '                                   Checking for updates...')
    local_version = version.ver
    try:
        response = requests.get('https://raw.githubusercontent.com/Jesewe-Hack/External-Mem/main/version.py').text
    except:
        print(Fore.RED + '\n                                   Failed to get latest version')
        input(bcolors.OKGREEN + '\n                                   Press Enter to return to the main menu...')
        response = None

    if response != None:
        github_version = float(re.split('=', response.strip())[1])

        if github_version > local_version:
            print(Fore.RED + f'\n                                   Found new version: {github_version}')
            try:
                webbrowser.open('https://github.com/Jesewe-Hack/External-Mem/releases')
                input(bcolors.OKGREEN + '\n                                   Press Enter to return to the main menu...')
            except:
                print(Fore.GREEN + '\n                                   No updates found!')
                input(bcolors.OKGREEN + '\n                                   Press Enter to return to the main menu...')
        else:
            print(Fore.GREEN + '\n                                   No updates found!')
            input(bcolors.OKGREEN + '\n                                   Press Enter to return to the main menu...')

def radar():
    pm = pymem.Pymem('csgo.exe')
    client = pymem.process.module_from_name(pm.process_handle,
                                    'client.dll')

    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'\x74\x15\x8B\x47\x08\x8D\x4F\x08',
                                     clientModule).start() - 1

    pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)
    pm.close_process()

def wallhack():
    pm = pymem.Pymem('csgo.exe')
    client = pymem.process.module_from_name(pm.process_handle,
                                            'client.dll')

    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'\x33\xC0\x83\xFA.\xB9\x20',
                                             clientModule).start() + 4

    pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
    pm.close_process()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

banner="""
                    ▄▄▄ .▐▄• ▄ ▄▄▄▄▄▄▄▄ .▄▄▄   ▐ ▄  ▄▄▄· ▄▄▌      • ▌ ▄ ·. ▄▄▄ .• ▌ ▄ ·.       ▄▄▄   ▄· ▄▌
                    ▀▄.▀· █▌█▌▪•██  ▀▄.▀·▀▄ █·•█▌▐█▐█ ▀█ ██•      ·██ ▐███▪▀▄.▀··██ ▐███▪▪     ▀▄ █·▐█▪██▌
                    ▐▀▀▪▄ ·██·  ▐█.▪▐▀▀▪▄▐▀▀▄ ▐█▐▐▌▄█▀▀█ ██▪      ▐█ ▌▐▌▐█·▐▀▀▪▄▐█ ▌▐▌▐█· ▄█▀▄ ▐▀▀▄ ▐█▌▐█▪
                    ▐█▄▄▌▪▐█·█▌ ▐█▌·▐█▄▄▌▐█•█▌██▐█▌▐█ ▪▐▌▐█▌▐▌    ██ ██▌▐█▌▐█▄▄▌██ ██▌▐█▌▐█▌.▐▌▐█•█▌ ▐█▀·.
                     ▀▀▀ •▀▀ ▀▀ ▀▀▀  ▀▀▀ .▀  ▀▀▀ █▪ ▀  ▀ .▀▀▀     ▀▀  █▪▀▀▀ ▀▀▀ ▀▀  █▪▀▀▀ ▀█▄▀▪.▀  ▀  ▀ • 
"""

while True:
    os.system("cls")
    print(bcolors.OKGREEN + banner)
    print(bcolors.OKBLUE + """
                                [ Made by Jesewe Hack : https://github.com/Jesewe-Hack ]
    """ + bcolors.ENDC)
    print(bcolors.OKCYAN + """
                                    [0] Exit 
                                    [1] Run WallHack
                                    [2] Run RadarHack
                                    [3] Check for Update
                                    [4] About
    """ + bcolors.ENDC)
    try:
        choose_cheat=int(input(bcolors.OKBLUE + '                                   Action : '))
    except Exception as e:
        os.system("cls")
        print(bcolors.FAIL + '                                   ERROR: You entered an invalid value!')
        input(bcolors.FAIL + '                                   Press Enter to return to the main menu...')
    else:
        if choose_cheat==0:
            print(bcolors.WARNING + "\n                                   Exit...")
            os.abort()
        elif choose_cheat==1:
            try:
                os.system('cls')
                print(bcolors.HEADER + '                                   Injecting...')
                wallhack()
            except Exception as e:
                print(bcolors.FAIL + '\n                                   ERROR: csgo.exe process is not running!')
                input(bcolors.FAIL + '\n                                   Press Enter to return to the main menu...')
            else:
                print(bcolors.OKGREEN + '\n                                   Successfully!')
                input(bcolors.OKGREEN + '\n                                   Press Enter to return to the main menu...')
        elif choose_cheat==2:
            try:
                os.system('cls')
                print(bcolors.HEADER + '                                   Injecting...')
                radar()
            except Exception as e:
                print(Fore.RED + '\n                                   ERROR: csgo.exe process is not running!')
                input(Fore.RED + '\n                                   Press Enter to return to the main menu...')
            else:
                print(bcolors.OKGREEN + '\n                                   Successfully!')
                input(bcolors.OKGREEN + '\n                                   Press Enter to return to the main menu...')
        elif choose_cheat==3:
            try:
                check_version()
            except Exception as e:
                print(bcolors.FAIL + '                                   Failed to check for update!')
                input(bcolors.OKGREEN + '\n                                   Press Enter to return to the main menu...')
        elif choose_cheat==4:
            print(bcolors.OKCYAN + """
                                            Use at your own risk, VAC anti-cheat does not ban 
                                            for this script! But it can ban the patrol!
                                            The external cheat is fully optimized for Windows versions: 8.1, 10.
            """ + bcolors.ENDC)
            input(bcolors.OKGREEN + '                                   Press Enter to return to the main menu...')
        else:
            os.system("cls")
            print(bcolors.FAIL + '\n                                   ERROR: You entered an invalid value!')
            input(bcolors.FAIL + '\n                                   Press Enter to return to the main menu...')
