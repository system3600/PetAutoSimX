from Aux_main import Basic_Utils
from termcolor import *
import time
# opencv-python

cprint(' ===== PetAutoSimX Beta 0.0.1 =====', 'green')
print('Para conseguir atualizações visite: https://github.com/system3600/PetAutoSimX/edit/main/README.md')
print('To get updates visit: https://github.com/system3600/PetAutoSimX/edit/main/README.md\n ')
time.sleep(1)

def main():
    lang = int(input('selecione a linguagem do programa / select program language \n1)BR\n2)EN\n> '))

    if lang == 1:
        print('A linguagem atual é : PT-BR')
        opr = int(input('Selecione a operação \n1)auto egg open \n2)afk \n3)auto farm \n4)Sobre \n5)Sair\n> '))
        if opr == 1:
            cprint('AVISO : para funcionar corretamente o roblox precisa estar ABERTO', 'light_red')
            print('Para parar o auto egg pressione q ')
            Basic_Utils.auto_egg()
        if opr == 2:
            cprint('AVISO : para funcionar corretamente o roblox precisa estar ABERTO', 'light_red')
            print('Para parar o afk pressione q ')
            Basic_Utils.afk()
        if opr == 3:
            print('Não implementado.')
            time.sleep(2)
            main()
        if opr == 4:
            print('Versão atual: Beta 0.0.1\nBuild: Publica\n data de lançamento: 21/07/2023')
            cprint('Feitor por : EXNOP#1293', 'light_magenta')
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
            Basic_Utils.afk()
        if opr == 3:
            print('not implemented. ')
            time.sleep(2)
            main()
        if opr == 4:
            print('Current version: Beta 0.0.1\nBuild: Publica\n launch date: 21/07/2023')
            cprint('made by : EXNOP#1293', 'light_magenta')
            time.sleep(4)
            main()
        if opr == 5:
            print('Exiting')
main()
