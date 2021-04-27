import datetime,time
for i in range(10):
    zeit = (datetime.datetime.now().strftime("%H:%M:%S"))
    stund = int(zeit[0:2])

    if stund >= 17:
        leke = (15 + ((stund-17)*45))%60
    elif stund < 10:
        leke = (50 + ((stund-8)*55))%60
    else :
        leke = (50 + ((stund-10)*55))%60

    sec = int(zeit[6:8])
    minu = (int(zeit[3:5])-0)

    if leke < minu:
        leke = (leke + 55)%60

    if leke != 45 :
        minu = (minu - (leke-45))%60

    minproz = (100/(45*60))*((minu*60)+sec)
    if minproz > 100:
        minproz= -(100/3 -(minproz-100))
    proz= (round(minproz,2))
    print(str(proz)+"%")
    time.sleep(5)