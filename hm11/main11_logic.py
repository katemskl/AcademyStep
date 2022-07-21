import sys
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog


def save_file(file_name, text):
    with open(file_name, 'w') as file:
        text_save = str(text.get(1.0, END))
        file.write(text_save + '\n')


def directory_file(root, text):
    file_name = filedialog.asksaveasfilename(initialdir='/', title='Select file',
                                             filetypes=(('Text Documents', '*.txt'), ('all files', '*.*')))
    root.title(f'{file_name} - Notepad')
    if file_name:
        save_file(file_name, text)


def open_file(root, text):
    file_name = filedialog.askopenfilename(initialdir='/', title='Open file',
                                           filetypes=(('Text Documents', '*.txt'), ('all files', '*.*')))
    root.title(f'{file_name} - Notepad')
    if file_name:
        with open(file_name, 'r', encoding='utf-8') as file:
            text_open = file.read()
            if text_open != NONE:
                text.delete(1.0, END)
                text.insert(END, text_open)


def show_about():
    tkinter.messagebox.showinfo(title='About us', message='This app has been made 21.07 by Katusha')


def show_help():
    tkinter.messagebox.showinfo(title='Info', message='тут могла б бути інформація, але мені ліньки :(')


def check_and_save(text):
    answer = tkinter.messagebox.askyesno(title='Save document', message='Do you want to save ?')
    if answer:
        file_name = filedialog.asksaveasfilename(initialdir='/', title='Open file',
                                                 filetypes=(('Text Documents', '*.txt'), ('all files', '*.*')))

        if file_name:
            save_file(file_name, text)


def new(text):
    check_and_save(text)
    text.delete(1.0, END)


def exit_notepad(text):
    check_and_save(text)
    sys.exit()

