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
print(degree.celsius_to_fahrenheit(10))
print(degree.fahrenheit_to_celsius(10))
print(degree.output_cnt())
