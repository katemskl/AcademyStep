import json
import hashlib

# x = [10, [3.141, 20, [30, 'qqz', 2.178]], 'foo']
# print(x[1][2][1][2])
#
# print(sorted((1, 2, 3)))
# print(False == True in [False])


def divisible_by_b(a, b):
    while a % b != 0:
        a += 1
    return a


# print(divisible_by_b(17000, 8000))
# print(divisible_by_b(980000, 30000))

def multiply(arr):
    ret_list = []
    for elem in arr:
        elem_list = []
        for _ in range(len(arr)):
            elem_list.append(elem)
        ret_list.append(elem_list)
    return ret_list


def multiply2(arr):
    return [[i]*len(arr) for i in arr]

#
# print(multiply2([4, 5]))
# print(multiply(["*", "%", "$"]))


def sum_missing_numbers(arr):
    first = min(arr)
    last = max(arr)
    sum_arr = []
    for i in range(first, last):
        if i not in arr:
            sum_arr.append(i)
    return sum(sum_arr)


# def sum_missing_numbers2(arr):
#     return sum(range(min(arr), max(arr))) - sum(arr)


# print(sum_missing_numbers([4, 3, 8, 1, 2]))
# print(sum_missing_numbers([17, 16, 15, 10, 11, 12]))
# print(sum_missing_numbers([1, 2, 3, 4, 5]))


def is_slidey(num):
    check = str(num)
    for n in range(len(check) - 1):
        check1 = int(check[n]) == int(check[n+1])+1
        check2 = int(check[n]) == int(check[n+1])-1
        if check1 or check2:
            continue
        else:
            return False
    return True


# print(is_slidey(123454321) is True)
# print(is_slidey(54345) is True)
# print(is_slidey(987654321) is True)
# print(is_slidey(1123) is False)
# print(is_slidey(1357) is False)
# print(is_slidey(1) is True)


"""
Есть некоторый словарь, который хранит названия стран и столиц. 
Название страны используется в качестве ключа, название столицы 
в качестве значения. Необходимо реализовать: добавление данных, 
удаление данных, поиск данных, редактирование данных, сохранение 
и загрузку данных (используя упаковку и распаковку)
"""


def add_new_item(storage: dict, **kwargs):
    key = kwargs.get('key')
    value = kwargs.get('value')
    storage[key] = value
    return storage


def delete_item(storage: dict, **kwargs):
    key = kwargs.get('key')
    storage.pop(key)
    return storage


def find_item(storage: dict, **kwargs):
    key = kwargs.get('key')
    return storage.get(key)


def edit_item(storage, **kwargs):
    key = kwargs.get('key')
    value = kwargs.get('value')
    storage[key] = value


def save_storage(**kwargs):
    file_name = kwargs.get('file_name')
    storage = kwargs.get('storage')
    if file_name and storage:
        with open(file_name, 'w', encoding='utf-8') as fw:
            fw.write(json.dumps(storage, ensure_ascii=True, indent=4))
            return 'Storage written successfully'
    else:
        return f'There is no argument {"file_name" if not kwargs.get("file_name") else None}' \
               f'{"storage" if not kwargs.get("storage") else None}'


def get_data(file_name):
    with open(file_name, 'r') as fr:
        data = fr.read()
        return json.loads(data)


# countries = get_data('country_data')
# print(add_new_item(countries, key='Ukraine', value='Kiyv'))
# print(delete_item(countries, key='Belgium'))
# print(find_item(countries, key='US'))
# edit_item(countries, key='Mexico', value='Mexico-city')
# print(countries)
# save_storage(file_name='country_data', storage=countries)

class Node:
    __slots__ = {'value', 'prev_node', 'next_node'}

    def __init__(self, value=None):
        self.value = value
        self.prev_node = None
        self.next_node = None

    def __repr__(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        # self.tail = None
        # if nodes is not None:
        #     node = Node(nodes.pop(0))
        #     self.head = node
        #     self.tail = Node()
        #     self.tail.next_node = node
        #     prev = node
        #     for elem in nodes:
        #         node.prev_node = prev
        #         node.next_node = Node(elem)
        #         node = node.next_node
        #         prev.prev_node = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next_node
        nodes.append('None')
        return ' ==> '.join(nodes)

    def add_at_start(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
        else:
            new_node = Node(value)
            self.head.prev_node = new_node
            new_node.next_node = self.head
            self.head = new_node

    def insert_in_the_end(self, value):
        new_node = Node(value)
        temp: Node = self.head
        while temp.next_node is not None:
            temp = temp.next_node
        temp.next_node = new_node
        new_node.prev_node = temp


# ll = LinkedList()
# for i in range(1, 5):
#     ll.insert_in_the_end(i)

# print(ll)

def zeroes(base, number):
    factorial = 1
    ret = 0
    for i in range(number+1):
        factorial *= i
    check = str(factorial)[::-1]
    for num in check:
        if num == '0':
            ret += 1
        else:
            return ret

print(zeroes(10, 10))