import os
import webbrowser
import subprocess
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

file_location = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(file_location, '..', 'assets', 'icon.png')
url = 'https://www.google.com/search?q='

def find_chrome_exe():
    try:
        result = subprocess.run(["where", "chrome.exe"], capture_output=True, text=True, check=True)
        chrome_path = result.stdout.strip()
        return chrome_path
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

chrome_exe_path = find_chrome_exe()

def create_url(query):
    return url + query.replace(' ', '+')

def search_google():
    user_input = search_entry_var.get()
    if not user_input:
        messagebox.showwarning(title='Error', message='Invalid.')
    else:
        final_url = create_url(user_input)
        webbrowser.get(chrome_exe_path).open(final_url)

root = ttk.Window(themename='cosmo')
root.title('Browse Internet')

root_pos_width = root.winfo_screenwidth() - 445
root_pos_height = root.winfo_screenheight() - 1030
root.geometry(f"425x75+{root_pos_width}+{root_pos_height}")

root.resizable(False, False)

search_entry_var = tk.StringVar()
search_entry = ttk.Entry(
    root, width=30, textvariable=search_entry_var)
search_entry.pack(side='left', padx=15, expand=1)

search_button = ttk.Button(root, text='Browse', command=search_google)
search_button.pack(side='left', padx=15, expand=1)

root.attributes('-topmost', True)
root.mainloop()
