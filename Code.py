from tkinter import *
from tkinter import ttk

# Color palette
light1 = "#60C7FB"
light2 = "#FFFFFF"
dark1 = "#2E2E2E"
dark2 = "#1C1C1C"

# Window
window = Tk()
window.geometry("800x500")
window.title("AutoLauncher")
window.configure(bg=dark2)

# Pré-Styled Class


class StyledButton(Button):
    def __init__(self, parent, text, command=None):
        super().__init__(parent, text=text, bg=dark1, fg="white", padx=10,
                         pady=5, font=("Arial", 10, "bold"), command=command)


# **Screens**
# Home Screen
Home_Screen = Frame(window, bg=dark2)
Home_Screen.place(relheight=1, relwidth=1)

# Sandbox Screen
Sandbox_Screen = Frame(window, bg=dark2)

# **Home Screen Context**
preset_container = Frame(Home_Screen, width=400, height=200)
preset_container.place(relx=0.5, rely=0.5, anchor="center")
preset_container.configure(
    bg=dark2, highlightbackground=dark1, highlightthickness=2)

notice = Label(preset_container, text="No presets available.")
notice.place(relx=0.5, rely=0.5, anchor="center")

# Buttons


def go_to_sandbox():
    Home_Screen.place_forget()
    Sandbox_Screen.place(relheight=1, relwidth=1)


def go_to_home():
    Sandbox_Screen.place_forget()
    Home_Screen.place(relheight=1, relwidth=1)


more_button = Button(window, text="+", font=("Arial", 12,
                     "bold"), width=1, height=1, command=go_to_sandbox)
edit_button = Button(window, text="Edit", font=(
    "Arial", 12, "bold"), width=3, height=1)

more_button.place(in_=preset_container, relx=1, y=-40, anchor="ne")
edit_button.place(in_=preset_container, relx=0.9, y=-40, anchor="ne")

# **Sandbox Screen**
tab_row = Frame(Sandbox_Screen, bg=dark1,
                highlightbackground=dark2, highlightthickness=3, height=40)
tab_row.pack(fill=X, side=TOP)

workspace = Frame(Sandbox_Screen, bg=dark2)
workspace.pack(fill=BOTH, expand=True)

workspace.grid_rowconfigure(0, weight=1)
# Permite expansão apenas no App Space
workspace.grid_columnconfigure(1, weight=1)

# Tabs
tab_New = StyledButton(tab_row, text="New Preset")
tab_Preferences = StyledButton(tab_row, text="Preferences")

tab_New.config(bg=dark2)
tab_New.pack(side=LEFT, padx=10, pady=5)
tab_Preferences.pack(side=LEFT, padx=10, pady=5)

# Back Button
backButton = Button(tab_row, text="Back to Home", bg=dark1,
                    fg=light2, command=go_to_home)
backButton.pack(side=RIGHT, padx=10, pady=5)

# Workspace
properties_container = Frame(
    workspace, width=200, bg=dark2, highlightbackground=dark1, highlightthickness=1)
properties_container.grid(row=0, column=0, sticky="ns")

workspace_center = Frame(workspace, bg=dark2,
                         highlightbackground=dark1, highlightthickness=1)
workspace_center.grid(row=0, column=1, sticky="nsew")

explorer_container = Frame(
    workspace, width=200, bg=dark2, highlightbackground=dark1, highlightthickness=1)
explorer_container.grid(row=0, column=2, sticky="ns")

# *Properties*

# Name
name_entry = Entry(properties_container, width=20, bg=dark1, fg=light2)
name_entry.pack(side=TOP, pady=20, padx=20, ipadx=5, ipady=5)

# Attributes
prptsFrame = Canvas(properties_container, bg=dark2)
prptsFrame.pack(side=RIGHT, padx=10, pady=20, fill=BOTH, expand=True)

# >Scroll
scrollbar = Scrollbar(
    prptsFrame, orient="vertical", command=Canvas.yview, width=2)
prptsFrame.configure(yscrollcommand=Scrollbar.set)

scrollbar.pack(side='left', fill=Y, padx=(5, 10), pady=5)


# *App Space*

# Topbar
launch_methods = ["Simple", "Timed"]
top_bar = Frame(workspace_center, bg=dark1)
top_bar.pack(side=TOP, padx=10, pady=10, fill=BOTH)

# Type
type = ttk.Combobox(top_bar, values=launch_methods)
type.set(launch_methods[0])
type.pack(side='left', padx=5, pady=5)

# Desk
desk = Frame(workspace_center, bg=dark2,
             highlightbackground=dark1, highlightthickness=1)
desk.pack(side=TOP, padx=10, pady=(10, 20), fill=BOTH, expand=True)

# *Explorer*

# Search and Files Order
search_bar = Entry(explorer_container, bg=dark1, fg=light2)
search_bar.place(anchor='center', relwidth=0.6, y=20, x=80)

add_path = Button(explorer_container, bg=dark1, text="+", width=1, height=1)
add_path.place(anchor=CENTER, x=160, y=20)

order_button = Button(explorer_container, bg=dark1,
                      text="Tt", width=1, height=1)
order_button.place(anchor=CENTER, x=180, y=20)

# Files
files = Canvas(explorer_container, bg=dark2)
files.place(width=180, height=365, y=60, x=10)

window.mainloop()
