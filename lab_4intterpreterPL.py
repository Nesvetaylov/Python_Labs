class AirCastle:
    def __init__(self, height, clouds, color):
        self.height = height  # Инициализация высоты замка
        self.clouds = clouds  # Инициализация количества облаков
        self.color = color    # Инициализация цвета замка

    def change_height(self, value):
        """Изменяет высоту замка на value, не позволяя высоте стать меньше нуля."""
        self.height = max(0, self.height + value)

    def __add__(self, n):
        """Прибавляет n облаков к замку и увеличивает высоту на n // 5."""
        self.clouds += n
        self.height += n // 5
        return self

    def __call__(self, transparency):
        """Возвращает значение видимости замка по формуле: высота // прозрачность * количество облаков."""
        if transparency <= 0:
            raise ValueError("Прозрачность должна быть положительным целым числом.")
        return (self.height // transparency) * self.clouds

    def __str__(self):
        """Возвращает строковое представление замка."""
        return f"Воздушный замок на высоте {self.height} метров, цвет: {self.color}, облаков: {self.clouds}."

    def __lt__(self, other):
        """Сравнение экземпляров класса по количеству облаков, высоте и цвету."""
        if self.clouds != other.clouds:
            return self.clouds < other.clouds
        if self.height != other.height:
            return self.height < other.height
        return self.color < other.color


class PaintedAirCastle(AirCastle):
    def __init__(self, height, clouds, color, pattern):
        super().__init__(height, clouds, color)  # Вызов конструктора родительского класса
        self.pattern = pattern  # Инициализация узора

    def __str__(self):
        """Возвращает строковое представление раскрашенного замка."""
        return f"Раскрашенный воздушный замок на высоте {self.height} метров, цвет: {self.color}, облаков: {self.clouds}, узор: '{self.pattern}'."
    
if __name__ == "__main__":
    # Пример использования класса AirCastle
    print("Создание обычного замка:")
    castle = AirCastle(height=100, clouds=10, color="белый")
    print(castle)  # Ожидаемый вывод: "Воздушный замок на высоте 100 метров, цвет: белый, облаков: 10."

    # Изменение высоты замка
    print("\nИзменение высоты замка:")
    castle.change_height(20)  # Увеличиваем высоту на 20
    print(castle)  # Ожидаемый вывод: "Воздушный замок на высоте 120 метров, цвет: белый, облаков: 10."

    castle.change_height(-50)  # Уменьшаем высоту на 50
    print(castle)  # Ожидаемый вывод: "Воздушный замок на высоте 70 метров, цвет: белый, облаков: 10."

    # Проверка, что высота не может стать меньше 0
    print("\nПроверка минимальной высоты:")
    castle.change_height(-100)  # Пытаемся уменьшить высоту на 100
    print(castle)  # Ожидаемый вывод: "Воздушный замок на высоте 0 метров, цвет: белый, облаков: 10."

    # Добавление облаков
    print("\nДобавление облаков:")
    castle + 5  # Добавляем 5 облаков
    print(castle)  # Ожидаемый вывод: "Воздушный замок на высоте 1 метров, цвет: белый, облаков: 15."

    # Проверка видимости
    print("\nПроверка видимости:")
    visibility = castle(5)  # Прозрачность 5
    print(f"Видимость: {visibility}")  # Ожидаемый вывод: "Видимость: 0"

    # Создание другого замка для сравнения
    another_castle = AirCastle(height=50, clouds=10, color="черный")
    print("\nСравнение двух замков:")
    print(castle < another_castle)  # Ожидаемый вывод: False, так как у castle больше облаков

    # Пример использования класса PaintedAirCastle
    print("\nСоздание раскрашенного замка:")
    painted_castle = PaintedAirCastle(height=150, clouds=20, color="синий", pattern="полосатый")
    print(painted_castle)  # Ожидаемый вывод: "Раскрашенный воздушный замок на высоте 150 метров, цвет: синий, облаков: 20, узор: 'полосатый'."

    # Изменение высоты раскрашенного замка
    print("\nИзменение высоты раскрашенного замка:")
    painted_castle.change_height(-30)  # Уменьшаем высоту на 30
    print(painted_castle)  # Ожидаемый вывод: "Раскрашенный воздушный замок на высоте 120 метров, цвет: синий, облаков: 20, узор: 'полосатый'."

    # Добавление облаков в раскрашенный замок
    print("\nДобавление облаков в раскрашенный замок:")
    painted_castle + 15  # Добавляем 15 облаков
    print(painted_castle)  # Ожидаемый вывод: "Раскрашенный воздушный замок на высоте 123 метров, цвет: синий, облаков: 35, узор: 'полосатый'."

    # Проверка видимости раскрашенного замка
    print("\nПроверка видимости раскрашенного замка:")
    visibility = painted_castle(10)  # Прозрачность 10
    print(f"Видимость: {visibility}")  # Ожидаемый вывод: "Видимость: 420"

    # Сравнение раскрашенного замка с обычным замком
    print("\nСравнение раскрашенного замка с обычным замком:")
    print(painted_castle < castle)  # Ожидаемый вывод: False, так как у painted_castle больше облаков