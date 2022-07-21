import sys
import tkinter.messagebox
from tkinter import *
import random


def read_previous(listbox):
    with open('to-do-list.txt', 'r') as file:
        tasks = list(file.readlines())
    update_listbox(listbox, tasks)
    return tasks


def update_listbox(listbox, tasks):
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)


def add_task(text_input, listbox, tasks):
    task = text_input.get()
    if task != '':
        tasks.append(task)
        update_listbox(listbox, tasks)
    else:
        tkinter.messagebox.showwarning('Warning', 'Enter task in the input box')
    text_input.delete(0, END)


def delete_one(listbox, tasks):
    task = listbox.get('active')
    if task in tasks:
        tasks.remove(task)
    update_listbox(listbox, tasks)


def delete_all(listbox, tasks):
    confirmed = tkinter.messagebox.askyesno('Confirm', 'Really delete all ?')
    if confirmed:
        # global tasks
        while tasks:
            tasks.pop()
        update_listbox(listbox, tasks)


def sort_asc(listbox, tasks):
    tasks.sort()
    update_listbox(listbox, tasks)


def sort_desc(listbox, tasks):
    tasks.sort()
    tasks.reverse()
    update_listbox(listbox, tasks)


def choose_random(tasks, label_display):
    if len(tasks):
        task = random.choice(tasks)
        label_display['text'] = task
    else:
        tkinter.messagebox.showwarning('Warning', 'No tasks')


def show_number(tasks, label_display):
    numer_tasks = len(tasks)
    message = f'Number of tasks: {numer_tasks}'
    label_display['text'] = message


def exit_and_save(tasks):
    with open('to-do-list.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    sys.exit()
