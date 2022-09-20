import random
from tkinter import *
from tkinter import messagebox


def clicked(index):
    global name
    name = '{}'.format(ent[index].get())
    if name.replace(' ', '') != '':
        ent[index].config(state='disabled')


def begin():
    global amount
    global go
    go = random.randint(0, 1)
    if name == '':
        messagebox.showinfo('А как же назваться?', 'Введите имя')
    else:
        amount = 2021
        # txt_0.config(text=f'Осталось: {amount} конфет(ы)')
        ent[2].config(state='normal')
    if go == 1:
        amount -= bot()
    else:
        txt_3.config(text='')
    txt_0.config(text=f'Осталось: {amount} конфет(ы)')


def steps():
    global go
    global amount
    if go == 0:
        amount -= player_step()
        go = 1
    else:
        step = bot()
        amount -= step
        go = 0
    if amount < 1:
        if go == 0:
            messagebox.showinfo('Победа', 'Ура - победа!')
        else:
            messagebox.showinfo('Game over', 'Game over')
    txt_0.config(text=f'Осталось: {amount} конфет(ы)')


def player_step():
    global amount
    global go
    try:
        step = int('{}'.format(ent[2].get()))
        if 0 < step < 29:
            amount -= step
            txt_0.config(text=f'Осталось: {amount} конфет(ы)')
            return step
            # if amount < 1:
            #     messagebox.showinfo('The end', f'Победил(а) {name}')
        else:
            messagebox.showinfo('Мухлюешь?', 'Кузя, я за тобой наблюдаю')
    except ValueError:
        messagebox.showinfo('Что это?', 'Это точно не число, попробуй снова')


def bot():
    global amount
    if amount < 29:
        step = amount
    else:
        step = random.randint(1, 28)
    txt_0.config(text=f'Осталось: {amount} конфет(ы)')
    txt_3.config(text=f'Bot взял {step}: конфет')
    return step


window = Tk()
window.title('Игра в конфеты против бота')


ent = [Entry(width=26) for i in range(2)]
ent[0].grid(row=1, column=0)
# ent[1].grid(row=2, column=0)
ent.append(Entry(width=26, state='disabled'))

ent[2].grid(row=9)

ent[0].focus()

btn = [Button(text='Введите имя игрока', width=20, command=lambda j=i: clicked(j)) for i in range(2)]
btn[0].grid(row=1, column=1)
# btn[1].grid(row=2, column=1)

btn_2 = Button(text='Взять конфеты', width=20, command=steps)
btn_2.grid(row=9, column=1)
btn_3 = Button(text='Начать', width=35, command=begin)
btn_3.grid(row=6, columnspan=2)


amount = 2021
go = random.randint(0, 1)
name = ''


txt_0 = Label(text=f'Осталось: {amount} конфет(ы)')
txt_0.grid(row=7, column=0)

txt_2 = Label()
txt_2.grid(row=5)
txt_3 = Label(justify=LEFT)
txt_3.grid(row=10)


window.mainloop()
