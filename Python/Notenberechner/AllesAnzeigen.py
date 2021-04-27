def funk ():
    fach = input("Das Fach: ")
    offen = open (fach, "r")
    liste1 = (offen.readlines())
    listenoten = []
    nummernoten = len(liste1)
    gewichtsum = 0
    for i in range(nummernoten):
        es = liste1[i]
        aknot = float(es[4:-1])
        zs = aknot*int(es[0:3])/100
        print("Deine "+ str(i+1) +". Note: "+ es[4:-1] + "; Gewichtung der Notein %: " +es[0:3])
        listenoten.append(zs)
        gewichtsum = gewichtsum + int(es[0:3])
        i = i + 1

    summenoten = 0
    for ii in listenoten:
        summenoten = summenoten + float(ii)
    durchschnitt = summenoten/(gewichtsum/100)

    print("Dein Notendurchschnitt in "+ fach +": " + str(durchschnitt))

