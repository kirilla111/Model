# -*- coding: utf-8 -*-
import tkinter
import math
#
tk=tkinter.Tk()
tk.title(" Sample ")
#
button=tkinter.Button(tk)
button["text"]="Закрыть"
button["command"]=tk.quit
button.pack()
#
canvas=tkinter.Canvas(tk)
canvas["height"]=360
canvas["width"]=480
canvas["background"]="#eeeeff"
canvas["borderwidth"]=2
canvas.pack()
#
#canvas.create_text(20, 10, text="20, 10")
#canvas.create_text(460, 350, text="460, 350")
#
points=[]
ay=150
y0=150
x0=50
x1=470
dx=10
#
for n in range(x0, x1, dx):
    y=y0-ay*math.cos(n*dx)
    pp=(n, y)
    points.append(pp)
# - Афанасьев Кирилл, делаем метки и подписи к осям
# по oY
xk =20
yk_1=10
yk_2=300
dy=30
xxk_1 = 40
xxk_2 = 55
for i in range(yk_1,yk_2,dy):
    xk_axe =[]
    xxk =(xxk_1,i)
    xk_axe.append(xxk)
    xxk =(xxk_2,i)
    xk_axe.append(xxk)
    canvas.create_text(xk, i, text=str(i))
    canvas.create_line(xk_axe, fill="red", width=1)
# по oX
yk =150
xk_1=50
xk_2=460
dx=50
xyk_1 = 140
xyk_2 = 155
for i in range(xk_1,xk_2,dx):
    xk_axe =[]
    xxk =(i+15,xyk_1)
    xk_axe.append(xxk)
    xxk =(i+15,xyk_2)
    xk_axe.append(xxk)
    canvas.create_text(i+15, yk+10, text=str(int(i+15)))
    canvas.create_line(xk_axe, fill="red", width=1)
#
canvas.create_line(points, fill="blue", smooth=1)
#
y_axe=[]
yy=(x0, 0)
y_axe.append(yy)
yy=(x0, y0+ay)
y_axe.append (yy)
canvas.create_line(y_axe, fill="black", width=2)
#
x_axe=[]
xx=(x0, y0)
x_axe.append(xx)
xx=(x1, y0)
x_axe.append(xx)
canvas.create_line(x_axe, fill="black", width=2)
#
tk.mainloop()

