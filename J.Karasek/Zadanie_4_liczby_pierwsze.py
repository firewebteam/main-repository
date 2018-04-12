for num in range(1,101):
    if num > 1:                   #liczba pierwsza musi być większaod zera
        for i in range(2, num):   #od 2,bo przecież każda liczba dzieli się przez 1
            if num % i == 0:      #szuka dzielników rozważanych liczb
                break             #jeśli dzielnik się znajdzie, to pętla jest przerywana i poszukiwana jest kolejna liczba num
        else:                     #jeśli num przejdzie przez pętlę bez znajdywania żadnych dzielnków,
            print(num)            #to oznacza, że jest podzielna tylko przez 1 i przez samą siebie, zatem jest liczbą pierwszą







