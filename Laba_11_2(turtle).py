import turtle

#Напишите подпрограмму формирования строки со значениями координат для
#примера, показанного на рис. 3.2.
# Афанасьев - начало
def draw_coordinates(x,y):
    turtle.goto(x,y)
    coordinates = "("+str(x)+":"+str(y)+")"
    turtle.write(coordinates)
# - конец
turtle.reset()
turtle.tracer(0)
turtle.color('#0000ff')
#
turtle.write('0,0')
#
turtle.up()
x=-170
y=-120
coords=str(x)+","+str(y)
turtle.goto(x, y)
turtle.write(coords)
#
x=130
y=100
coords=str(x)+","+str(y)
turtle.goto(x, y)
turtle.write(coords)
#
x=0
y=-100
coords=str(x)+","+str(y)
turtle.goto(x, y)
turtle.write(coords)
#
turtle.down()
x=0
y=100
coords=str(x)+","+str(y)
turtle.goto(x, y)
turtle.write(coords)
#
turtle.up()
x=-150
y=0
coords=str(x)+","+str(y)
turtle.goto(x, y)
turtle.write(coords)
#
turtle.down()
x=150
y=0
coords=str(x)+","+str(y)
turtle.goto(x, y)
turtle.write(coords)
turtle.up()
#
while True:
    text_x = turtle.textinput('Ввод координат', 'введите координату по oX')
    text_y = turtle.textinput('Ввод координат', 'введите координату по oY')
    draw_coordinates(int(text_x),int(text_y))
turtle.mainloop()

