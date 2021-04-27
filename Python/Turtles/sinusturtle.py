import turtle, time, math
turtle.ht()
turtle.speed(1000)
turtle.setup(width=1300)
a = 200  #variabel
f = 5   
ff = 1  #variabel
t = 0.001 #variabel
tx = 1
xy = 0
anz = 0
pi = math.pi
angabe = 0

anzper = 1
for i in range(500): #while angabe != anzper*2:
    sin = math.sin(2*f*ff*t)+1/3*math.sin(2*3*f*ff*t)+1/5*math.sin(2*5*f*ff*t)
    
    y = a*sin
    print(y)
    turtle.left(90)
    turtle.forward(y-xy)
    turtle.right(90)
    turtle.forward(tx)
    xy = y
    t= t + 0.002
    anz= anz+1
    print(anz)
    if round(round(y)/2) == 0: # klappt nur bei der addierten t =0,001 und f = 5
        angabe = angabe + 1
    
    #print(angabe)
print("ENDE")
time.sleep(2)
