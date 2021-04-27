
def funk ():
    def funk2 ():
        o1 = open ("zwischenspeicher", "r")
        f1 = (o1.readline())
        d1 = (f1[0:8])
        print (d1)

    datum = input("Datum des Abgabetermins: (tt.mm.jj)")
    fach = input("Das Fach deiner Aufgabe: ")
    auftrag = input("Der genaue Auftag: ")

    o1 = open ("zwischenspeicher", "w")


    o1.write(str(datum) + " " + str(fach) + " " + str(auftrag))
    o1.seek(0,0)
    funk2()
   

#funk()