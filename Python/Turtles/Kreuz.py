import turtle, time
turtle.ht()
x = 150
c=0

def k1 ():
    #x = 150
    turtle.goto(10,14)
    for i in range(4):
        turtle.left(90)
        turtle.forward(x)
        turtle.right(90)
        turtle.forward(x)
        turtle.right(90)
        turtle.forward(x)
    time.sleep(1)


def k2 ():
    #x = 150
    c=0
    for i in range(4):
        turtle.left(90)
        while c < x:
            turtle.forward(1)
            c = c + 1

        c = 0

        turtle.right(90)
        while c < x:
            turtle.forward(1)
            c = c + 1

        c = 0

        turtle.right(90)
        while c < x:
            turtle.forward(1)
            c = c + 1

        c = 0
    

k2()
k1()