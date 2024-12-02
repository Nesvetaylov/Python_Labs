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
        self.pattern = pattern 

    def __str__(self):
        return f"Раскрашенный воздушный замок на высоте {self.height} метров, цвет: {self.color}, облаков: {self.clouds}, узор: '{self.pattern}'."
    
if __name__ == "__main__":
    print("Создание обычного замка:")
    castle = AirCastle(height=100, clouds=10, color="белый")
    print(castle)  

    castle.change_height(5) 
    print(castle)

    castle + 5 
    print(castle)

    visibility = castle(5)  
    print(f"Видимость: {visibility}") 
