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
        return f'Device is working'


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
# print(blender.work())
# print(blender.mix())
# print(meat_grinder)
# print(meat_grinder.twist('for sausages'))


# task 2

"""Создайте класс Ship, который содержит информацию о корабле.
С помощью механизма наследования, реализуйте 
класс Frigate (содержит информацию о фрегате), 
класс Destroyer (содержит информацию об эсминце), 
класс Cruiser (содержит информацию о крейсере).
Каждый из классов должен содержать необходимые для работы методы."""


class Ship:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.speed = kwargs.get('speed')
        self.fuel = kwargs.get('fuel')

    def sail(self):
        return f'{self.name} is sailing'


class Frigate(Ship):

    def __init__(self, **kwargs):
        Ship.__init__(self, **kwargs)
        self.weapons = kwargs.get('weapon')

    def attack(self, count_of_enemies):
        if self.weapons >= count_of_enemies:
            return 'The enemy is defeated'
        return 'You are defeated'

    def __repr__(self):
        return f'Name of the ship: {self.name}\nMax speed: {self.speed}\n' \
               f'Fuel: {self.fuel}\nNumber of weapons on board: {self.weapons}'


class Destroyer(Ship):

    def __init__(self, **kwargs):
        Ship.__init__(self, **kwargs)
        self.displacement = kwargs.get('displacement')

    def destroy_submarines(self, number_of_submarines):
        if self.displacement >= number_of_submarines:
            return 'The submarines is destroyed'
        return 'Not enough displacement'

    def __repr__(self):
        return f'Name of the ship: {self.name}\nMax speed: {self.speed}\n' \
               f'Fuel: {self.fuel}\nNumber of displacement: {self.displacement}'


class Cruiser(Ship):

    def __init__(self, **kwargs):
        Ship.__init__(self, **kwargs)
        self.capacity = kwargs.get('capacity')

    def __repr__(self):
        return f'Name of the ship: {self.name}\nMax speed: {self.speed}\n' \
               f'Fuel: {self.fuel}\tCapacity: {self.capacity}'


frigate = Frigate(name='Liberty', speed=300, fuel=250, weapon=400)
print(frigate)
print(frigate.attack(390))
destroyer = Destroyer(name='Violet', speed=200, fuel=300, displacement=800)
print(destroyer)
print(destroyer.destroy_submarines(60))
cruiser = Cruiser(name='Georgia', speed=350, fuel=900, capacity=800)
print(cruiser)
print(cruiser.sail())
