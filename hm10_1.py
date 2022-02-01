#task 1

"""Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
название модели, год выпуска, производителя, объем двигателя, цвет
машины, цену. Реализуйте методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса."""


class Car:
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__year = kwargs.get('year_issue')
        self.__creator = kwargs.get('creator')
        self.__fuel = kwargs.get('fuel_volume')
        self.__color = kwargs.get('color')
        self.__price = kwargs.get('price')

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_year(self):
        return self.__year

    def set_year(self, new_year):
        self.__year = new_year

    def get_creator(self):
        return self.__creator

    def set_creator(self, new_creator):
        self.__creator = new_creator

    def get_fuel_volume(self):
        return self.__fuel

    def set_fuel_volume(self, new_fuel):
        self.__fuel = new_fuel

    def get_color(self):
        return self.__color

    def set_color(self, new_color):
        self.__color = new_color

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def __repr__(self):
        return f'Name of the model:{self.__creator} {self.__name}, {self.__year} year of issue;\n' \
               f'Fuel volume: {self.__fuel}\nColor of car: {self.__color}\n' \
               f'Price: {self.__price}'


car1 = Car(name='RAV-4', year_issue='2021', creator='Toyota', fuel_volume='1.8', color='white', price='920000')

print(car1)
