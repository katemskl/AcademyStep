from tkinter import *


def add_item():
    select = list(box.curselection())
    select.reverse()
    for i in select:
        shop_list.insert(END, products[i])
        box.delete(i)


def del_list():
    select = list(shop_list.curselection())
    select.reverse()
    for i in select:
        shop_list.delete(i)
        box.insert(END, products[i])


root = Tk()

products = ['bananas', 'pineapple', 'apple', 'orange', 'strawberry']

box = Listbox(selectmode=EXTENDED)
box.pack(side=LEFT)

for product in products:
    box.insert(END, product)

scroll = Scrollbar(command=box.yview())
scroll.pack(side=LEFT, fill=Y)
box.config(yscrollcommand=scroll.set)

shop_list = Listbox()
shop_list.pack(side=RIGHT)

frame = Frame()
frame.pack(padx=20)


Button(frame, text='Add', command=add_item).pack(fill=X)
Button(frame, text='Delete', command=del_list).pack(fill=X)



root.mainloop()
