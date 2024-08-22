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
    painter.forward(40)
    painter.right(90)
    painter.circle(10)
    painter.right(60)
    painter.forward(20)
    painter.back(20)
    painter.right(60)
    painter.forward(20)
    painter.back(20)
    painter.left(30)
    painter.forward(40)
    painter.right(45)
    painter.forward(20)
    painter.back(20)
    painter.left(90)
    painter.forward(20)
    painter.back(20)
boy()
painter.penup()
painter.setposition(-35,-90 )
painter.pendown()
def littlegirl():
    painter.forward(10)
    painter.right(90)
    painter.circle(10)
    painter.right(60)
    painter.forward(10)
    painter.back(10)
    painter.right(60)
    painter.forward(10)
    painter.back(10)
    painter.left(30)
    painter.forward(10)
    painter.right(45)
    painter.forward(10)
    painter.back(10)
    painter.left(90)
    painter.forward(10)
    painter.back(10)
painter.right(225)
littlegirl()
painter.penup()
painter.setposition(-20,-90 )
painter.pendown()
painter.right(225)
boy()
painter.penup()
painter.setposition(-35,-60 )
painter.pendown()
painter.setheading(-90)
def hair():
    for _ in range (1):
        painter.left (75)
        painter.forward(20)
        painter.back(20)
        painter.right (140)
        painter.forward(20)
        painter.back(20)
hair()
painter.penup()
painter.setposition(-20,-30 )
painter.pendown()
painter.setheading(-90)
hair()
def draw_sun():
    
    
    painter.penup()
    painter.goto(200 , 200)  
    painter.pendown()
    painter.color("yellow")
    painter.begin_fill()
    painter.circle(50)  
    painter.end_fill()
    
    num_rays = 12
    ray_length = 50
    
    for _ in range(num_rays):
        painter.penup()
        painter.goto(225,150)  
        painter.pendown()
        painter.setheading(360 / num_rays * _)  
        painter.forward(50)  
        painter.forward(ray_length)  
    
    

draw_sun()
painter.setheading(0)

painter.color('#008000')
painter.fillcolor('#008000')
painter.penup()
painter.goto(150, -20)
painter.pendown()
painter.begin_fill()
painter.forward(250)
painter.left(90)
painter.forward(50)
painter.left(90)
painter.forward(250)
painter.left(90)
painter.forward(50)
painter.end_fill()

painter.penup()
painter.goto(200, 30)
painter.pendown()
painter.setheading(45)
painter.forward(50)
painter.setheading(0)
painter.forward(75)
painter.setheading(-45)
painter.forward(50)
painter.setheading(90)



painter.penup()
painter.goto(200, -10)
painter.pendown()
painter.color('#000000')
painter.fillcolor('#000000')
painter.begin_fill()
painter.circle(20)
painter.end_fill()
painter.penup()
painter.goto(350, -10)
painter.pendown()
painter.color('#000000')
painter.fillcolor('#000000')
painter.begin_fill()
painter.circle(20)
painter.end_fill()

painter.hideturtle()
















wn=trtl.Screen()
wn.mainloop()      
