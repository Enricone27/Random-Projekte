import turtle
import time



class horizontalerWurf:

    def __init__(self):
        """ Sh(t) = V0*t """
        """ Sv(t) = H0 + (-1/2) * g * t^2 """
        self.t = 0.01
        self.V0 = 8
        self.g = 9.8
        self.H0 = 3
        self.tS = (-self.H0/-(0.5*self.g))**(1/2)
        self.A =50

        self.tur = turtle.Turtle()
        self.tur.ht()
        self.tur.speed(0)

    def Wurf(self):
        tstart = self.t
        self.Sv_t = 0
        self.Sh_t = 0
        self.tur.penup()
        self.tur.goto(-(self.V0*self.tS)*self.A,(self.H0*self.A))
        self.tur.pendown()

        def Wurfrechnung():
            hs = self.Sh_t
            vs = self.Sv_t

            self.Sh_t = (self.V0*self.t)
            self.Sv_t = (0.5 * self.g * self.t**2)

            self.esh = (self.Sh_t-hs)*self.A
            self.esv = (self.Sv_t-vs)*self.A
        
        while self.t < self.tS:

            Wurfrechnung()

            self.tur.forward(self.esh)
            self.tur.right(90)
            self.tur.forward(self.esv)
            self.tur.left(90)
            
            self.t = self.t + tstart
        print("durch")

e = horizontalerWurf()

e.Wurf()

