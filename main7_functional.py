from tkinter import *


def red(label, entry):
    label.config(text='Red')
    entry.delete(0, END)
    entry.insert(0, '#ff0000')


def orange(label, entry):
    label.config(text='Orange')
    entry.delete(0, END)
    entry.insert(0, '#ff7d00')


def yellow(label, entry):
    label.config(text='Yellow')
    entry.delete(0, END)
    entry.insert(0, '#ffff00')


def green(label, entry):
    label.config(text='Green')
    entry.delete(0, END)
    entry.insert(0, '#00ff00')


def cyan(label, entry):
    label.config(text='Cyan')
    entry.delete(0, END)
    entry.insert(0, '#007dff')


def blue(label, entry):
    label.config(text='Blue')
    entry.delete(0, END)
    entry.insert(0, '#0000ff')


def purple(label, entry):
    label.config(text='Purple')
    entry.delete(0, END)
    entry.insert(0, '#7d00ff')
