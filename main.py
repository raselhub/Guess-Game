# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Developed by MOHAMMAD RASEL, Date: 02/15/2022
# Copyright @2022 All rights reserved!

from tkinter import *
import random

attempts = 10
answer = random.randint(1, 99)

  #def on_click(check):
     #winsound.Beep('frequency', 'duration')


def check_answer():
    global attempts
    global text


    attempts -= 1
    guess = int(entry_window.get())

    if answer== guess:
        text.set("You Won! Congratulations!! \n Try again")
        btn_check.pack_forget()

    elif attempts == 0:
        text.set("You are out of attempts!")
        btn_check.pack_forget()
    elif guess < answer:
        text.set("Incorrect! You have "+ str(attempts) + " attempts remaining - \n Choose Higher Number!")
    elif guess > answer:
        text.set("Incorrect! You have "+ str(attempts) + " attempts remaining - \n Choose Lower Number!")

    return

root = Tk()

root.title('Guess Game')
root.wm_geometry("750x250")


label = Label(root, text= "Guess the Number between  1 to 99", bg= "#008080")
label.pack()

entry_window = Entry(root, width=40, borderwidth= 7)
entry_window.pack()

btn_check = Button(root, text="Check", command= check_answer, bg = "#FF0000")
btn_check.pack()

btn_exit = Button(root, text= "Exit", command= root.destroy)

btn_exit.pack()

text = StringVar()
text.set("You have 10 attempts remaining! Good Luck ")
guess_attempts = Label(root, textvariable= text)
guess_attempts.pack()


root.mainloop()


