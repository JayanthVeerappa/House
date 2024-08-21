import turtle as trtl

ninja = trtl.Turtle()

ninja.speed(1000)
def draw():
    ninja = trtl.Turtle()
    for i in range(180):
        ninja.speed(1000000)
        ninja.forward(100)
        ninja.right(30)
        ninja.forward(20)
        ninja.left(60)
        ninja.forward(50)
        ninja.right(30)

        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()

        ninja.right(2)
draw()
ninja.right(90)
ninja.forward(100)
draw()
wn = trtl.Screen()
wn.mainloop()