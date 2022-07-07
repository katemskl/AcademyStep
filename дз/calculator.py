from calculator_functional import *

calculator_wind = Tk()

calculator_wind.title('Calculator')
calculator_wind.geometry('250x250')
calculator_wind.resizable(True, True)

entry = Entry(calculator_wind, justify='right', )
entry.grid(columnspan=4, row=0)

button_clear = Button(calculator_wind, text='clear', height=2, width=5, command=lambda: clear(entry))
button_clear.grid(column=0, row=1)

button_plus = Button(calculator_wind, text='+', height=2, width=5, command=lambda: show_action('+', entry))
button_minus = Button(calculator_wind, text='-', height=2, width=5, command=lambda: show_action('-', entry))
button_multiply = Button(calculator_wind, text='*', height=2, width=5, command=lambda: show_action('*', entry))
button_division = Button(calculator_wind, text='/', height=2, width=5, command=lambda: show_action('/', entry))
button_coma = Button(calculator_wind, text='.', height=2, width=5, command=lambda: show_action('.', entry))

button_plus.grid(column=1, row=1)
button_minus.grid(column=2, row=1)
button_multiply.grid(column=3, row=1)
button_division.grid(column=3, row=2)
button_coma.grid(column=3, row=3)

button_0 = Button(calculator_wind, text='0', height=2, width=5, command=lambda: show_action('0', entry))
button_0.grid(column=3, row=4)

button_1 = Button(calculator_wind, text='1', height=2, width=5, command=lambda: show_action('1', entry))
button_2 = Button(calculator_wind, text='2', height=2, width=5, command=lambda: show_action('2', entry))
button_3 = Button(calculator_wind, text='3', height=2, width=5, command=lambda: show_action('3', entry))
button_4 = Button(calculator_wind, text='4', height=2, width=5, command=lambda: show_action('4', entry))
button_5 = Button(calculator_wind, text='5', height=2, width=5, command=lambda: show_action('5', entry))
button_6 = Button(calculator_wind, text='6', height=2, width=5, command=lambda: show_action('6', entry))
button_7 = Button(calculator_wind, text='7', height=2, width=5, command=lambda: show_action('7', entry))
button_8 = Button(calculator_wind, text='8', height=2, width=5, command=lambda: show_action('8', entry))
button_9 = Button(calculator_wind, text='9', height=2, width=5, command=lambda: show_action('9', entry))
button_1.grid(column=0, row=4)
button_2.grid(column=1, row=4)
button_3.grid(column=2, row=4)
button_4.grid(column=0, row=3)
button_5.grid(column=1, row=3)
button_6.grid(column=2, row=3)
button_7.grid(column=0, row=2)
button_8.grid(column=1, row=2)
button_9.grid(column=2, row=2)

calculator_wind.mainloop()
