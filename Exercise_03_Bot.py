from tkinter import *
from tkinter import messagebox
import random


def click(index):
    global count
    global field
    field[index] = 'X'
    btn[index].config(text='X', state='disabled')
    count += 1
    victory('X')
    if count == 5:
        messagebox.showinfo('Ничья', 'Ничья')
        end_game()
        return
    bot()
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
        if field[i] == '':
            field[i] = 'End'
            btn[i].config(state='disabled')


def bot():
    if field[4] == '':
        change_button(4)
        return
    for i in range(0, 9, 3):
        if field[i] + field[i + 1] + field[i + 2] == '00':
            j = search_empty(i, i + 1, i + 2)
            change_button(j)
            return
    for i in range(3):
        if field[i] + field[i + 3] + field[i + 6] == '00':
            j = search_empty(i, i + 3, i + 6)
            change_button(j)
            return
    if field[0] + field[4] + field[8] == '00':
        j = search_empty(0, 4, 8)
        change_button(j)
        return
    if field[2] + field[4] + field[6] == '00':
        j = search_empty(2, 4, 6)
        change_button(j)
        return
    for i in range(0, 9, 3):
        if field[i] + field[i + 1] + field[i + 2] == 'XX':
            j = search_empty(i, i + 1, i + 2)
            change_button(j)
            return
    for i in range(3):
        if field[i] + field[i + 3] + field[i + 6] == 'XX':
            j = (search_empty(i, i + 3, i + 6))
            change_button(j)
            return
    if field[0] + field[4] + field[8] == 'XX':
        j = search_empty(0, 4, 8)
        change_button(j)
        return
    if field[2] + field[4] + field[6] == 'XX':
        j = search_empty(2, 4, 6)
        change_button(j)
        return
    while '' in field:
        temp = random.randint(0, 8)
        if field[temp] == '':
            field[temp] = '0'
            change_button(temp)
            break


def search_empty(index_0, index_1, index_2):
    global field
    if field[index_0] == '':
        return index_0
    elif field[index_1] == '':
        return index_1
    else:
        return index_2


def change_button(index):
    global field
    field[index] = '0'
    btn[index].config(text='0', state='disabled')


count = 0
field = [''] * 9

window = Tk()
window.title('X & 0')

btn = [Button(width=10, height=4, font=('Arial', 10, 'bold'), command=lambda x=i: click(x)) for i in range(9)]
cnt = 0
for i in range(3):
    for k in range(3):
        btn[cnt].grid(row=i, column=k)
        cnt += 1

window.mainloop()
