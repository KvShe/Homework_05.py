from tkinter import *
from tkinter import messagebox


def click(index):
    global count
    global field
    if count % 2 == 0:
        btn[index].config(text='X', state='disabled')
        count += 1
        field[index] = 'X'
    else:
        btn[index].config(text='0', state='disabled')
        count += 1
        field[index] = '0'
    victory('X')
    if count == 9:
        messagebox.showinfo('', 'Ничья')
    victory('0')


def victory(ch):
    global field
    global count
    if field[0] == field[1] == field[2] == ch or \
            field[3] == field[4] == field[5] == ch or \
            field[6] == field[7] == field[8] == ch or \
            field[0] == field[3] == field[6] == ch or \
            field[1] == field[4] == field[7] == ch or \
            field[2] == field[5] == field[8] == ch or \
            field[0] == field[4] == field[8] == ch or \
            field[2] == field[4] == field[6] == ch:
        messagebox.showinfo('Игра окончена', f'Победил {ch}')
        end_game()
        if count == 9:
            count = False


def end_game():
    global field
    for i in range(len(field)):
        if field[i] == 0:
            btn[i].config(state='disabled')


count = 0
field = [0] * 9

window = Tk()
window.title('X & 0')

btn = [Button(width=10, height=4, font=('Arial', 10, 'bold'), command=lambda x=i: click(x)) for i in range(9)]
cnt = 0
for i in range(3):
    for k in range(3):
        btn[cnt].grid(row=i, column=k)
        cnt += 1

window.mainloop()
