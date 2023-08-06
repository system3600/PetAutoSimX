# B.A.F (Basic Automation Framework) - framework de automação basica feita por exnop
# Versão do BAF utilizada no programa: 1.1 (devido a descontinuação do projeto o BAF não será mais atualizado e nem novas funções serão adicionadas)
# para conseguir mais informações e atualizações do BAF me adicione no discord: exnop


# Utilidades basicas de automação

import pyautogui
import time
import keyboard
import win32api, win32con

# funções auxiliares / aux functions

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

def clickun():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

def press_key(tecla):
    win32api.keybd_event(tecla, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(tecla, 0, win32con.KEYEVENTF_KEYUP, 0)

def wait(w):
    time.sleep(w)

def press_key1(key):
    win32api.keybd_event(key, 0, 0, 0)

def release_key1(key):
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

def keys(key1, key2, key3, key4):
    press_key1(key1)
    wait(5.5)
    release_key1(key1)

    press_key1(key2)
    wait(4.5)
    release_key1(key2)

    press_key1(key3)
    wait(5.5)
    release_key1(key3)

    press_key1(key4)
    wait(4.5)
    release_key1(key4)


# Funções principais / main functions

def auto_egg():
    wait(5)
    key = 0x045
    while keyboard.is_pressed('q') == False:
        press_key(key)
        click(821, 669)
        wait(2)
        print('auto egg running')

def anti_afk():
    wait(5)
    while keyboard.is_pressed('q') == False:
        key1 = 0x57
        key2 = 0x53
        press_key(key1)
        wait(1)
        press_key(key2)
        wait(1)
        print('anti afk running')

def auto_click(t):
    wait(5)
    while keyboard.is_pressed('q') == False:
        wait(t)
        clickun()
        print('auto click running.')

def event_farm():
    wait(5)
    keyap = 0x41
    keydp = 0x44
    keysp = 0x53
    keywp = 0x57
    while keyboard.is_pressed('q') == False:
        keys(keywp, keyap, keysp, keydp)
        wait(0.5)
        print('Event farm running..')
