stand = [[0,15,0.020502],
        [1,15,0.197063],
        [2,31,0.788251],
        [3,46,2.365],
        [5,2,6.306],
        [7,33,18.918],
        [10,4,50.448],
        [18,53,69.618],
        [37,45,266.608],
        [94,22,1299]]


total = 0
for i in stand:
    längm = i[0] * 60
    längs = i[1]
    gewinn = i[2]
    sec = (gewinn/(längs+längm))
    print(sec)
    total = total + sec
print("\n")
print ((1000 / total)/60)