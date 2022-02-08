# task 1
"""Создайте класс Device, который содержит информацию об устройстве.
С помощью механизма наследования, реализуйте
класс CoffeeMachine (содержит информацию о кофемашине),
класс Blender (содержит информацию о блендере),
класс MeatGrinder (содержит информацию о мясорубке).
Каждый из классов должен содержать необходимые для работы методы."""


class Device:

    def __init__(self, **kwargs):
        self.power = kwargs.get('power')
        self.guarantee = kwargs.get('guarantee')

    @staticmethod
    def work():
        return "I'm working now"


class CoffeeMachine (Device):

    def __init__(self, **kwargs):
        Device.__init__(self, **kwargs)
        self.types = kwargs.get('types')

    def __repr__(self):
        return f'Amount of energy consumed: {self.power} volt\nGuarantee period: {self.guarantee} year\n' \
               f'Amount of types of coffee it can make: {self.types}'

    def make_coffee(self, type_of_coffee):
        types_of_coffee = ['espresso', 'cappuccino', 'americano', 'latte',
                           'frappe', 'coffee with milk', 'iced coffee', 'irish coffee']
        if type_of_coffee in types_of_coffee[:self.types]:
            return f'Your {type_of_coffee} is done'
        else:
            return "Sorry, I can't make this one"


class Blender (Device):

    def __init__(self, **kwargs):
        Device.__init__(self, **kwargs)
        self.modes = kwargs.get('modes')

    def __repr__(self):
        return f'Amount of energy consumed: {self.power} volt\nGuarantee period: {self.guarantee} year\n' \
               f'Number of modes in this blender: {self.modes}'

    @staticmethod
    def mix():
        return "I mixed your cocktail"


class MeatGrinder(Device):

    def __init__(self, **kwargs):
        Device.__init__(self, **kwargs)
        self.nozzles = kwargs.get('nozzles')

    @staticmethod
    def twist(nozzle):
        return f'I work with nozzles {nozzle}'

    def __repr__(self):
        return f'Amount of energy consumed: {self.power} volt\nGuarantee period: {self.guarantee} year\n' \
               f'Number of nozzles in this meat grinder: {self.nozzles}'


device = Device(power=220, guarantee=4)
coffee_machine = CoffeeMachine(power=220, guarantee=2, types=5)
blender = Blender(power=220, guarantee=1, modes=3)
meat_grinder = MeatGrinder(power=220, guarantee=2, nozzles=2)
# print(coffee_machine)
# print(coffee_machine.make_coffee('espresso'))
# print(blender)
# print(blender.mix())
print(meat_grinder)
print(meat_grinder.twist('for sausages'))
