class STATUS:
    LOADING = "Загрузка.."
    VIRIFY = "Верификация.."
    LOAD = "Загружено"
    QUEUE = "В Очереди "
    RUNNING = "Выполнение.."
    COMPLETE = "Завершено"
    ERROR = "Ошибка.."
    ERRVERY = "Ошибка вер.."


RESULTS: str = "results"
RESULT: str = "result"

PRIORITY: dict = {
    "Высокий": 1,
    "Средний": 2,
    "Низкий": 3,
    "Смешанный": 4,
}

PRIORITY_V: dict = {
    1: "Высокий",
    2: "Средний",
    3: "Низкий",
    4: "Смешанный",
}

NOT_WORK: list = ["Запущена", "Завершена", "Провалена"]
