from main8_logic import *

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

root.option_add('*Font', 'Calibri')
root.option_add('*Background', 'white')

img = PhotoImage(file='img/bg2.gif')
background_label = Label(root, image=img)
background_label.place(relwidth=1, relheight=1)

button_signup = Button(root, text='SIGN UP', bg='gold', command=lambda: registration(root))
button_signup.place(relx=0.2, rely=0.1, relwidth=0.3)

button_signin = Button(root, text='SIGN IN', bg='gold', command=lambda: log_in(root))
button_signin.place(relx=0.5, rely=0.1, relwidth=0.3)

root.mainloop()
