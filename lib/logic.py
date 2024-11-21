from tkinter import *
from tkinter import ttk
from random import randint
from tkinter import filedialog
import os
import json
from PIL import Image, ImageTk

# MÉTODOS | METHODS

# refresh_lb : Atualiza a listbox com os itens da lista fornecida
# print_lb_active : Imprime o item ativo em uma listbox
# print_lb_sel : Imprime todos os itens selecionados em uma listbox
# add_item_to_lb : Adiciona um novo item à uma lista 
# open_file : Abre uma janela para seleção de arquivos e retorna os endereços dos arquivos
# file_to_lb :  Usa o metodo anterior (open_file) e adiciona os arquivos a listbox

# Functions
def refresh_lb(listbox, item_list):
    listbox.delete(0, listbox.size())
    for a in item_list:
        listbox.insert(END, a)

def print_lb_active(listbox):
    print(listbox.get(ACTIVE))

def print_lb_sel(listbox):
    selected_items = [listbox.get(i) for i in listbox.curselection()]  
    print("Itens selecionados:", selected_items)

def add_item_to_lb(item_list, listbox, name=None):
    if name is None:
        name = str(randint(1, 10))
    item_list.append(name)  
    refresh_lb(listbox, item_list)

# Explorer
def get_file():
    filetypes = (("All", "*.png *.jpeg, *.jpg, *.exe"), ("PNG", "*.png"), ("JPEG", "*.jpeg, *.jpg"), ("EXE", "*.exe"))
    filenames = filedialog.askopenfilenames(initialdir="C:\\", title="Select a file", filetypes=filetypes)
    
    return filenames

def get_icon(file_type):
    # gallery
    icon_gallery = {
        "png": "lib/source/image.png",
        "jpeg": "lib/source/image.png",
        "jpg": "lib/source/image.png",
        "mp3": "lib/source/audio.png",
        "wav": "lib/source/audio.png",
        "exe": "lib/source/exe.png"}

    return icon_gallery.get(file_type, "lib/source/file.png")

def get_file_dox():
    files = get_file()
    logs = []

    for file in files:
        file_name = os.path.basename(file)
        file_type = os.path.splitext(file_name)[1][1:]
        file_name = os.path.splitext(file_name)[0]

        log = {"Name": file_name, "Extension" : file_type, "Adress" : file}
        
        logs.append(log)
        # Carregar e redimensionar a imagem
        #icon_path = get_icon(file_type)
        #icon_img = Image.open(icon_path).resize((20, 20))
        #icon_photo = ImageTk.PhotoImage(icon_img)

    return logs

def print_tv_active(tree : ttk.Treeview):
    print(tree.bind(ACTIVE))

def verify_existed_file(name):
    # Listar todos os pares de Nome no JSON (não importa a extensão para renomeação)
    with open("lib/log.json") as file:
        data = json.load(file)
    
    values_Name = [item['Name'] for item in data.values()]
    
    
    # Verificar se o nome base já existe
    reformated_name = name
    contador = values_Name.count(name)
    
    if contador >0:
        reformated_name = f"{name}({contador})"
    else:
        reformated_name = name

    # Retornar o nome único
    return reformated_name

# Workspace
