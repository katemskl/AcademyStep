from main10_logic import *

SIZE = 400
GRID_LEN = 4
GRID_PADDING = 10

BACKGROUND_COLOR_GAME = '#92877d'
BACKGROUND_COLOR_CELL_EMPTY = '#9e948a'

BACKGROUND_COLOR_DICT = dict(zip([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],
                                 ['#eee4da', '#ede0c8', '#f2b179', '#f59563',
                                  '#f67c5f', '#f65e3b', '#edcf72', '#edcc61',
                                  '#edc850', '#edc53f', '#edc22e']))

CELL_COLOR_DICT = dict(zip([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048],
                                 ['#776e65', '#776e65', '#f9f6f2', '#f9f6f2',
                                  '#f9f6f2', '#f9f6f2', '#f9f6f2', '#f9f6f2',
                                  '#f9f6f2', '#f9f6f2', '#f9f6f2']))

FONT = ('Verdana', 40, 'bold')

KEY_UP = 'w'
KEY_DOWN = 's'
KEY_LEFT = 'a'
KEY_RIGHT = 'd'

main_frame = Frame()
grid_cell = []
matrix = []
