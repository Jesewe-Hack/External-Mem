import pymem, re
import pymem.process
from tkinter import messagebox

def radarhack():
    try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                        'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'\x74\x15\x8B\x47\x08\x8D\x4F\x08',
                                         clientModule).start() - 1

        pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)
        pm.close_process()
    except Exception:
        messagebox.showerror('External Memory', f'Task not completed!\nERROR: csgo.exe process is not running!', icon='error')
    else:
        messagebox.showinfo('External Memory', 'Task successfully completed!', icon='info')

def radarhack_key():
    try:
        pm = pymem.Pymem('csgo.exe')
        client = pymem.process.module_from_name(pm.process_handle,
                                        'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'\x74\x15\x8B\x47\x08\x8D\x4F\x08',
                                         clientModule).start() - 1

        pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)
        pm.close_process()
    except Exception:
        messagebox.showerror('External Memory', f'Task not completed!\nERROR: csgo.exe process is not running!', icon='error')