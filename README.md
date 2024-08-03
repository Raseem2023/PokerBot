# PokerBot

PokerBot - это покерный бот с элементами HUD, который собирает и анализирует данные сессий, принимает решения на основе обученной модели машинного обучения и улучшает свою стратегию посредством самообучения.

## Структура проекта

```plaintext
PokerBot/
├── data/
│   ├── charts/
│   │   ├── preflop_chart.csv
│   │   ├── position_chart.csv
│   ├── session_data.json
├── src/
│   ├── __init__.py
│   ├── data_collection.py
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── decision_making.py
│   ├── player_analysis.py
├── main.py
├── requirements.txt
└── README.md
