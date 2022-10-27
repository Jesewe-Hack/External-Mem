import pymem, re
import pymem.process
import sys
from tkinter import messagebox

def check_game_connection():
    try:
        pm = pymem.Pymem("csgo.exe")                                                    
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    except Exception as e:
        messagebox.showerror("External Memory", "ERROR: csgo.exe process is not running!")
        sys.exit(0)