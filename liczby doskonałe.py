suma = 1
n=1
liczby_doskonale = []
dot=10
ile=1
b = 3
a = 0
while True:
    suma += 2**n
    if suma>dot:
        print("10^", ile)
        dot*=10
        ile += 1
    while True:

        if suma != 2:
            if (suma % 2) == 0:
                a = 1
            else:
                while b <= (suma/2):
                    if suma % b == 0:
                        a = 1
                    b += 2
        if a == 1:
            break
        else:
            liczby_doskonale.append(suma*(2**n))
            print(liczby_doskonale)
            break
    n+=1