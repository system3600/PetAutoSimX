from Aux_main import Basic_Utils as ut
import tkinter as tk
from termcolor import *

def auto_egg_open():
    ut.auto_egg()
    print("Auto Egg Open ativado!")

def anti_afk():
    ut.anti_afk()
    print("Anti AFK ativado!")

def auto_click_gui():
    print("tempo padrão de 1.5 segundos por click")
    t = 1.5
    ut.auto_click(t)

def about():
    print('Versão atual: Beta 0.0.2\nBuild: Publica\n data de lançamento: 21/07/2023')
    cprint('Feitor por : EXNOP#1293', 'light_magenta')

def sair():
    root = tk.Tk()
    root.destroy()


def interface():
    root = tk.Tk()
    root.title("PetAutoSimulatorX BETA")
    root.geometry("275x200")
    root.configure(background='gray')

    bg_image = tk.PhotoImage(file="C:\\Users\\Administrator\\PycharmProjects\\AutoPetSimX\\Images\\pet.png")
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    auto_egg_image = tk.PhotoImage(file="C:\\Users\\Administrator\\PycharmProjects\\AutoPetSimX\\Images\\AUTO EGG OPEN.png")
    anti_afk_image = tk.PhotoImage(file="C:\\Users\\Administrator\\PycharmProjects\\AutoPetSimX\\Images\\Anti Afk.png")
    auto_click_image = tk.PhotoImage(file="C:\\Users\\Administrator\\PycharmProjects\\AutoPetSimX\\Images\\auto click.png")
    about_image = tk.PhotoImage(file="C:\\Users\\Administrator\\PycharmProjects\\AutoPetSimX\\Images\\ABOUT.png")
    exit_image = tk.PhotoImage(file="C:\\Users\\Administrator\\PycharmProjects\\AutoPetSimX\\Images\\EXIT.png")
    comandos_image = tk.PhotoImage(file=("C:\\Users\\Administrator\\PycharmProjects\\AutoPetSimX\\Images\\comandos.png"))

    titulo_label = tk.Label(root, text="Comandos:", font=("Helvetica", 16), image=comandos_image)
    titulo_label.grid(row=0, column=3, pady=5,)

    auto_egg_button = tk.Button(root, image=auto_egg_image, command=auto_egg_open)
    auto_egg_button.grid(row=1, column=0, pady=3)

    anti_afk_button = tk.Button(root, image=anti_afk_image, command=anti_afk)
    anti_afk_button.grid(row=1, column=3, pady=3)

    auto_click_button = tk.Button(root, image=auto_click_image, command=auto_click_gui)
    auto_click_button.grid(row=1, column=5, pady=5)

    about_button = tk.Button(root, image=about_image, command=about)
    about_button.grid(row=2, column=0, pady=5)

    exit_button = tk.Button(root, image=exit_image, command=sair)
    exit_button.grid(row=2, column=5, pady=5)

    root.mainloop()