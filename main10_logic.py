import random
from tkinter import *


def init_grid(bg_color_game, size, grid_len, bg_color_cell_empty, grid_padding, font, grid_cell):
    background = Frame(bg=bg_color_game, width=size, height=size)
    background.grid()
    for i in range(grid_len):
        grid_row = []
        for j in range(grid_len):
            cell = Frame(background, background=bg_color_cell_empty, width=size/grid_len)
            cell.grid(row=i, column=j, padx=grid_padding, pady=grid_padding)
            t = Label(master=cell, text='', background=bg_color_cell_empty,
                      justify=CENTER, font=font, width=5, height=2)
            t.grid()
            grid_row.append(t)
        grid_cell.append(grid_row)


def main(bg_color_game, size, grid_len, bg_color_cell_empty, grid_padding, font, grid_cell):
    init_grid(bg_color_game, size, grid_len, bg_color_cell_empty, grid_padding, font, grid_cell)
    mainloop()
