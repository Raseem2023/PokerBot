def make_decision(game_state):
    """
    Принимает решение на основе текущего состояния игры.
    
    :param game_state: Объект GameState с текущим состоянием игры.
    :return: Строка с решением ('фолд', 'колл', 'рейз', 'чек').
    """
    # Пример стратегии на основе силы руки и позиции
    if game_state.current_street == 'preflop':
        if game_state.player_cards == ['A♠', 'A♦']:
            return 'raise'
        else:
            return 'fold'
    elif game_state.current_street == 'flop':
        if 'A♠' in game_state.table_cards:
            return 'bet'
        else:
            return 'check'
    # Добавить логику для терна и ривера
    
    return 'check'
