import requests, version, re, webbrowser
from tkinter import messagebox

def check_update_app():
    local_version = version.ver
    try:
        response = requests.get('https://raw.githubusercontent.com/Jesewe-Hack/External-Mem/main/version.py').text
    except:
        messagebox.showerror(f"External Memory", "Failed to get latest version")
        response = None

    if response != None:
        github_version = float(re.split('=', response.strip())[1])

        if github_version > local_version:
            messagebox.showinfo('External Memory', f'Found new version: {github_version}')
            try:
                webbrowser.open('https://github.com/Jesewe-Hack/External-Mem/releases')
            except:
                messagebox.showinfo("External Memory", "No updates found!")
        else:
            messagebox.showinfo("External Memory", "No updates found!")