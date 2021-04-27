import AllesAnzeigen
import DatumErmitteln
import NeuerEintrag

befehl = input("Dein Befehl: ")

while befehl != str("Ende") :
    if befehl == str("1"):
        print ("Hallo")
    
    if befehl == str("2"):
        print ("Tschüss")

    if befehl == str ("Anzeigen"):
        AllesAnzeigen.funk1()
    if befehl == str("Neu"):
        NeuerEintrag.funk()


    befehl = input("Dein Befehl: ")