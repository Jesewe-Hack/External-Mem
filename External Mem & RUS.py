import os
import ctypes
import time
import pymem
import re
import colorama
from colorama import init, Fore
init(autoreset=True)
ctypes.windll.kernel32.SetConsoleTitleA("EXTERNAL MEM | By Jesewe#8563")

os.system("cls")
print(Fore.MAGENTA + 'Добро пожаловать в EXTERNAL MEM')
print(Fore.CYAN + '\n1 > WallHack\n2 > RadarHack')
try:
    choose_cheat=int(input(Fore.YELLOW + '\nПожалуйста, выберите номер >>> '))
except Exception as e:
    os.system("cls")
    print(Fore.RED + 'ОШИБКА: вы ввели недопустимый символ!')
    input(Fore.RED + '\nНажмите Enter, чтобы выйти...')
else:
    if choose_cheat==1:
        try:
            pm=pymem.Pymem('csgo.exe') # using memory csgo.exe
            client=pymem.process.module_from_name(pm.process_handle,'client.dll')
            clientModule=pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
            address =client.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F',clientModule).start() + 2
            pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
            pm.close_process()
        except Exception as e:
            os.system("cls")
            print(Fore.RED + 'ОШИБКА: процесс csgo.exe не запущен!')
            input(Fore.RED + '\nНажмите Enter, чтобы выйти...')
        else:
            os.system("cls")
            print(Fore.GREEN + 'Успешно завершено!')
            input(Fore.GREEN + '\nНажмите Enter, чтобы выйти...')
    elif choose_cheat==2:
        try:
            pm=pymem.Pymem('csgo.exe') # using memory csgo.exe
            client = pymem.process.module_from_name(pm.process_handle,'client.dll')
            clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
            address = client.lpBaseOfDll + re.search(rb'\x74\x15\x8B\x47\x08\x8D\x4F\x08',clientModule).start() - 1
            pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)
            pm.close_process()
        except Exception as e:
            os.system("cls")
            print(Fore.RED + 'ОШИБКА: процесс csgo.exe не запущен!')
            input(Fore.RED + '\nНажмите Enter, чтобы выйти...')
        else:
            os.system("cls")
            print(Fore.GREEN + 'Успешно завершено!')
            input(Fore.GREEN + '\nНажмите Enter, чтобы выйти...')
    else:
        os.system("cls")
        print(Fore.RED + 'ОШИБКА: вы ввели недопустимый символ!')
        input(Fore.RED + '\nНажмите Enter, чтобы выйти...')