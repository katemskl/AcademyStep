import sys
import tkinter.messagebox
from tkinter import *
import random

tasks = []


def read_previous(listbox):
    with open('to-do-list.txt', 'r') as file:
        global tasks
        tasks = list(file.readlines())
    update_listbox(listbox)


def update_listbox(listbox):
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)


def add_task(text_input, listbox):
    task = text_input.get()
    if task != '':
        tasks.append(task)
        update_listbox(listbox)
    else:
        tkinter.messagebox.showwarning('Warning', 'Enter task in the input box')
    text_input.delete(0, END)


def delete_one(listbox):
    task = listbox.get('active')
    if task in tasks:
        tasks.remove(task)
    update_listbox(listbox)


def delete_all(listbox):
    confirmed = tkinter.messagebox.askyesno('Confirm', 'Really delete all ?')
    if confirmed:
        while tasks:
            tasks.pop()
        update_listbox(listbox)


def sort_asc(listbox):
    tasks.sort()
    update_listbox(listbox)


def sort_desc(listbox):
    tasks.sort()
    tasks.reverse()
    update_listbox(listbox)


def choose_random( label_display):
    if len(tasks):
        task = random.choice(tasks)
        label_display['text'] = task
    else:
        tkinter.messagebox.showwarning('Warning', 'No tasks')


def show_number(label_display):
    numer_tasks = len(tasks)
    message = f'Number of tasks: {numer_tasks}'
    label_display['text'] = message


def save_list():
    with open('to-do-list.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def exit_and_save():
    save_list()
    sys.exit()




