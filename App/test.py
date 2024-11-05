from tkinter import *

window = Tk()
window.geometry("800x600")

apps = []

# Criação do Canvas e da Scrollbar
canvas = Canvas(window, bg="gray")
scrollbar = Scrollbar(window, orient="vertical", command=canvas.yview)

# Configuração do Frame dentro do Canvas
frame_container = Frame(canvas, bg="white")

# Adiciona o Frame ao Canvas
canvas.create_window((0, 0), window=frame_container, anchor="nw")

# Configura a Scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Função para atualizar a largura do Canvas quando o frame mudar


def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


canvas.bind("<Configure>", on_configure)


def on_mouse_wheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")


canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Empacotando o Canvas e a Scrollbar
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)


def refresh_list():
    # Limpa o grid para atualizar a posição dos frames
    for widget in frame_container.winfo_children():
        widget.grid_forget()  # Remove o widget do grid

    # Adiciona os frames de volta ao grid
    for i, app in enumerate(apps):
        app.grid(row=i // 3, column=i % 3, padx=5, pady=5)

    # Atualiza a scrollregion do canvas para incluir todos os widgets
    frame_container.update_idletasks()  # Atualiza a geometria dos widgets
    canvas.configure(scrollregion=canvas.bbox("all")
                     )  # Define a região de rolagem


def add_new_frame():
    new_frame = Frame(frame_container, bg="blue", width=100, height=100)
    apps.append(new_frame)
    refresh_list()


button = Button(window, text="Add Frame", command=add_new_frame)
button.pack(side=TOP)

# Adicionando frames iniciais
frame1 = Frame(frame_container, bg="black", width=100, height=100)
frame2 = Frame(frame_container, bg="black", width=100, height=100)
frame3 = Frame(frame_container, bg="black", width=100, height=100)

apps.append(frame1)
apps.append(frame2)
apps.append(frame3)

# Configuração dos frames iniciais no grid
refresh_list()

# Força o Canvas a ajustar a região de rolagem no início
frame_container.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"))

window.mainloop()
