from utils import ocr, detect_suit, log_action

class GameState:
    def __init__(self):
        self.current_street = 'preflop'  # Текущая улица
        self.our_turn = False  # Флаг нашего хода
        self.player_cards = []
        self.table_cards = []
        self.bets = []
        self.last_screenshot = None
        self.initial_chips = None  # Начальное количество фишек
        self.current_chips = None  # Текущее количество фишек

    def update_state(self, screenshot, changes):
        """
        Обновление состояния игры на основе скриншота и изменений.
        """
        self.detect_cards(screenshot)
        self.detect_bets(changes)
        self.check_current_street()
        self.update_chips(screenshot)
        log_action(f"Обновлено состояние игры: улица {self.current_street}, карты {self.player_cards} {self.table_cards}, ставки {self.bets}, фишки {self.current_chips}")

    def detect_cards(self, screenshot):
        """
        Распознавание карт на руках и на столе.
        """
        self.player_cards = [ocr(screenshot.crop(region)) for region in self.get_player_card_regions()]
        self.table_cards = [ocr(screenshot.crop(region)) for region in self.get_table_card_regions()]

    def detect_bets(self, changes):
        """
        Распознавание ставок оппонентов по изменениям в тексте.
        """
        for change in changes:
            recognized_text = ocr(change)
            if 'колл' in recognized_text.lower():
                self.bets.append('call')
            elif 'рейз' in recognized_text.lower():
                self.bets.append('raise')
            elif 'чек' in recognized_text.lower():
                self.bets.append('check')

    def check_current_street(self):
        """
        Определение текущей улицы по количеству карт на столе.
        """
        if len(self.table_cards) == 0:
            self.current_street = 'preflop'
        elif len(self.table_cards) == 3:
            self.current_street = 'flop'
        elif len(self.table_cards) == 4:
            self.current_street = 'turn'
        elif len(self.table_cards) == 5:
            self.current_street = 'river'

    def update_chips(self, screenshot):
        """
        Обновление количества фишек по скриншоту.
        """
        # Пример области, где отображаются фишки
        chips_region = (50, 50, 100, 30)  # Нужно настроить под конкретный стол
        chips_text = ocr(screenshot.crop(chips_region))
        try:
            self.current_chips = int(chips_text.strip())
        except ValueError:
            log_action(f"Не удалось распознать количество фишек: {chips_text}")

        if self.initial_chips is None:
            self.initial_chips = self.current_chips

    def record_final_results(self):
        """
        Запись результата игры в лог-файл (выигрыш или проигрыш).
        """
        result = "Выигрыш" if self.current_chips > self.initial_chips else "Проигрыш"
        log_action(f"Результат игры: {result}")
        log_action(f"Начальные фишки: {self.initial_chips}, Конечные фишки: {self.current_chips}")
        self.reset_game_state()

    def reset_game_state(self):
        """
        Сброс состояния игры перед началом новой раздачи.
        """
        self.current_street = 'preflop'
        self.our_turn = False
        self.player_cards = []
        self.table_cards = []
        self.bets = []
        self.initial_chips = None
        self.current_chips = None
