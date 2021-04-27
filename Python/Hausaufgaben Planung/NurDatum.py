import datetime

def funk2 (n):
    o1 = open ("Daten", "r")
    liste = (o1.readlines())

    l = liste[n]
    dt = l[0:8]
    print (dt)


    dj = (datetime.datetime.now().strftime("%d.%m.%y"))
    print(dj)

    def Monatherausfindenvorne ():
        z = int(dt[3:5]) - int(dj[3:5])
        jahr = [31,28,31,30,31,30,31,31,30,31,30,31]
        b = int(dj[3:5]) - 1
        x = 0
        for i1 in range(z):
            x = x + jahr[int(b)]
            b = int(b)+1
        return x
    def Monatherausfindenhinten ():
        z = int(dj[3:5]) - int(dt[3:5])
        jahr = [31,28,31,30,31,30,31,31,30,31,30,31]
        b = int(dj[3:5]) - 2
        x = 0
        for i1 in range(z):
            x = x + jahr[int(b)]
            b = int(b)-1
        return x
    def Jahrherausfinden ():
        b = int(dt[6:8]) - int(dj[6:8])
        c = 365 * b
        return (c)            
    if dt[6:8] == dj[6:8]:                  #gleiches Jahr
        print(dj[6:8] + "ja1")

        if dt[3:5] == dj[3:5]:              #gleiches Jahr; gleicher Monat
            print(dj[3:5] + "ja1.1")

            if dt[0:2] == dj[0:2]:          #gleiches Jahr; gleicher Monat; gleicher Tag;
                print(dj[0:2] + "ja1.1.1")
                a = 0

            elif dt[0:2] > dj[0:2]:         #gleiches Jahr; gleicher Monat; späterer Tag
                print(dj[0:2] + "ja1.1.2")
                a = int(dt[0:2]) - int(dj[0:2])

        elif dt[3:5] > dj[3:5]:             #gleiches Jahr; späterer Monat
            print(dj[3:5] + "ja1.2")

            if dt[0:2] == dj[0:2]:          #gleiches Jahr; späterer Monat; gleicher Tag
                print(dj[0:2] + "ja1.2.1")
                a = Monatherausfindenvorne()

            elif dt[0:2] > dj[0:2]:         #gleiches Jahr; späterer Monat; späterer Tag
                print(dj[0:2] + "ja1.2.2")
                a = Monatherausfindenvorne() + (int(dt[0:2]) - int(dj[0:2]))

            elif dt[0:2] < dj[0:2]:         #gleiches Jahr; späterer Monat; früherer Tag
                print(dj[0:2] + "ja1.2.3")
                a = Monatherausfindenvorne() - (int(dj[0:2]) - int(dt[0:2]))
    

    elif int(dt[6:8]) > int(dj[6:8]):       #späteres Jahr;
        print (dj[6:8] + "ja2")

        if dt[3:5] == dj[3:5]:              #späteres Jahr; gleicher Monat
            print(dj[3:5] + "ja2.1")

            if dt[0:2] == dj[0:2]:          #späteres Jahr; gleicher Monat; gleicher Tag;
                print(dj[0:2] + "ja2.1.1")
                a = Jahrherausfinden()

            elif dt[0:2] > dj[0:2]:         #späteres Jahr; gleicher Monat; späterer Tag
                print(dj[0:2] + "ja2.1.2")
                a = Jahrherausfinden() + (int(dt[0:2]) - int(dj[0:2]))

            elif dt[0:2] < dj[0:2]:         #späteres Jahr; gleicher Monat; früherer Tag
                print(dj[0:2] + "ja2.1.3")
                a = Jahrherausfinden() - (int(dj[0:2]) - int(dt[0:2]))

        elif dt[3:5] > dj[3:5]:             #späteres Jahr; späterer Monat
            print(dj[3:5] + "ja2.2")

            if dt[0:2] == dj[0:2]:          #späteres Jahr; späterer Monat; gleicher Tag
                print(dj[0:2] + "ja2.2.1")
                a = Jahrherausfinden() + Monatherausfindenvorne()

            elif dt[0:2] > dj[0:2]:         #späteres Jahr; späterer Monat; späterer Tag
                print(dj[0:2] + "ja2.2.2")
                a = Jahrherausfinden() + Monatherausfindenvorne() + (int(dt[0:2]) - int(dj[0:2]))

            elif dt[0:2] < dj[0:2]:         #späteres Jahr; späterer Monat; früherer Tag
                print(dj[0:2] + "ja2.2.3")
                a = Jahrherausfinden() + Monatherausfindenvorne() - (int(dj[0:2]) - int(dt[0:2]))

        elif dt[3:5] < dj[3:5]:             #späteres Jahr; früherer Monat
            print(dj[3:5] + "ja2.3")

            if dt[0:2] == dj[0:2]:          #späteres Jahr; früherer Monat; gleicher Tag
                print(dj[0:2] + "ja2.3.1")
                a = Jahrherausfinden() - Monatherausfindenhinten()

            elif dt[0:2] > dj[0:2]:         #späteres Jahr; früherer Monat; späterer Tag
                print(dj[0:2] + "ja2.3.2")
                a = Jahrherausfinden() - Monatherausfindenhinten() + (int(dt[0:2]) - int(dj[0:2]))

            elif dt[0:2] < dj[0:2]:         #späteres Jahr; früherer Monat; früherer Tag
                print(dj[0:2] + "ja2.3.3")
                a = Jahrherausfinden() - Monatherausfindenhinten() - (int(dj[0:2]) - int(dt[0:2]))
    return (a)

a = funk2(0)
print(a)

def funk3 (n):
    o1 = open ("Daten", "r+")
    liste = (o1.readlines())

    l = liste[n]
    dt = l[0:8]
    print (dt)

    o1 = open ("Daten" , "r+")
    o1.seek(0,2)
    o1.write("0000")
    #noch nichts gemacht