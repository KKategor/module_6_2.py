# Task "Изменять нельзя получать"


class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, color, engine_power):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    def get_model (self, __model):
        return __model
    def get_horsepower (self, __engine_power):
        return __engine_power
    def get_color (self, __color):
        return __color
    def print_info (self):
        print(f'Владелец:  {self.owner} \nМодель: {self.__model} \nЦвет: {self.__color} \nМощность двигателя: {self.__engine_power}')

    def set_color (self, new_color):
        self.new_color = str.lower(new_color)
        if self.new_color in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()