def funk10 ():
    o1 = open ("Daten" , "r+")
    o1.seek(0,2)
    o1.write("0000")

funk10()