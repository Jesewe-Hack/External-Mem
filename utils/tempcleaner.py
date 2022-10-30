import os
import shutil
import psutil
from tkinter import messagebox

def temp_cleaner():  
    folder = 'C:/Users/'+os.getlogin()+'/AppData/Local/Temp'

    deleteFileCount = 0
    deleteFolderCount = 0

    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        indexNo = file_path.find('\\')
        itemName = file_path[indexNo+1:]
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
                print( '%s file deleted' % itemName )
                deleteFileCount = deleteFileCount + 1

            elif os.path.isdir(file_path):
                if file_path.__contains__('chocolatey'):  continue
                shutil.rmtree(file_path)
                print( '%s folder deleted' % itemName )
                deleteFolderCount = deleteFolderCount + 1

        except Exception as e:
            print('Access Denied: %s' % itemName )
    messagebox.showinfo("External Memory", "Temp folder cleared successfully!", icon='info')