class Vehicle:
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
    __COLOR_VARIANTS = ['white', 'BLACK', 'green', 'blue', 'red', 'yellow']

    def print_info(self):
        print(f"Владелец: {self.owner}")
        print(f"Модель: {self.__model}")
        print(f"Мощность двигателя: {self.__engine_power}")
        print(f"Цвет: {self.__color}")

    def set_color(self, new_color):
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
            print(f"Цвет изменен на {new_color}")
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['white', 'black', 'green', 'blue', 'red', 'yellow']
vehicle1 = Sedan('Maxim', 'Audi A4', 101, 'white')
# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()