import pyautogui

import time

import pyperclip

import keyboard



time.sleep(1) #Время - через сколько начнётся спам



def spam(text: str, amount: int):

    pyperclip.copy(text)

    for _ in range(amount):

        time.sleep(0.2) #скорость вставки сообщений

        keyboard.press_and_release('ctrl + v')

        pyautogui.press("enter")

spam("Выруби демку", 1000) #пишем сообщение и кол-во повторов
