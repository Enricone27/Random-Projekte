
def funk ():
    fach = input("Das Fach deiner Note: ")
    note = input("Die Note: ")
    provgewicht = input("Die Gewichtung der Note in %: ")
    
    if len(provgewicht) <3:
        gewicht = "0"+provgewicht
    else:
        gewicht = provgewicht

    o1 = open (fach, "r")
    liste = (o1.read())
    o2 = open (fach, "w")
    liste = liste +gewicht + " "+ note + "\n" 
    o2.write(liste)  
    
