class Main:
    def __init__(self):
        self.felder = [" "," "," "," "," "," "," "," "," "]
        self.kombis = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.finalcheck=0

    def brett(self):
        print( " "+self.felder[0]+" ¦ "+self.felder[1]+" ¦ "+self.felder[2]+" \n\n "+self.felder[3]+" ¦ "+self.felder[4]+" ¦ "+self.felder[5]+" \n\n "+self.felder[6]+" ¦ "+self.felder[7]+" ¦ "+self.felder[8]+" ")

    def menschendurch(self):
        Menschen = ["X","O","X","O","X","O","X","O","X"]
        for self.i in (Menschen):
            self.check1()
            self.play()

    def check1(self):
        self.checkcounder = 0
        for ii in range(len(self.kombis)):
            self.maincheck(ii)

    def maincheck(self,ii):
        kombo = self.kombis[ii]
        if self.felder[kombo[0]-1] == (" "):
            self.checkcounder = self.checkcounder + 1
        elif self.felder[kombo[0]-1] == self.felder[kombo[1]-1] == self.felder[kombo[2]-1]:
            self.win()
        else:
            self.checkcounder = self.checkcounder + 1 

    def win(self):
        self.finalcheck = self.finalcheck +1
        if self.finalcheck == 1:
            if self.i == "O":
                g = "X"
            else:
                g = "O"
            print("Spieler "+g+" hat gewonnen!!!")

    def play(self):
        if self.checkcounder == len(self.kombis):
            print("Spieler "+ self.i + " ist an der Reihe.")
            self.feld = input("Dein Gewünschtes Feld: ")
            self.freecheck()
            self.brett()


    def freecheck(self):
        if self.felder[int(self.feld)-1] == " ":
            self.felder[int(self.feld)-1] = str(self.i)

haupt = Main()
haupt.brett()
haupt.menschendurch()
