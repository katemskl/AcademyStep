# def angle_sun(time: str):
#     time_list = time.split(':')
#     hour = int(time_list[0])
#     minutes = int(time_list[1])
#     # points = {'hour': 15, 'minutes': 0.25}
#     if 18 < hour < 24 or 0 < hour < 6:
#         return 'I cant see the sun'
#     else:
#         return (hour - 6) * 15 + minutes * 0.25
#
#
# # print(angle_sun('05:59'))
# # print(angle_sun('07:30'))
# # print(angle_sun('12:00'))
# # print(angle_sun('18:00'))
#
#
# def dict_word(word: str):
#     dict_ret = dict()
#     word = word.lower()
#     for letter in word:
#         dict_ret[letter] = word.count(letter)
#     return dict_ret
#
#
# # print(dict_word('Hello'))
#
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
#
# c = dict(zip(a, b))
# print(c)


class Dog:
    def __init__(self, name, color, age, breed):
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

    def bark_bark(self):
        return f"I'm {self.name}. Bark-bark"

    def __str__(self):
        return f'{self.name}, {self.breed}, {self.color}, {self.age}'


# dog = Dog(name='Bobik', breed='Ovcharka', color='black', age='5')
# dog2 = Dog(name='Sharik', breed='Mops', color='white', age='10')

# print(dog.bark_bark())
# print(dog2.bark_bark())
# print(type(dog))
# print(type(Dog))


"""Завдання 1 Реалізуйте клас «Людина». 
Збережіть у класі: ПІБ, дату народження, контактний телефон, місто, країну, домашню адресу. 
Реалізуйте методи класу для введення-виведення даних та інших операцій."""


class Person:
    def __init__(self, full_name, date, city, country, phone):
        self.full_name = full_name
        self.age = date
        self.city = city
        self.country = country
        self.phone = phone

    def place_of_living(self):
        return f'I live in {self.city}'

    def change_city(self, new_city):
        self.city = new_city
        return self.city

    def birthday(self):
        self.age += 1
        return self.age


kate = Person('Kateryna', 16, 'Sumy', 'Ukraine', '123_456')
# print(kate.place_of_living())
# print(kate.change_city('Kyiv'))
# print(kate.birthday())


"""Створіть клас «Країна». Збережіть у класі: назву країни, назву континенту, 
кількість жителів країни, телефонний код країни, назву столиці, назву міст країни. 
Реалізуйте методи класу для введення-виведення даних та інших операцій."""


class Country:
    def __init__(self, name_country, count_citizen, capital_city, cities):
        self.name_country = name_country
        self.count_citizen = count_citizen
        self.capital_city = capital_city
        self.cities = cities

    def delete(self, del_info):
        self.cities.remove(del_info)
        return self.cities

    def add(self, add_city):
        self.cities.append(add_city)
        return self.cities

    def __str__(self):
        return f'Name of the country: {self.name_country}\nCount of citizen: {self.count_citizen}\n' \
               f"Capital of {self.name_country}: {self.capital_city}\n" \
               f"{self.name_country}'s cities: {', '.join(self.cities)}"


ukraine = Country('Ukraine', '3 Billion', 'Kyiv', ['Sumy', 'Odesa', 'Mexico'])

# print(ukraine)
# print(ukraine.delete('Mexico'))


class Puppy(Dog):
    def __init__(self, name, breed, age, color):
        super(Puppy, self).__init__(name, color, age, breed)

    def bark_bark(self):
        return f'I am {self.name}, i can`t bark'


puppy = Puppy(name='Dunkie', breed='Taksa', color='Brown', age='1')
# print(puppy.bark_bark())
# print(puppy)


class Bird:
    type_class = 'Bird'

    def fly(self):
        return f'I am {self.type_class}, i can fly'


class Horse:
    type_class = 'Horse'

    def run(self):
        return f'I am {self.type_class}, i can run'


class Pegasus(Bird, Horse):
    type_class = 'Pegasus'


bird = Bird()
horse = Horse()
my_pegasus = Pegasus()
# print(bird.fly())
# print(horse.run())
# print(my_pegasus.fly())
# print(my_pegasus.run())


