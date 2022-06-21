from main7_functional import *


# def insert():
#     entry.insert(0, 'Hello')
#
#
# def delete():
#     entry.delete(0, END)
#
#
# wind = Tk()
#
# wind.title('Widgets')
# wind.geometry('300x140')
# wind.resizable(False, False)
#
# label = Label(wind, text='Hello World', font=('Arial', 16, 'bold'))
# label.config(bd=10)
# label.pack()
#
# entry = Entry(width=30)
# entry.pack()
#
# button_click = Button(wind, text='Click to say', bg='#fff', width=10, height=1)
# button_click.config(command=insert)
# button_click.pack(side=LEFT, padx=10, pady=15)
#
# button_delete = Button(wind, text='Delete', background='#eeeeee', width=10, height=1)
# button_delete.config(command=delete)
# button_delete.pack(side=RIGHT, padx=10, pady=15)
#
# wind.mainloop()

wind = Tk()
wind.title('Rainbow')
wind.geometry('180x240')

label = Label(wind, anchor='center')
label.pack()

entry = Entry(wind, justify='center', bd=5)
entry.pack()

button_red = Button(width=16, highlightbackground='#ff0000', command=lambda: red(label, entry))
button_orange = Button(width=16, highlightbackground='#ff7d00', command=lambda: orange(label, entry))
button_yellow = Button(width=16, highlightbackground='#ffff00', command=lambda: yellow(label, entry))
button_green = Button(width=16, highlightbackground='#00ff00', command=lambda: green(label, entry))
button_cyan = Button(width=16, highlightbackground='#007dff', command=lambda: cyan(label, entry))
button_blue = Button(width=16, highlightbackground='#0000ff', command=lambda: blue(label, entry))
button_purple = Button(width=16, highlightbackground='#7d00ff', command=lambda: purple(label, entry))

button_red.pack()
button_orange.pack()
button_yellow.pack()
button_green.pack()
button_cyan.pack()
button_blue.pack()
button_purple.pack()
wind.mainloop()
