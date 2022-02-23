# task 1

"""Задание 1
Создайте класс, содержащий набор целых чисел. В классе должна быть реализована следующая функциональность:
■ Сумма элементов набора.
■ Среднеарифметическое элементов набора.
■ Максимум из элементов набора.
■ Минимум из элементов набора.
Протестируйте все возможности созданного класса с помощью модульного тестирования(unittest)."""


class Numbers:
    def __init__(self, *args):
        self.list_numbers = args

    def sum(self):
        suma = 0
        for i in self.list_numbers:
            suma += i
        return suma

    def arithmetic_mean(self):
        return sum(self.list_numbers)//len(self.list_numbers)

    def max(self):
        maxi = self.list_numbers[0]
        for i in self.list_numbers:
            if i > maxi:
                maxi = i
        return maxi

    def min(self):
        mini = self.list_numbers[0]
        for i in self.list_numbers:
            if i < mini:
                mini = i
        return mini

    def __repr__(self):
        return f'{self.list_numbers}{type(self.list_numbers)}'


numbers = Numbers(1, 2, 3, 4, 5)


# task 2

"""Создайте класс для числа. В классе должна быть реализована следующая функциональность:
■ Запись и чтение значения.
■ Перевод числа в восьмеричную систему исчисления. 
■ Перевод числа в шестнадцатеричную систему исчисления.
■ Перевод числа в двоичную систему исчисления.
Протестируйте все возможности созданного класса с помощью модульного тестирования(unittest)."""


class Number:
    def __init__(self, number):
        self.number = number

    def octal_system(self):
        new_num = ''

        while self.number > 0:
            new_num = str(self.number % 8) + new_num
            self.number //= 8

        return int(new_num)

    def hexadecimal_system(self):
        new_num = ''
        h = '0123456789ABCDEF'

        while self.number > 0:
            new_num = h[self.number % 16] + new_num
            self.number = self.number // 16
        return int(new_num)

    def binary_system(self):
        new_num = ''

        while self.number > 0:
            new_num = str(self.number % 2) + new_num
            self.number = self.number // 2

        return int(new_num)

    def __repr__(self):
        return f'{self.number}'


number = Number(20)

