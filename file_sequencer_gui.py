import os
import shutil
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage, filedialog

root = tk.Tk()
root.title(" File Sequencer")
root.geometry("500x200")
root.resizable(False, False)
root.wm_iconbitmap(r"icon.ico")

def exit_func(event = None):
    mbox = messagebox.askyesno("Warning", "Are you sure you want to Exit", icon = "warning")
    if mbox:
        root.destroy()
    else:
        pass


frame = ttk.Frame(root)
frame1 = ttk.Frame(frame)
frame2 = ttk.Frame(frame)
input_label = ttk.Label(frame1, text = "Input Folder PATH : ")
folder_path_ = tk.StringVar()
input_entry = ttk.Entry(frame2, width = 40, textvariable = folder_path_)
def browse(event = None):
    folder_path_temp = filedialog.askdirectory()
    input_entry.insert(tk.END, folder_path_temp)

dict_extensions = {
    'Audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac', '.aiff', '.amr', '.aif', '.mid'),
    'Video_extensions' : ('.mp4', '.mkv', '.MKV', '.3gp', '.mpeg'),
    'Image_extensions' : ('.jpg', '.png', '.gif', '.jpeg'),
    'Documents_extensions' : ('.pdf', '.txt', '.doc'),
    'Archives_extensions' : ('.zip', '.7z', '.xz', '.gz', '.rar'),
    'Installer_extensions' : ('.exe', '.msi'),
    'RDP_extensions' : ('.rdp'),
    'Apps_extensions' : ('.apk'),
}

def submit(event = None):
    global folder_path
    folderpath = folder_path_.get()
    def file_finder(folder_path, file_extensions):
        return [file for file in os.listdir(folder_path) for extensions in file_extensions if file.endswith(extensions)]

    for extension_type, extension_tuple in dict_extensions.items():
        folder_name = extension_type.split('_')[0] + ' Files'
        folder_path = os.path.join(folderpath, folder_name)
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            pass
        for item in (file_finder(folderpath, extension_tuple)):
            item_path = os.path.join(folderpath, item)
            item_new_path = os.path.join(folder_path, item)
            shutil.move(item_path, item_new_path)
    messagebox.showinfo("Done", "Task Completed Successfully")

browse_button = ttk.Button(frame2, text = "Browse", command = browse, cursor = "hand2")
submit_button = ttk.Button(root, text = "Submit", command = submit, cursor = "hand2")
line = tk.Frame(root, height = 1, width = 500, bg = "gray80", relief = "groove")
bottom_label = ttk.Label(root, text = "                                       This Software is developed by : Rahul Meena", background = "black", foreground = "white", cursor = "pirate")


frame.pack(side = tk.TOP, pady = 30)
frame1.pack(side = tk.LEFT)
frame2.pack(side = tk.RIGHT)
input_label.pack(padx = 20, pady = 0)
input_entry.pack(pady = 0, side = tk.LEFT)
browse_button.pack(padx = 2, pady = 0, side = tk.RIGHT)
line.pack(pady = 0)
submit_button.pack(pady = 30)
bottom_label.pack(side = tk.BOTTOM, fill = tk.X, padx = 0, pady = 1)

root.bind("<Control-q>", exit_func)
root.bind("<Escape>", exit_func)

root.mainloop()