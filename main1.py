# from datetime import date
# #
# # class Number:
# #     def __init__(self, number):
# #         self.number = number
# #
# #     def __add__(self, other):
# #         return self.number + other.number
# #
# #     def __mul__(self, other):
# #         return self.number * other.number
# #
# #     def __truediv__(self, other):
# #         return self.number / other.number
# #
# #
# # num = Number(5)
# # num2 = Number(4)
# # num3 = Number(3)
# #
# # print(num / num2)
#
#
# class Human:
#     def __init__(self, **kwargs):
#         if Human.is_adult(kwargs.get('year')):
#             self.name = kwargs.get('name')
#             self.year = kwargs.get('year')
#
#     @staticmethod
#     def is_adult(age):
#         if age < 18:
#             print('You just a child')
#             return False
#         else:
#             return True
#
#     @classmethod
#     def from_birth_year(cls, age):
#         return cls(year=date.today().year - age)
#
#     def __repr__(self):
#         return f'Name: {self.name}, year: {self.year}'
#
#
# human = Human(name="mike", year=1999)
# print(human)
# # print(human.from_birth_year('mike', human.year))
# print(Human.from_birth_year(23))
# import time
#
#
# def decorator(iters):
#     def actual_decorator(func):
#         def wrapper(a):
#             for _ in range(iters):
#                 start = time.time()
#                 res = func(a)
#                 print(f'Status code of response is {res}')
#                 stop = time.time()
#                 print(f'Time - {(stop-start)} seconds')
#         return wrapper
#     return actual_decorator
#
#
# @decorator(iters=5)
# def hello(a):
#     return a
#
#
# hello('aa')

def same(list1, list_squ):
    flag = True
    for num in list1:
        flag = False
        if num ** 2 in list_squ:
            flag = True
    return flag


print(same([2, 5, 3], [9, 4, 25]))
print(same([1, 0, 5], [1, 2, 24]))
print(same([], []))

