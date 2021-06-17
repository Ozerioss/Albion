import time
from pathlib import Path

import keyboard
import pyautogui

from Action import Action


def locate_enemy_health_bar(enemy_health_bar: Path, confidence: float = 0.9):
    # TODO : optimize where to look on screen
    # TODO : maybe add a check on healthbar color ?
    if (
        pyautogui.locateOnScreen(
            str(enemy_health_bar), confidence=confidence, grayscale=False
        )
        is None
    ):
        print("No enemy nearby")
        time.sleep(0.3)
        return False
    else:
        print("ENEMY SPOTTED")
        return True


def run_action(action: str):
    if action:
        pyautogui.press(action)
        print(f"Pressed {Action[action]}, mapped to button {action}")


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed(Action.stop_script):
            print("Stopping script")
            break
        is_located = locate_enemy_health_bar(
            Path("assets/health_bar_low_opacity.png"), confidence=0.778
        )
        if is_located:
            run_action(Action.chest_ability)
