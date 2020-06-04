import pyautogui
from tkinter import *
import time
import win32api
import random
import keyboard

## Configuração
# Defina o limite horizontal: 5 significa no máximo 5 pixels para a esquerda ou para a direita a cada foto
horizontal_range =1
# Defina a quantidade mínima e máxima de pixels para mover o mouse a cada pixel
min_vertical =0.9
max_vertical =1
# Defina a quantidade mínima e máxima de tempo em segundos para esperar até mover o mouse novamente
min_firerate = 0.01
max_firerate = 0.02
# Defina o botão de alternância
toggle_button = 'caps lock'
# Define se o anti-recuo está ativado por padrão
enabled = False


def is_mouse_down():  #Retorna true se o botão esquerdo do mouse é pressionado
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0





# Alguns prints para inicialização
print("Anti-recoil | script iniciado!")
if enabled:
    print("Script Ativado")
else:
    print("Script Desativado")
time.sleep(5)
last_state = False
while True:
    key_down = keyboard.is_pressed(toggle_button)

     # Se o botão de alternância for pressionado, alterne o valor ativado e imprima
    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("Anti-recoil ENABLED")
            else:
                print("Anti-recoil DISABLED")

    if is_mouse_down() and enabled:
        # As compensações são geradas a cada disparo entre as configurações mín e máx.
        offset_const = 1000
        horizontal_offset = random.randrange(-horizontal_range * offset_const, horizontal_range * offset_const,
                                             1) / offset_const
        vertical_offset = random.randrange(min_vertical * offset_const, max_vertical * offset_const, 1) / offset_const

        # Mova o mouse com esses deslocamentos
        win32api.mouse_event(0x0001, int(horizontal_offset), int(vertical_offset))

        # Gera deslocamento de tempo aleatório com as configurações
        time_offset = random.randrange(min_firerate * offset_const, max_firerate * offset_const, 1) / offset_const
        time.sleep(time_offset)

        pyautogui.click(clicks=4)
        pyautogui.click(clicks=4)
    # Atraso no loop while
    time.sleep(0.001)