def funk ():
    fach = input("Das Fach: ")
    gewüschnitt = input("Gewünschter Schnitt im Fach: ")
    offen = open (fach, "r")
    liste1 = (offen.readlines())
    listenoten = []
    nummernoten = len(liste1)
    gewichtsum = 0
    for i in range(nummernoten):
        es = liste1[i]
        zs = float(es[4:-1])*int(es[0:3])/100
        listenoten.append(zs)
        gewichtsum = gewichtsum + int(es[0:3])
        i = i + 1

    summenoten = 0
    for ii in listenoten:
        summenoten = summenoten + float(ii)
    durchschnitt = summenoten/(gewichtsum/100)

    nötigenote = ((nummernoten+1)* gewüschnitt)-summenoten  

    print("Im nächsten "+ fach +" Test barachst du eine: " + str(nötigenote))