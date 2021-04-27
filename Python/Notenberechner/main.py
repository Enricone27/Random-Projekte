import AllesAnzeigen
import NeueNote
import BenötigteNote

befehl = input("Dein Befehl: ")

while befehl != str("Ende") :

    if befehl == str ("Anzeigen"):
        AllesAnzeigen.funk()
    if befehl == str("Neu"):
        NeueNote.funk()
    if befehl == str("NextNote"):
        BenötigteNote.funk()


    befehl = input("Dein Befehl: ")