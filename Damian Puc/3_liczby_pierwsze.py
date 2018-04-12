print("Zadanie 2")
i=2

while i<=100:
    dzielnik=0
    ile=0
    while dzielnik<=i:
        dzielnik+=1
        if i%dzielnik==0:
            ile+=1
    if ile==2:
        print(i)
    i+=1

print("")