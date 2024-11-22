from tkinter import *
from tkinter import ttk
from lib.logic import get_icon, get_file_dox, verify_existed_file
from PIL import Image, ImageTk
import sv_ttk
import json

with open("lib/log.json", "r") as f:
    data = json.load(f)

# Constants
applist = []

MAX_COLS = 5
current_row = 0
current_col = 0


def remove_focus(event):
    window.focus_set()


# Window
window = Tk()
window.geometry("1000x600")
window.title("QuickStarter")
window.resizable(0, 0)
icon = ImageTk.PhotoImage(file="lib/source/QS.png")
window.iconphoto(False, icon)

# Styles
edit_img = Image.open("lib/source/edit.png").resize((15, 15))
plus_img = Image.open("lib/source/plus.png").resize((10, 10))
sort_img = Image.open("lib/source/sort-az.png").resize((15, 15))
folder_img = Image.open("lib/source/folder.png").resize((15, 15))
minus_img = Image.open("lib/source/minus.png").resize((10, 10))

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

# Buttons


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

# *Explorer

# Methods


def refresh_tv(treeview, dic):
    for item in treeview.get_children():
        treeview.delete(item)

    for k in dic:
        shortname = k
        # Verifica se o shortname excede 16 caracteres
        if len(shortname) > 16:
            shortname = shortname[:16] + "..."

        treeview.insert("", "end", values=(
            shortname, dic[k]["Name"], dic[k]["Extension"], dic[k]["Adress"]))


def import_file():
    filelist = get_file_dox()

    values = [(item["Name"], item["Extension"], item["Adress"])
              for item in filelist]

    for n, e, a in values:
        shortname = verify_existed_file(n)

        commit = {shortname: {"Name": n, "Extension": e, "Adress": a}}

        data.update(commit)
        with open("lib/log.json", "w") as file:
            json.dump(data, file, indent=4)

    refresh_tv(tv, data)

# Widgets


def pull_to_workspace(tv: ttk.Treeview):
    focused_item = tv.focus()
    if focused_item:
        itemlog = tv.item(focused_item, "values")

        name = itemlog[1]
        ext = itemlog[2]
        path = itemlog[3]  
        
        add_element(name, ext, path)
    else:
        print("Nenhum item está ativo.")

search_bar = ttk.Entry(tab1, width=19)
search_bar.place(x=805, y=20)
sort_btn = ttk.Button(tab1, text="Sortering", image=sort_tk)
sort_btn.place(x=805, y=55)

file_btn = ttk.Button(tab1, text="Add File", image=folder_tk,
                      command=import_file)
file_btn.place(x=850, y=55)

add_btn = ttk.Button(tab1, image=plus_tk, width=4,
                     compound="center", style="Accent.TButton", command=lambda: pull_to_workspace(tv))
add_btn.place(x=920, y=55)

sort_btn.bind("<ButtonRelease-1>", remove_focus)
file_btn.bind("<ButtonRelease-1>", remove_focus)
add_btn.bind("<ButtonRelease-1>", remove_focus)

tv = ttk.Treeview(tab1, columns=("name"), show="headings")
tv.column("name", minwidth=50, width=50)
tv.heading("name", text="Aa-Zz")

tv.place(width=170, height=440, x=805, y=90)

refresh_tv(tv, data)

# *Workspace
cont = ttk.Labelframe(tab1, text="Workspace")
cont.place(x=210, y=60, height=470, width=580)

canvas = Canvas(cont)
canvas.pack(fill=BOTH, expand=True, padx=1, pady=(0, 3))

canvas_frame = Frame(canvas)
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

def add_element(name, ext, path):
    global current_row, current_col

    if current_col == MAX_COLS:
        current_col = 0
        current_row += 1

    # Criação do item que será adicionado à app_list
    item = {
        "id": len(applist),  
        "name": name,
        "ext": ext,
        "path": path
    }

    # Adicionando o item na lista
    applist.append(item)

    element = ttk.Frame(canvas_frame)
    element.grid(row=current_row, column=current_col, padx=8, pady=10)

    url = get_icon(ext)
    image = ImageTk.PhotoImage(Image.open(url).resize((90, 90)))

    lbl = Label(element, image=image)
    lbl.image = image
    lbl.pack(padx=2, pady=2)

    text = ttk.Label(element, text=name, font=("Arial", 13), background="gray", padding=(5, 0))
    text.pack(padx=2, pady=10)

    text.bind("<MouseWheel>", on_mouse_wheel)
    element.bind("<MouseWheel>", on_mouse_wheel)
    lbl.bind("<MouseWheel>", on_mouse_wheel)

    # Atualiza o canvas
    current_col += 1
    canvas_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def on_mouse_wheel(event):
    if current_row <= 2:
        return
    delta = -1 * (event.delta // 120)

    canvas.yview_scroll(delta, "units")


canvas_frame.bind("<MouseWheel>", on_mouse_wheel)

add_btn = ttk.Button(tab1, text="Adicionar Elemento",)
add_btn.place(x=250, y=450)

# Operations
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

# *Properties
name_entry = ttk.Entry(tab1, width=15)
name_entry.place(x=35, y=20)

prop_frame = ttk.Labelframe(tab1, width=175, height=470, text="Properties")
prop_frame.place(x=20, y=60)
prop_frame.bind("<ButtonRelease-1>", remove_focus)

# Exe
sv_ttk.use_dark_theme()
window.mainloop()
