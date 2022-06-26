import pickle
from tkinter import *
from tkinter import messagebox

# original = {'Illinois': "Aurora",
#             'Massachusetts': 'Boston',
#             'Florida': 'Orlano'}
#
# pickled = pickle.dumps(original)
# indent = pickle.loads(pickled)
#
# print(f'Orig: {original}\nPick: {pickled}\nInd: {indent}')

HEIGHT = 550
WIDTH = 550

root = Tk()
root.title('Form')
root.geometry(f'{WIDTH}x{HEIGHT}')
root.resizable(False, False)

root.mainloop()
