import pymem, re
import pymem.process
from tkinter import messagebox

def wallhack():
    try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                                'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'\x33\xC0\x83\xFA.\xB9\x20',
                                                 clientModule).start() + 4

        pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
        pm.close_process()
    except Exception:
        messagebox.showerror('External Memory', f'Task not completed!\nERROR: csgo.exe process is not running!', icon='error')
    else:
        messagebox.showinfo('External Memory', 'Task successfully completed!', icon='info')

def wallhack_key():
    try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                                'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'\x33\xC0\x83\xFA.\xB9\x20',
                                                 clientModule).start() + 4

        pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
        pm.close_process()
    except Exception:
        messagebox.showerror('External Memory', f'Task not completed!\nERROR: csgo.exe process is not running!', icon='error')