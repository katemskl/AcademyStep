import json

# task 1

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
    try:
        key = kwargs.get('key')
        storage.pop(key)
        return storage
    except KeyError:
        return 'No such key'


def find_item(storage: dict, **kwargs):
    key = kwargs.get('key')
    return storage.get(key)


def edit_item(storage, **kwargs):
    key = kwargs.get('key')
    value = kwargs.get('value')
    storage[key] = value
    return storage


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


# dict1 = get_data('/Users/katamoskalcuk/PycharmProjects/AcademyStepA/hm8_1/country_data')
# print(add_new_item(dict1, key='France', value='Paris'))
# print(delete_item(dict1, key='Ukraine'))
# print(find_item(dict1, key='US'))
# print(edit_item(dict1, key='US', value='Washington'))
# print(save_storage(file_name='/Users/katamoskalcuk/PycharmProjects/AcademyStepA/hm8_1/country_data', storage=dict1))
# print(dict1)


# task 2

"""Есть некоторый словарь, который хранит названия музыкальных групп(исполнителей) и альбомов. 
Название группы используется в качестве ключа, название альбомов в качестве значения. 
Необходимо реализовать: добавление данных, удаление данных, поиск данных, редактирование данных, 
сохранение и загрузку данных (используя упаковку и распаковку)."""

dict2 = get_data('/Users/katamoskalcuk/PycharmProjects/AcademyStepA/hm8_1/group_data')
print(add_new_item(dict2, key='Кино', value='Звезда по имени солнце'))
print(save_storage(file_name='/Users/katamoskalcuk/PycharmProjects/AcademyStepA/hm8_1/group_data', storage=dict2))

