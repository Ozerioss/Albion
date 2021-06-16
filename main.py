import time
from pathlib import Path

import pyautogui
import pyautogui as gui


def position_test():
    position = gui.position()
    return position


def locate_enemy_health_bar():
    enemy_healthbar = Path("assets/health_bar.png")
    print(enemy_healthbar)
    while True:
        # TODO : optimize where to look on screen
        # TODO : maybe add a check on healthbar color ?
        if pyautogui.locateOnScreen(str(enemy_healthbar)) is None:
            print("No enemy nearby")
            time.sleep(0.5)
        else:
            print("ENEMY SPOTTED")
            time.sleep(1)


if __name__ == "__main__":
    locate_enemy_health_bar()
