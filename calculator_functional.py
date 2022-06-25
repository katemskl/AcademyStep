from tkinter import *

first_number = 0
index_action = 0
flag = True


def show_action(act, entry):
    clear(entry)
    entry.insert(0, act)
    return 1


def clear(entry):
    entry.delete(0, END)
    return 1


def check_action(action):
    actions = ['+', '-', '*', '/']
    return actions.index(action)


def button_click(number, entry):
    show_action(number, entry)
    global first_number, flag
    if flag:
        first_number = int(entry.get())
        flag = False


def make_action(action, entry):
    show_action(action, entry)
    global index_action
    index_action = check_action(action)


def count_result(entry):
    second_number = int(entry.get())
    global flag
    flag = True
    print(first_number, second_number)
    if index_action == 0:
        return first_number + second_number
    elif index_action == 1:
        return first_number - second_number
    elif index_action == 2:
        return first_number * second_number
    elif index_action == 3:
        return first_number / second_number


def return_result(entry):
    result = count_result(entry)
    show_action(result, entry)
