from Aux_main import Basic_Utils
from Aux_main import gui
from termcolor import *
import time
# opencv-python

cprint(' ===== PetAutoSimX Beta 0.0.1 =====', 'green')
print('Para conseguir atualizações visite: https://github.com/system3600/PetAutoSimX/edit/main/README.md')
print('To get updates visit: https://github.com/system3600/PetAutoSimX/edit/main/README.md\n ')
time.sleep(1)

def main():
    lang = int(input('selecione a linguagem do programa / select program language \n1)BR\n2)EN\n> '))
    mode = int(input('Ativar GUI ? / activate GUI ? \n1)sim/yes \n2)não/no'))

    if mode == 1:
        gui.interface()
    if mode == 2:
        if lang == 1:
            print('A linguagem atual é : PT-BR')
            opr = int(input('Selecione a operação \n1)auto egg open \n2)afk \n3)auto click \n4)Sobre \n5)Sair\n> '))
            if opr == 1:
                cprint('AVISO : para funcionar corretamente o roblox precisa estar ABERTO', 'light_red')
                print('Para parar o auto egg pressione q ')
                Basic_Utils.auto_egg()
            if opr == 2:
                cprint('AVISO : para funcionar corretamente o roblox precisa estar ABERTO', 'light_red')
                print('Para parar o afk pressione q ')
                Basic_Utils.anti_afk()
            if opr == 3:
                t = float(input('especifique o tempo entre os clicks\n> '))
                Basic_Utils.auto_click(t)
            if opr == 4:
                print('Versão atual: 0.0.2\nBuild: Publica\ndata de lançamento: 21/07/2023')
                cprint('Feito por : EXNOP#1293', 'light_magenta')
                time.sleep(4)
                main()
            if opr == 5:
                print('Saindo do programa :)')
        if lang == 2:
            print('Actual language : en')
            opr = int(input('Select a  operation \n1)auto egg open \n2)afk \n3)auto farm \n4)about \n5)exit\n> '))
            if opr == 1:
                cprint('ATTENTION: to work correctly roblox needs to be OPEN', 'light_red')
                print('to stop auto egg press q ')
                Basic_Utils.auto_egg()
            if opr == 2:
                cprint('ATTENTION: to work correctly roblox needs to be OPEN', 'light_red')
                print('to stop afk press q ')
                Basic_Utils.anti_afk()
            if opr == 3:
                t = float(input('specify time between clicks\n> '))
                Basic_Utils.auto_click(t)
            if opr == 4:
                print('Current version: 0.0.2\nBuild: Publica\nlaunch date: 21/07/2023')
                cprint('made by : EXNOP#1293', 'light_magenta')
                time.sleep(4)
                main()
            if opr == 5:
                print('Exiting')
main()
