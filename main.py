import time
from pathlib import Path

import pyautogui


def locate_enemy_health_bar(enemy_health_bar: Path):
    while True:
        # TODO : optimize where to look on screen
        # TODO : maybe add a check on healthbar color ?
        if pyautogui.locateOnScreen(str(enemy_health_bar), confidence=0.79, grayscale=True) is None:
            print("No enemy nearby")
            time.sleep(0.2)
        else:
            print("ENEMY SPOTTED")
            run_action("r")
            break


def run_action(action: str):
    pyautogui.press(action)
    print(f"Pressed {action}")


if __name__ == "__main__":
    locate_enemy_health_bar(Path("assets/health_bar_flagged.png"))
