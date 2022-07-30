import random
from tkinter import *

matrix = []


def add_two():
    a = random.randint(0, len(matrix) - 1)
    b = random.randint(0, len(matrix) - 1)
    while matrix[a][b] != 0:
        a = random.randint(0, len(matrix) - 1)
        b = random.randint(0, len(matrix) - 1)
    matrix[a][b] = 2


def init_grid(bg_color_game, size, grid_len, bg_color_cell_empty, grid_padding, font_n, grid_cell):
    background = Frame(bg=bg_color_game, width=size, height=size)
    background.grid()
    for i in range(grid_len):
        grid_row = []
        for j in range(grid_len):
            cell = Frame(background, background=bg_color_cell_empty, width=size/grid_len)
            cell.grid(row=i, column=j, padx=grid_padding, pady=grid_padding)
            t = Label(master=cell, text='', background=bg_color_cell_empty,
                      justify=CENTER, font=font_n, width=5, height=2)
            t.grid()
            grid_row.append(t)
        grid_cell.append(grid_row)


def init_matrix(grid_len):
    for i in range(grid_len):
        matrix.append([0]*grid_len)
    add_two()
    add_two()


def update_grid_cells(grid_len, grid_cell, bg_color_cell_empty, bg_color_dict, cell_color_dict):
    for i in range(grid_len):
        for j in range(grid_len):
            if matrix[i][j] == 0:
                grid_cell[i][j].configure(text='', bg=bg_color_cell_empty)
            else:
                grid_cell[i][j].configure(text=str(matrix[i][j]), bg=bg_color_dict[matrix[i][j]],
                                          fg=cell_color_dict[matrix[i][j]])


def cover_up(mat):
    new = []
    for i in range(len(mat)):
        new.append([0]*len(mat))
    done = False
    for i in range(len(mat)):
        count = 0
        for j in range(len(mat)):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return new, done


def merge(mat):
    done = False
    for i in range(len(mat)):
        for j in range(len(mat) - 1):
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return mat, done


def left_move():
    global matrix
    matrix, done = cover_up(matrix)
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    return done


def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new


def right_move():
    global matrix
    matrix = reverse(matrix)
    matrix, done = cover_up(matrix)
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    matrix = reverse(matrix)
    return done


def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new


def up_move():
    global matrix
    matrix = transpose(matrix)
    game, done = cover_up(matrix)
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    matrix = transpose(matrix)
    return done


def down_move():
    global matrix
    matrix = reverse(transpose(matrix))
    matrix, done = cover_up(matrix)
    temp = merge(matrix)
    matrix = temp[0]
    done = done or temp[1]
    matrix = cover_up(matrix)[0]
    matrix = transpose(reverse(matrix))
    return done


def game_state():
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 2048:
                return 'win'
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            if matrix[i][j] == matrix[i+1][j] or matrix[i][j+1] == matrix[i][j]:
                return 'not over'
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return 'not over'
    for k in range(len(matrix)-1):
        if matrix[len(matrix)-1][k] == matrix[len(matrix)-1][k+1]:
            return 'not over'
    for j in range(len(matrix)-1):
        if matrix[j][len(matrix)-1] == matrix[j+1][len(matrix)-1]:
            return 'not over'
    return 'lose'


def key_down(mainframe, event, grid_len, grid_cell, bg_color_cell_empty, bg_color_dict, cell_color_dict):
    key = repr(event.char)
    if key in mainframe.commands:
        done = mainframe.commands[repr(event.char)]()
        if done:
            add_two()
            update_grid_cells(grid_len, grid_cell, bg_color_cell_empty, bg_color_dict, cell_color_dict)
            if game_state() == 'win':
                grid_cell[1][1].configure(text='You', bg=bg_color_cell_empty)
                grid_cell[1][2].configure(text='WIN!', bg=bg_color_cell_empty)
            if game_state() == 'lose':
                grid_cell[1][1].configure(text='You', bg=bg_color_cell_empty)
                grid_cell[1][2].configure(text='LOSE!', bg=bg_color_cell_empty)


def main(bg_color_game, size, grid_len, bg_color_cell_empty, grid_padding,
         font_n, grid_cell, bg_color_dict, cell_color_dict, mainframe, k_up, k_down, k_left, k_right):
    mainframe.master.title('2048')
    mainframe.master.bind("<Key>", key_down)
    mainframe.commands = {k_up: up_move(), k_down: down_move(), k_left: left_move(), k_right: right_move()}
    init_grid(bg_color_game, size, grid_len, bg_color_cell_empty, grid_padding, font_n, grid_cell)
    init_matrix(grid_len)
    update_grid_cells(grid_len, grid_cell, bg_color_cell_empty, bg_color_dict, cell_color_dict)
    mainloop()
