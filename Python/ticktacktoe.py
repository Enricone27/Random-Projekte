felder = [" "," "," "," "," "," "," "," "," "]
kombis = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
finalcheck = 0
brett = " "+felder[0]+" ¦ "+felder[1]+" ¦ "+felder[2]+" \n\n "+felder[3]+" ¦ "+felder[4]+" ¦ "+felder[5]+" \n\n "+felder[6]+" ¦ "+felder[7]+" ¦ "+felder[8]+" "
Menschen = ["X","O","X","O","X","O","X","O","X"]
for i in (Menschen):
    checkcounder = 0
    for ii in range(len(kombis)):
        kombo = kombis[ii]

        if felder[kombo[0]-1] == (" "):
            checkcounder = checkcounder + 1
            #print("check3")

        elif felder[kombo[0]-1] == felder[kombo[1]-1] == felder[kombo[2]-1]:
            finalcheck = finalcheck +1
            if finalcheck == 1:
                if i == "O":
                    g = "X"
                else:
                    g = "O"
                print("Spieler "+g+" hat gewonnen!!!")

        else:
            #print("check2")
            checkcounder = checkcounder + 1  
                
            

    #print(checkcounder)
    #print("check1")
    if checkcounder == len(kombis):
        print("Spieler "+ i + " ist an der Reihe.")
        feld = input("Dein Gewünschtes Feld: ")
        if felder[int(feld)-1] == " ":
            felder[int(feld)-1] = str(i)
        brett = " "+felder[0]+" ¦ "+felder[1]+" ¦ "+felder[2]+" \n\n "+felder[3]+" ¦ "+felder[4]+" ¦ "+felder[5]+" \n\n "+felder[6]+" ¦ "+felder[7]+" ¦ "+felder[8]+" "
        print (brett)          