from main12_logic import *

HEIGHT = 600
WIDTH = 600

root = Tk()
root.title('To Do')
root.geometry(f'{HEIGHT}x{WIDTH}')
root.resizable(False, False)

img = PhotoImage(file='img/bg2.gif')
bg_label = Label(root, image=img)
bg_label.place(relwidth=1, relheight=1)

root.option_add('Font', '{Comic Sans MS} 10')
root.option_add('Background', 'white')

frame = Frame(root, bd=10)
frame.place(relx=.1, rely=.1, relwidth=.8, relheight=.8)

listbox = Listbox(frame)
listbox.place(relx=.3, rely=.24, relwidth=.6, relheight=.6)

tasks = read_previous(listbox)

label_title = Label(frame, text='To-Do List', fg='blue', font='{Comic Sans MS} 16')
label_title.place(relx=.3)

label_display = Label(frame, text='')
label_display.place(relx=.3, rely=.1)

text_input = Entry(frame, width=15)
text_input.place(relx=.3, rely=.15, relwidth=.6)

button_add_task = Button(frame, text='Add task', command=lambda: add_task(text_input, listbox, tasks))
button_add_task.place(rely=.15, relwidth=.25)

button_del = Button(frame, text='Delete', command=lambda: delete_one(listbox, tasks))
button_del.place(rely=.25, relwidth=.25)

button_del_all = Button(frame, text='Delete all', command=lambda: delete_all(listbox, tasks))
button_del_all.place(rely=.35, relwidth=.25)

button_sort_asc = Button(frame, text='Sort A-Z', command=lambda: sort_asc(listbox, tasks))
button_sort_asc.place(rely=.45, relwidth=.25)

button_sort_desc = Button(frame, text='Sort Z-A', command=lambda: sort_desc(listbox, tasks))
button_sort_desc.place(rely=.55, relwidth=.25)

button_random = Button(frame, text='Random', command=lambda: choose_random(tasks, label_display))
button_random.place(rely=.65, relwidth=.25)

button_number = Button(frame, text='Number', command=lambda: show_number(tasks, label_display))
button_number.place(rely=.75, relwidth=.25)

button_random = Button(frame, text='Exit', command=lambda: exit_and_save(tasks))
button_random.place(rely=.85, relwidth=.25)


root.mainloop()
