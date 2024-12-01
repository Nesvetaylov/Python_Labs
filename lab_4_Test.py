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
    castle.change_height(5)  # Увеличиваем высоту на 5
    print(castle)

    # Добавление облаков
    castle + 5  # Добавляем 5 облаков
    print(castle)

    # Проверка видимости
    visibility = castle(5)  # Прозрачность 5
    print(f"Видимость: {visibility}")  # Ожидаемый вывод: 300
