import pytesseract
from PIL import Image

def ocr(image: Image) -> str:
    """
    Распознавание текста на изображении с помощью Tesseract.

    :param image: Изображение для распознавания.
    :return: Распознанный текст.
    """
    return pytesseract.image_to_string(image, config='--psm 6')

def detect_suit(color: tuple) -> str:
    """
    Определение масти карты по цвету.

    :param color: Цвет карты (RGB).
    :return: Масть карты ('hearts', 'spades', 'diamonds', 'clubs').
    """
    if color == (255, 0, 0):  # Красный
        return 'hearts'
    elif color == (0, 0, 0):  # Чёрный
        return 'spades'
    elif color == (255, 165, 0):  # Оранжевый
        return 'diamonds'
    elif color == (0, 0, 255):  # Синий
        return 'clubs'
    else:
        return 'unknown'

def log_action(action: str):
    """
    Запись действия в лог-файл.
    
    :param action: Действие для записи.
    """
    with open('bot_actions.log', 'a', encoding='utf-8') as f:
        f.write(action + "\n")
