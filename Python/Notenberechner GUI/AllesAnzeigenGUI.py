def funk ():
    menu = Menu(self.master)
    self.master.config (menu = menu)

    file = Menu(menu)
    menu.add_cascade(label="Das Fach", menu=file)
    file.add_command(label="Bio", command= lambda: fach = "Bio")
    file.add_command(label="PAM", command= lambda: fach = "PAM")
    

    
    offen = open (fach, "r")
    liste1 = (offen.readlines())
    listenoten = []
    nummernoten = len(liste1)
    gewichtsum = 0
    for i in range(nummernoten):
        es = liste1[i]
        zs = float(es[4:-1])*int(es[0:3])/100
        print("Deine "+ str(i+1) +". Note: "+ es[4:-1] + "; Gewichtung der Notein %: " +es[0:3])
        listenoten.append(zs)
        gewichtsum = gewichtsum + int(es[0:3])
        i = i + 1

    summenoten = 0
    for ii in listenoten:
        summenoten = summenoten + float(ii)
    durchschnitt = summenoten/(gewichtsum/100)

    print("Dein Notendurchschnitt in "+ fach +": " + str(durchschnitt))