"""Створіть клас Human, який міститиме інформацію про людину. 
За допомогою механізму успадкування реалізуйте 
клас Builder (містить інформацію про будівельника), 
клас Sailor (містить інформацію про моряка),
клас Pilot (містить інформацію про льотчика). Кожен із класів має містити необхідні для роботи методи."""


class Human:
    def __init__(self, name, age, place_work):
        self.name = name
        self.age = age
        self.place_work = place_work

    def human_can(self):
        return f'I`m {self.name}. I can everything\n'

    def __repr__(self):
        return


class Builder(Human):

    def human_can(self):
        return f'I`m {self.name}. I build\n'


class Sailor(Human):

    def sail(self):
        return f'I`m {self.name}. I sail\n'


class Pilot(Human):

    def fly(self):
        return f'I`m {self.name}. I fly\n'

    def __str__(self):
        return f'{self.name}, {self.age}, {self.place_work}'


# person = Human(name='Kate', age='16', place_work='student')
# builder = Builder(name='Bill', age='34', place_work='Builder')
# sailor = Sailor(name='Jack', age='27', place_work='Sailor')
# pilot = Pilot(name='Ivan', age='45', place_work='Pilot')
# print(pilot)
# pilot.__init__('Kevin', '45', 'Pilot')
# print(pilot)


class Passport:
    def init(self, num, name, country):
        self.num = num
        self.name = name
        self.country = country

    def str(self):
        return f'identify: {self.num}, name: {self.name}, country: {self.country}'


class ForeignPassport(Passport):
    def init(self, num, name, country):
        super().init(num, name, country)
        self.visa = []

    def str(self):
        return f'identify: {self.num}, name: {self.name}, country: {self.country}, ' \
               f'visa: {"".join(self.visa)}'

    def trip(self, country):
        self.visa.append(country)
        return self.visa


# pasport = Passport(1706257890, 'Mokil hogrid', 'Egipt')
# print(pasport)
# foriegn_passsport = ForeignPassport(1893230, 'mok', 'sha')
# print(foriegn_passsport.trip('Poland'))
# print(foriegn_passsport)

'''Створіть базовий клас «Тварина» та похідні класи: «Тигр», «Крокодил», «Кенгуру». 
Встановіть за допомогою конструктора ім’я кожної тварини та її характеристики. 
Створіть для кожного класу необхідні методи та поля.'''


class Animals:
    def __init__(self, kind, name, age):
        self.kind = kind
        self.name = name
        self.feed = []
        self.age = age

    def add_feed(self, food):
        self.feed.append(food)
        return self.feed

    def getting_food(self):
        return f'I`m {self.name}.'

    def __str__(self):
        return f'{self.kind}, {self.name}, {self.age}\n{", ".join(self.feed)}'


# animal = Animals('mammal', 'bear', '5')
# animal.add_feed('Fish')
# animal.add_feed('Meat')


# class Tiger(Animals):
#     def __init__(self, kind, name, age, teeth):
#         super(Tiger, self).__init__(kind, name, age)
#
#         self.teeth = teeth
#
#     def getting_food(self):
#         return f'I`m {self.name}. I hunt'


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_mark(self, mark):

        if mark == 4:
            return 'Excellent'
        elif mark == 3:
            return 'Good'
        elif mark == 2:
            return 'Enough'
        if mark == 1:
            return 'Bad'
        elif mark <= 0:
            return 'There is not such mark'


class SmallSchool(Student):
    def get_mark(self, mark):
        a = super()
        if 1 <= mark <= 3:
            return a.get_mark(1)
        elif 4 <= mark <= 6:
            return a.get_mark(2)
        elif 7 <= mark <= 9:
            return a.get_mark(3)
        elif 10 <= mark <= 12:
            return a.get_mark(4)


class School(Student):
    pass


class University(Student):
    def __init__(self, name, age, place_of_study):
        super(University, self).__init__(name, age)

        self.place_of_study = place_of_study


small = SmallSchool('bill', 9)
# print(small.get_mark(3))


def rectangle(width, height):
    for i in range(height):
        if i == 0 or i == height-1:
            print(' * ' * width)
        else:
            print(' * '+'   '*(width-2) + ' * ')


rectangle(8, 10)
