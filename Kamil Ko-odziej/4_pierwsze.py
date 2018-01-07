pierwsze=[]
for i in range(2,101):
    for dz in range(2,i):
        if i % dz == 0:
            pierwsze.append(i)
    if pierwsze.count(i) == 0:
        print(i)