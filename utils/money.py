import pymem
import re
from tkinter import messagebox

def money_reveal():
    try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                                'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',
                                                 clientModule).start()

        pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)
        pm.close_process()
    except Exception:
        messagebox.showerror('External Memory', f'Task not completed!\nERROR: csgo.exe process is not running!', icon='error')
    else:
        messagebox.showinfo('External Memory', 'Task successfully completed!', icon='info')

def money_key():
    try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                                'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',
                                                 clientModule).start()

        pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)
        pm.close_process()
    except Exception:
        messagebox.showerror('External Memory', f'Task not completed!\nERROR: csgo.exe process is not running!', icon='error')