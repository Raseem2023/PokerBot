import pyautogui
from PIL import Image
from typing import Dict
from game_state import GameState

def capture_screenshot(region: tuple) -> Image:
    """
    Захват скриншота указанной области экрана.

    :param region: Координаты области (left, top, width, height).
    :return: Изображение области.
    """
    screenshot = pyautogui.screenshot(region=region)
    return Image.fromarray(screenshot)

def detect_changes(game_state: GameState) -> Dict[str, bool]:
    """
    Обнаружение изменений в областях экрана.

    :param game_state: Текущее состояние игры.
    :return: Словарь с результатами обнаружения изменений.
    """
    changes = {}
    for region_name, region_coords in game_state.regions.items():
        new_screenshot = capture_screenshot(region_coords)
        changes[region_name] = game_state.compare_screenshots(region_name, new_screenshot)
    return changes
