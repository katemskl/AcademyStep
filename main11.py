from main11_logic import *

root = Tk()
root.title('Notepad')
root.geometry('800x400')

menu = Menu(root)
root.config(menu=menu)

text = Text(root)
scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)
text.pack(expand=YES, fill=BOTH)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='New', command=lambda: new(text))
file_menu.add_command(label='Open as...', command=lambda: open_file(text))
file_menu.add_command(label='Save as...', command=lambda: directory_file(text))
file_menu.add_command(label='Exit', command=lambda: exit_notepad(text))

help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label='Help', command=show_help)
help_menu.add_command(label='About', command=show_about)

menu.add_cascade(label='File', menu=file_menu)
menu.add_cascade(label='Help', menu=help_menu)

root.mainloop()
