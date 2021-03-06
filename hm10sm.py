# task 1

class Fraction:
    cnt = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.cnt += 1

    @staticmethod
    def output_cnt():
        return Fraction.cnt

    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'


first = Fraction(2, 3)
second = Fraction(1, 5)
# print(first)
# print(first.output_cnt())

# task 2


"""Создайте класс для конвертирования температуры из Цельсия в Фаренгейт и наоборот. 
У класса должно быть два статических метода: для перевода из Цельсия в Фаренгейт и 
для перевода из Фаренгейта в Цельсий. Также класс должен считать количество подсчетов 
температуры и возвращать это значение с помощью статического метода."""


class Degrees:
    cnt = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        Degrees.cnt += 1
        return ((celsius * 9)/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        Degrees.cnt += 1
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def output_cnt():
        return Degrees.cnt


degree = Degrees
# print(degree.celsius_to_fahrenheit(10))
# print(degree.fahrenheit_to_celsius(10))
# print(degree.output_cnt())


# task 3

"""Создайте класс для перевода из метрической системы в английскую и наоборот. 
Функциональность необходимо реализовать в виде статических методов. Обязательно реализуйте перевод мер длины."""


class MetricSystem:

    @staticmethod
    def sm_to_in(sm):
        return sm / 2.54

    @staticmethod
    def m_to_ft(m):
        return m * 3.281

    @staticmethod
    def m_to_yard(m):
        return m * 1.094

    @staticmethod
    def km_to_mile(km):
        return km/1.609


class EnglishSystem:
    @staticmethod
    def in_to_sm(inches):
        return inches * 2.54

    @staticmethod
    def ft_to_m(ft):
        return ft / 3.281

    @staticmethod
    def yard_to_m(yard):
        return yard / 1.094

    @staticmethod
    def mile_to_km(mile):
        return mile * 1.609


meter = MetricSystem
english = EnglishSystem
# print(meter.sm_to_in(20))
# print(meter.m_to_ft(1))
# print(meter.m_to_yard(1))
# print(meter.km_to_mile(10))
# print(english.in_to_sm(34))
# print(english.ft_to_m(10))
# print(english.yard_to_m(20))
# print(english.mile_to_km(20))
