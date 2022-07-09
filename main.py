from functools import partial
from tkinter import *
from tkinter import messagebox
from default_window import Dwindow
import time

last_press = 0


def export_written(user_text, window):
    if messagebox.askquestion(title="title", message="You have reached your time limit \n "
                                                     "would you like to save your work in file"):
        with open('text.txt', 'w') as file:
            file.write(user_text.get('0.1', END))
            window.destroy()
            starting()
    else:
        window.destroy()
        starting()


def on_key_press(event):
    global last_press
    last_press = time.time()


def check_difference(user_text, window):
    user_text.bind('<Key>', on_key_press)
    current_time = time.time()
    difference = current_time - last_press
    if difference >= 5:
        export_written(user_text=user_text, window=window)
    window.after(1000, check_difference, user_text, window)


def start_here(starting_window=0):
    global last_press
    if not starting_window == 0:
        starting_window.destroy()
    window = Dwindow()
    user_text = Text(window, padx=10)
    user_text.grid(row=1, column=1)
    last_press = time.time()
    check_difference(user_text=user_text, window=window)


def starting():
    starting_window = Dwindow()

    title_label = Label(starting_window,
                        text='Disappearing Text Writing',
                        font=('Arial', 22, 'bold'),
                        fg='#F32013', )
    title_label.grid(row=0, column=0, columnspan=2)

    starting_window_text = Label(starting_window,
                                 text="For most writers, a big problem is writing block. Where you can't "
                                      "think of what to write and you can't write anything.\n"
                                      "So we have developed application for solving it, Here Writer can start writing "
                                      "and if writer stops writing for 5 seconds then all the text that written "
                                      "by the author will disappear.",
                                 font=('Arial', 12),
                                 wraplength=550,
                                 padx=20,
                                 pady=20
                                 )
    starting_window_text.grid(row=1, column=0, columnspan=2)

    start_button = Button(starting_window, text="start writing", command=partial(start_here, starting_window))
    start_button.grid(row=2, column=0, columnspan=2)

    starting_window.mainloop()


starting()
