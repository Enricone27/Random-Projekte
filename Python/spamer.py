import os, time
t1 = time.time()
size = 0
while size < 1000000000:
    o2 = open ("spamtext", "a")
    for ii in range(2000):
        o2.write("lol") 
    o2.close()
    dok = os.stat("spamtext")
    size = dok.st_size
    print(size)

o2.close()

print(size)
t2 = time.time()
print(t2-t1)
time.sleep(60)