# task 1

"""Реалізуйте клас «Автомобіль».
Збережіть у класі: назву моделі, рік випуску, виробника, об’єм двигуна, колір машини, ціну.
Реалізуйте методи класу для введення-виведення даних та інших операцій."""


class Auto:
    def __init__(self, name_model, year, creator, capacity, color, price):
        self.name_model = name_model
        self.year = year
        self.creator = creator
        self.capacity = capacity
        self.color = color
        self.price = price

    def change_price(self, new_price):
        self.price = new_price
        return self.price

    def how_old_is_auto(self, present_year):
        return present_year - self.year

    def __str__(self):
        return f'INFO ABOUT AUTO\n{self.name_model} {self.year} by {self.creator}\n' \
               f'Engine capacity: {self.capacity}\nColor: {self.color}\nPrice: {self.price}'


toyota = Auto(name_model='RAV4', year=2020, creator='Toyota', capacity=2000, color='white', price=1_200_000)
# print(toyota.change_price(2_000_000))
# print(toyota.how_old_is_auto(2022))
# print(toyota)


# task 2

"""Реалізуйте клас «Книга». 
Збережіть у класі: назву книги, рік видання, видавця, жанр, автора, ціну.
Реалізуйте методи класу для введення-виведення даних та інших операцій."""


class Book:
    def __init__(self, name, year, publisher, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.author = author
        self.price = price
        self.genre = []

    def add_genre(self, *args):
        for genre in args:
            self.genre.append(genre)

    def __str__(self):
        return f'INFO ABOUT BOOK\n"{self.name}" by {self.author}\nPublished in {self.year} by {self.publisher}\n' \
               f"Genre: {', '.join(self.genre)}\nPrice: {self.price}$"


book = Book('1984', 1949, 'Secker & Warburg', 'George Orwell', 15)
book.add_genre(	'Dystopian', 'political fiction')
book.add_genre('social science fiction')
# print(book)


# task 3

"""Реалізуйте клас «Стадіон». 
Збережіть у класі: назву стадіону, дату відкриття, країну, місто, місткість.
 Реалізуйте методи класу для введення-виведення даних та інших операцій."""


class Stadium:
    def __init__(self):
        self.name = 'not given'
        self.date_of_open = 'not given'
        self.country = 'not given'
        self.city = 'not given'
        self.capacity = 'not given'

    def change_name(self, name):
        self.name = name
        return self.name

    def change_date_of_open(self, date):
        self.date_of_open = date
        return self.date_of_open

    def change_country(self, country):
        self.country = country
        return self.country

    def change_city(self, city):
        self.city = city
        return city

    def change_capacity(self, capacity):
        self.capacity = capacity
        return capacity

    def __str__(self):
        return f'INFO ABOUT STADIUM\nName: {self.name}\nDate of opening: {self.date_of_open}\n' \
               f'Place: {self.country}, {self.city}\nCapacity: {self.capacity}'


stadium = Stadium()
stadium.change_name('Juvileiniy')
stadium.change_city('Sumy')
stadium.change_country('Ukraine')
stadium.change_capacity(10_000)
# print(stadium)
