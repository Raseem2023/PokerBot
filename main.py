import time
from screenshot_handler import capture_screenshot, detect_changes
from game_state import GameState
from decision_maker import make_decision
from utils import log_action

game_state = GameState()

while True:
    current_screenshot = capture_screenshot()
    changes_detected, changes = detect_changes(current_screenshot, game_state.last_screenshot)

    if changes_detected:
        game_state.update_state(current_screenshot, changes)

        if game_state.is_our_turn():
            decision = make_decision(game_state)
            log_action(f"Бот принимает решение: {decision}")
            game_state.record_action(decision)

        if game_state.current_street == 'river' and game_state.table_cards:
            game_state.record_final_results()

        game_state.last_screenshot = current_screenshot

    time.sleep(1)
