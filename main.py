import time
from pathlib import Path
from Action import Action

import pyautogui


def locate_enemy_health_bar(enemy_health_bar: Path):
    # TODO : optimize where to look on screen
    # TODO : maybe add a check on healthbar color ?
    if pyautogui.locateOnScreen(str(enemy_health_bar), confidence=0.778, grayscale=False) is None:
        print("No enemy nearby")
        time.sleep(0.2)
        return False
    else:
        print("ENEMY SPOTTED")
        return True


def run_action(action: str):
    if action:
        pyautogui.press(action)
        print(f"Pressed {Action[action]}, mapped to button {action}")


if __name__ == "__main__":
    # TODO break out of the loop on key press
    while True:
        is_located = locate_enemy_health_bar(Path("assets/health_bar_low_opacity.png"))
        if is_located:
            run_action(Action.chest_ability)
            break


