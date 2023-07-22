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

# função locate() não implementada / function locate() not implemented
def locate(img):
    pyautogui.locateOnScreen(img, confidence=0.6)

def press_key(tecla):
    win32api.keybd_event(tecla, 0, 0, 0)
    time.sleep(0.1)  # Tempo de espera (em segundos)
    win32api.keybd_event(tecla, 0, win32con.KEYEVENTF_KEYUP, 0)

def wait(w):
    time.sleep(w)

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
