# task 2

"""Реализуйте класс стека для работы со строками (стек строк).
Стек должен иметь фиксированный размер.
Реализуйте набор операций для работы со стеком:
■ помещение строки в стек;
■ выталкивание строки из стека;
■ подсчет количества строк в стеке;
■ проверку пустой ли стек;
■ проверку полный ли стек;
■ очистку стека;
■ получение значения без выталкивания верхней строки из стека.
При старте приложения нужно отобразить меню с помощью, которого пользователь может выбрать необходимую операцию."""


class Stack:
    def __init__(self):
        self.__storage = str()
        self.__size = 10

    @staticmethod
    def count_word(words):
        return len(words.split())

    def add_to_stack(self, words: str):
        if self.count_word(self.__storage) + self.count_word(words) <= 10:
            self.__storage += str(words) + ' '
            return self.__storage
        else:
            return -1

    def delete_from_stack(self):
        word_list = self.__storage.split()
        word = word_list.pop()
        self.__storage = ' '.join(word_list)
        return word

    def count_string_in_stack(self):   # строки, подразумивается, слова разделенные точками
        string_list = self.__storage.split('.')
        return len(string_list) - 1

    def is_empty(self):
        if len(self.__storage) == 0:
            return True
        return False

    def is_fully(self):
        if self.count_word(self.__storage) == self.__size:
            return True
        return False

    def clean_stack(self):
        self.__storage = ' '

    def get_value_from_stack(self):   # как я поняла последнее значение, так мы делали на уроке
        return self.__storage.split()[-1]

    def __repr__(self):
        return f'{self.__storage}'

    def main(self):
        print('Что вы хотите сделать ?\n'
              '1 : помещение строки в стек;\n'
              '2 : выталкивание строки из стека;\n'
              '3 : подсчет количества строк в стекее;\n'
              '4 : проверку пустой ли стек;\n'
              '5 : проверку полный ли стек;\n'
              '6 : очистку стека;\n'
              '7 : получение значения без выталкивания верхнего целого в стеке.\n'
              'q : Выйти\n')
        choose = input('Введите индекс выбраного вами действия: ')
        while choose != 'q':
            if choose == '1':
                value = input('Введите значение, которое ходите добавить в стек: ')
                res = self.add_to_stack(value)
                if res == -1:
                    print('Достигнут лимит слов в стеке')
                else:
                    print(res)
            elif choose == '2':
                print(self.delete_from_stack())
            elif choose == '3':
                print(self.count_string_in_stack())
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
            print('Что вы хотите сделать ?\n'
                  '1 : помещение строки в стек;\n'
                  '2 : выталкивание строки из стека;\n'
                  '3 : подсчет количества строк в стекее;\n'
                  '4 : проверку пустой ли стек;\n'
                  '5 : проверку полный ли стек;\n'
                  '6 : очистку стека;\n'
                  '7 : получение значения без выталкивания верхнего целого в стеке.\n'
                  'q : Выйти\n')
            choose = input('Введите индекс выбраного вами действия: ')
            print('')
        return -1


string = Stack()
string.add_to_stack('something interesting.')
string.add_to_stack('can happend. with you if you give me.')
string.add_to_stack('some money')
print(string)
string.main()

