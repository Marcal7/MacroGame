import pyautogui
import time
from pynput.keyboard import Key, Controller

# print(pyautogui.position())
def start_mission():
    time.sleep(1)
    pyautogui.press('e')
    pyautogui.click(848, 802)
    pyautogui.click()

def walk():
    time.sleep(1)
    #pyautogui.press('space')
    #pyautogui.press('space')
    pyautogui.keyDown("left")
    time.sleep(8)
    pyautogui.keyUp("left")
    pyautogui.keyDown("w")
    time.sleep(12)
    pyautogui.keyUp("w")

def power():
    time.sleep(1)
    pyautogui.press('5')

def volta():
    time.sleep(1)

def finish_mission():
    time.sleep(2)
    pyautogui.press('e')
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()

keyboard = Controller()

print('Começando em 5 segundos')
time.sleep(5)
print('Começando...')

with keyboard.pressed(Key.shift):
    # Pressiona e mantém a tecla 'w'
    keyboard.press('w')

    # Simula o tempo em que as teclas são mantidas pressionadas
    time.sleep(100)

    # Solta as teclas
    keyboard.release('w')


print('Finalizou o movimento.')

while True:
    time.sleep(0.2)
    pyautogui.click()


start_mission()
walk()
power()
volta()
finish_mission()