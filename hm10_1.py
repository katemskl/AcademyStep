#task 1

"""Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
название модели, год выпуска, производителя, объем двигателя, цвет
машины, цену. Реализуйте методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса."""


class Car:
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name')
        self.__year = kwargs.get('year of issue')
        self.__creator = kwargs.get('creator')
        self.__fuel = kwargs.get('fuel volume')
        self.__color = kwargs.get('color')
        self.__price = kwargs.get('price')

    def __repr__(self):
        return f'Name of the model: {self.__name}, {self.__year} year of issue;\n' \
               f'Creator: {self.__creator}\nFuel volume: {self.__fuel}\nColor of car: {self.__color}\n' \
               f'Price: {self.__price}'
