from tkinter import *
from tkinter import ttk
from lib.logic import file_to_treeview, print_tv_active
from PIL import Image, ImageTk
import sv_ttk
import os
import tempfile
import ctypes
from ctypes import windll, wintypes


# Color palette
light1 = "#60C7FB"
light2 = "#FFFFFF"
dark1 = "#2E2E2E"
dark2 = "#1C1C1C"


def remove_focus(event):
    window.focus_set()


# Window
window = Tk()
window.geometry("1000x600")
window.title("QuickStarter")
window.resizable(0, 0)
icon = ImageTk.PhotoImage(file="lib\source\QS.png")
window.iconphoto(False, icon)

# Styles
edit_img = Image.open("lib/source/edit.png").resize((15, 15))
plus_img = Image.open("lib\source\plus.png").resize((10, 10))
sort_img = Image.open("lib\source\sort-az.png").resize((15, 15))
folder_img = Image.open("lib\source\\folder.png").resize((15, 15))
minus_img = Image.open("lib\source\minus.png").resize((10, 10))

edit_tk = ImageTk.PhotoImage(edit_img)
plus_tk = ImageTk.PhotoImage(plus_img)
sort_tk = ImageTk.PhotoImage(sort_img)
folder_tk = ImageTk.PhotoImage(folder_img)
minus_tk = ImageTk.PhotoImage(minus_img)

# **Screens**
Home_Screen = ttk.Frame(window)
Home_Screen.place(relheight=1, relwidth=1)

Sandbox_Screen = ttk.Frame(window)

# **Home Screen**
task_container = ttk.LabelFrame(
    Home_Screen, text="Tasks", width=400, height=200)
task_container.place(relx=0.5, rely=0.5, anchor="center")

notice = ttk.Label(task_container, text="No tasks available.")
notice.place(relx=0.5, rely=0.5, anchor="center")

# -Buttons


def go_to_sandbox():
    Home_Screen.place_forget()
    Sandbox_Screen.place(relheight=1, relwidth=1)


def go_to_home():
    Sandbox_Screen.place_forget()
    Home_Screen.place(relheight=1, relwidth=1)


more_btn = ttk.Button(window, text="+", width=20,
                      command=go_to_sandbox, image=plus_tk, compound="center")
more_btn.place(in_=task_container, relx=1, y=-50, anchor="ne")

edit_btn = ttk.Button(window, width=20, image=edit_tk, compound="center")
edit_btn.place(in_=task_container, relx=.46, y=-50, anchor="ne")

# **Sandbox Screen**

# Tabs
notebook = ttk.Notebook(Sandbox_Screen)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.bind("<<NotebookTabChanged>>", remove_focus)

notebook.add(tab1, text="New Task")
notebook.add(tab2, text="Preferences")
notebook.place(relwidth=1, relheight=1)

# Screen
screen = ttk.Frame(tab1)
screen.pack(fill=BOTH, expand=True)

screen.bind("<ButtonRelease-1>", remove_focus)

# properties
name_entry = ttk.Entry(tab1, width=15)
name_entry.place(x=35, y=20)

prop_frame = ttk.Labelframe(tab1, width=175, height=470, text="Properties")
prop_frame.place(x=20, y=60)
prop_frame.bind("<ButtonRelease-1>", remove_focus)

# workspace
workspace = ttk.Labelframe(tab1, text="Workspace")
workspace.place(x=210, y=60, height=470, width=580)
workspace.bind("<ButtonRelease-1>", remove_focus)

# tools
modes = ["Default (Unordered)", "Timed"]
typeCBox = ttk.Combobox(tab1, values=modes, width=16)
typeCBox.set(modes[0])
typeCBox.place(x=220, y=15)

delete_tool = ttk.Button(
    tab1, width=4, style="Accent.TButton", image=minus_tk, compound="center")
delete_tool.place(x=730, y=15)

save_tool = ttk.Button(tab1, text="Save")
save_tool.place(x=670, y=15, )
clear_tool = ttk.Button(tab1, text="Clear All")
clear_tool.place(x=589, y=15, )
import_tool = ttk.Button(tab1, text="Import Task")
import_tool.place(x=487, y=15, )

delete_tool.bind("<ButtonRelease-1>", remove_focus)
save_tool.bind("<ButtonRelease-1>", remove_focus)
clear_tool.bind("<ButtonRelease-1>", remove_focus)
import_tool.bind("<ButtonRelease-1>", remove_focus)

# explorer

search_bar = ttk.Entry(tab1, width=19)
search_bar.place(x=805, y=20)
sort_btn = ttk.Button(tab1, text="Sortering", image=sort_tk)
sort_btn.place(x=805, y=55)

file_btn = ttk.Button(tab1, text="Add File", image=folder_tk,
                      command=lambda: file_to_treeview(tv))
file_btn.place(x=850, y=55)

add_btn = ttk.Button(tab1, image=plus_tk, width=4,
                     compound="center", style="Accent.TButton")
add_btn.place(x=920, y=55)

sort_btn.bind("<ButtonRelease-1>", remove_focus)
file_btn.bind("<ButtonRelease-1>", remove_focus)
add_btn.bind("<ButtonRelease-1>", remove_focus)


tv = ttk.Treeview(tab1, columns=("name"), show="headings")
tv.column("name", minwidth=50, width=50)
tv.heading("name", text="Name")

tv.place(width=170, height=440, x=805, y=90)
# Exe
sv_ttk.use_dark_theme()
window.mainloop()
