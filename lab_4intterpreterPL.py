class AirCastle:
    def __init__(self, height, clouds, color):
        self.height = height  
        self.clouds = clouds  
        self.color = color    

    def change_height(self, value):
        self.height = max(0, self.height + value)

    def __add__(self, n):
        self.clouds += n
        self.height += n // 5
        return self

    def __call__(self, transparency):
        if transparency <= 0:
            raise ValueError("Прозрачность должна быть положительным целым числом.")
        return (self.height // transparency) * self.clouds

    def __str__(self):
        return f"Воздушный замок на высоте {self.height} метров, цвет: {self.color}, облаков: {self.clouds}."

    def __lt__(self, other):
        if self.clouds != other.clouds:
            return self.clouds < other.clouds
        if self.height != other.height:
            return self.height < other.height
        return self.color < other.color


class PaintedAirCastle(AirCastle):
    def __init__(self, height, clouds, color, pattern):
        super().__init__(height, clouds, color) 
        self.pattern = pattern  # Инициализация узора

    def __str__(self):
        return f"Раскрашенный воздушный замок на высоте {self.height} метров, цвет: {self.color}, облаков: {self.clouds}, узор: '{self.pattern}'."
    
if __name__ == "__main__":
    print("Создание обычного замка:")
    castle = AirCastle(height=100, clouds=10, color="белый")
    print(castle)
    
    print("\nИзменение высоты замка:")
    castle.change_height(20) 
    print(castle)  

    castle.change_height(-50)  
    print(castle) 

    print("\nПроверка минимальной высоты:")
    castle.change_height(-100)
    print(castle) 

    print("\nДобавление облаков:")
    castle + 5
    print(castle)

    # Проверка видимости
    print("\nПроверка видимости:")
    visibility = castle(5)
    print(f"Видимость: {visibility}")

    another_castle = AirCastle(height=50, clouds=10, color="черный")
    print("\nСравнение двух замков:")
    print(castle < another_castle) 

    print("\nСоздание раскрашенного замка:")
    painted_castle = PaintedAirCastle(height=150, clouds=20, color="синий", pattern="полосатый")
    print(painted_castle)

    print("\nИзменение высоты раскрашенного замка:")
    painted_castle.change_height(-30)
    print(painted_castle)

    print("\nДобавление облаков в раскрашенный замок:")
    painted_castle + 15
    print(painted_castle) 

    print("\nПроверка видимости раскрашенного замка:")
    visibility = painted_castle(10) 
    print(f"Видимость: {visibility}")  

    print("\nСравнение раскрашенного замка с обычным замком:")
    print(painted_castle < castle)
