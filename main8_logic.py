import pickle
from tkinter import *
from tkinter import messagebox


def registration(root):

    label_error = False

    frame = Frame(root, bd=10)
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor='n')

    label = Label(frame, text='Sign Up', font='16')
    label.place(relheight=.1, relwidth=1)

    label_login = Label(frame, text='Login: ')
    label_login.place(rely=.2, relheight=.1, relwidth=.55)

    login_register = StringVar()

    label_register = Entry(frame, textvariable=login_register)
    label_register.place(relx=.4, rely=.2, relheight=.1, relwidth=.55)

    label_password1 = Label(frame, text='Password: ')
    label_password1.place(rely=.4, relwidth=.35, relheight=.1)

    password1 = StringVar()

    password1_entry = Entry(frame, show='*', textvariable=password1)
    password1_entry.place(relx=.4, rely=.4, relheight=.1, relwidth=.55)

    label_password2 = Label(frame, text='Re-Password: ')
    label_password2.place(rely=.6, relwidth=.35, relheight=.1)

    password2 = StringVar()

    password2_entry = Entry(frame, show='*', textvariable=password2)
    password2_entry.place(relx=.4, rely=.6, relheight=.1, relwidth=.55)

    button = Button(frame, text='Sign Up', command=lambda: sign_up())
    button.place(relx=.3, rely=.8, relheight=0.15, relwidth=.5)

    def sign_up():
        nonlocal label_error
        # error = ''

        if label_error:
            label_error.destroy()

        if len(login_register.get()) == 0:
            error = '*login error'
        elif len(password1.get()) < 6:
            error = '*min 6 characters'
        elif password1.get() != password2.get():
            error = 'password error'
        else:
            save()
        label_error = Label(frame, text='error', fg='red')
        label_error.place(rely=.7)

    def save():
        data = {login_register.get(): password1.get()}
        with open('main8.txt', 'wb') as file:
            pickle.dump(data, file)
        log_in(root)


def log_in(root):
    frame_login = Frame(root, bd=10)
    frame_login.place(relx=.5, rely=.2, relwidth=.7, relheight=.6, anchor='n')

    label_title_login = Label(frame_login, text='Sign In', font='16')
    label_title_login.place(relwidth=1, relheight=.1)

    label_login = Label(frame_login, text='Login: ')
    label_login.place(rely=.2, relheight=.1, relwidth=.35)

    enter_login = Entry(frame_login)
    enter_login.place(relx=.4, rely=.2, relheight=.1, relwidth=.55)

    label_password = Label(frame_login, text='Password: ')
    label_password.place(rely=.4, relwidth=.35, relheight=.1)

    enter_password = Entry(frame_login, show='*')
    enter_password.place(relx=.4, rely=.4, relheight=.1, relwidth=.55)

    button_sing_in = Button(frame_login, text='Sign up', command=lambda: login_pass())
    button_sing_in.place(relx=.3, rely=.8, relheight=.15, relwidth=.5)

    def login_pass():
        with open('main8.txt', 'rb') as file:
            a = pickle.load(file)

            if enter_login.get() in a and enter_password.get() == a[enter_login.get()]:
                messagebox.showinfo('Done', 'Welcome to STEP')
            else:
                messagebox.showerror('Error!', 'Something wrong!')
