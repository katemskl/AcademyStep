"""
Создать класс, в котором нет возможности получить элемент
по индексу.
Реализованны методы
1. Добавить в стек.
2. Взять из стека
3. Просмотреть стек
"""


# class Stack:
#     __cnt = 0
#     __slots__ = {'__storage'}
#
#     def __init__(self):
#         if Stack.__cnt != 1:
#             self.__storage = list()
#             Stack.__cnt += 1
#         else:
#             raise Exception('Нельзя создать больше одного обьекта')
#
#     def add_to_stack(self, value):
#         self.__storage.append(value)
#         return True
#
#     def take_from_stack(self):
#         return self.__storage.pop()
#
#     def __repr__(self):
#         return f'{self.__storage}'


# stack = Stack()
# for i in range(10):
#     stack.add_to_stack(i)
# print(stack.take_from_stack())
# print(Stack.cnt)
# stack.storage2 = [1, 2, 3]
# print(stack.storage2)
# stack2 = Stack()


class Queue:
    def __init__(self):
        self.__storage = tuple()

    def add_to_queue(self, value):
        self.__storage += (value, )
        return True

    def take_from_queue(self):
        try:
            first_element = self.__storage[0]
            self.__storage = self.__storage[1:]
            return first_element
        except IndexError as ie:
            print(ie)
            return self.__storage

    def __repr__(self):
        return f'{self.__storage}'


# queue = Queue()
# for i in range(1, 2):
#     queue.add_to_queue(i)
# print(queue.take_from_queue())
# print(queue.take_from_queue())
# print(queue)


"""Реализуйте класс стека для работы с целыми значениями (стек целых).
Стек должен иметь фиксированный размер.
Реализуйте набор операций для работы со стеком:
■ помещение целого значения в стек;
■ выталкивание целого значения из стека;
■ подсчет количества целых в стеке;
■ проверку пустой ли стек;
■ проверку полный ли стек;
■ очистку стека;
■ получение значения без выталкивания верхнего целого в стеке.
При старте приложения нужно отобразить меню с
помощью, которого пользователь может выбрать необходимую операцию"""


class Stack:
    def __init__(self):
        self.__storage = list()
        self.__size = 10

    def add_to_stack(self, value):
        if len(self.__storage) < self.__size:
            self.__storage.append(value)
            return True
        else:
            return False

    def raise_stack(self, new_value):
        self.__size = new_value

    def take_from_stack(self):
        return self.__storage.pop()

    def count_in_stack(self):
        return len(self.__storage)

    def is_empty(self):
        if len(self.__storage) == 0:
            return True
        return False

    def is_fully(self):
        if len(self.__storage) == self.__size:
            return True
        return False

    def clean_stack(self):
        while not self.is_empty():
            self.take_from_stack()
        return self.__storage

    def get_value_from_stack(self):
        return self.__storage[-1]

    def __repr__(self):
        return f'{self.__storage=}{len(self.__storage)=}'

    def menu(self):
        print('Что вы хотите сделать ?\n'
              '1 : помещение целого значения в стек;\n'
              '2 : выталкивание целого значения из стека;\n'
              '3 : подсчет количества целых в стеке;\n'
              '4 : проверку пустой ли стек;\n'
              '5 : проверку полный ли стек;\n'
              '6 : очистку стека;\n'
              '7 : получение значения без выталкивания верхнего целого в стеке.\n'
              'q : Выйти\n')
        choose = input('Введите индекс выбраного вами действия: ')
        while choose != 'q':
            if choose == '1':
                value = input('Введите значение, которое ходите добавить в стек: ')
                self.add_to_stack(value)
            elif choose == '2':
                print(self.take_from_stack())
            elif choose == '3':
                print(self.count_in_stack())
            elif choose == '4':
                if self.is_empty():
                    print('Он пустой')
                else:
                    print('Он не пустой')
            elif choose == '5':
                if self.is_fully():
                    print('Он полный')
                else:
                    print('Он не полный')
            elif choose == '6':
                print(self.clean_stack())
            elif choose == '7':
                print(self.get_value_from_stack())
            else:
                print('Была сделана ошибка, повторите попытку или нажмите "q" для выхода')
            print('\nЧто вы хотите сделать ?\n'
                  '1 : помещение целого значения в стек;\n'
                  '2 : выталкивание целого значения из стека;\n'
                  '3 : подсчет количества целых в стеке;\n'
                  '4 : проверку пустой ли стек;\n'
                  '5 : проверку полный ли стек;\n'
                  '6 : очистку стека;\n'
                  '7 : получение значения без выталкивания верхнего целого в стеке.\n'
                  'q : Выйти\n')
            choose = input('Введите индекс выбраного вами действия: ')
            print('')
        return -1


stack = Stack()
# stack.menu()
# for i in range(11):
#     stack.add_to_stack(i)

print(stack)
