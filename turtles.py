import turtle as trtl
painter = trtl.Turtle()
def house():

    painter.begin_fill()
    painter.fillcolor("blue")

    for _ in range(4):
        painter.forward(100)
        painter.right(90)

    painter.end_fill()
    painter.begin_fill()
    painter.left(45)
    painter.forward(75)
    painter.right(90)
    painter.forward(75)
    painter.right(135)
    painter.forward(110)
    painter.fillcolor("green")

    painter.end_fill()
house()
painter.penup()
painter.setposition(20,-90 )
painter.pendown()
def door():
    painter.begin_fill()
    painter.fillcolor("brown")
    painter.right(90)
    painter.forward(50)
    painter.right(90)
    painter.forward(30)
    painter.right(90)
    painter.forward(50)
    painter.right(90)
    painter.forward(30)
    painter.right(90)
    painter.end_fill()
door()
painter.penup()
painter.setposition(20,-30 )
painter.pendown()
def window():
    painter.begin_fill()
    painter.fillcolor("grey")
    for _ in range(4):
            painter.forward(20)
            painter.right(90)
    painter.end_fill()
    painter.forward(10)
    painter.right(90)
    painter.forward(20)
    painter.back(10)
    painter.right(90)
    painter.forward(10)
    painter.back(20)




    
    
window()
painter.penup()
painter.setposition(90,-10 )
painter.pendown()
window()

painter.penup()
painter.setposition(-60,-90 )
painter.pendown()
def boy():
    painter.forward(50)
    painter.circle(10)
boy()














wn=trtl.Screen()
wn.mainloop()       