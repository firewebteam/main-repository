imie = "Arnold"
haslo = "icra2013"
saldo = 2130
i = input("Wprowadz imie:")
if i == imie:
    h = input("Wprowadz haslo:")
    if h == haslo:
        print('Hasło prawidłowe')
        while True:
            co = int(input('Wpłacasz(1), wypłacasz(2) czy wychodzisz z konta(3):'))
            if co == 3:
                print('Do zobaczenia!')
                break
            elif co == 2:
                y = int(input('Wprowadz kwote jaką chcesz wypłącić:'))
                if y > saldo:
                    print('Masz na koncie tylko %i zł, idź do roboty!' % saldo)
                    continue
                else:
                    saldo -= y
                    print('wypłaciłeś %i zł, pozostało Ci %i zł' % (y, saldo) )
                    continue
            elif co == 1:
                y = int(input('Wprowadz kwote jaką chcesz wpłacić:'))
                saldo += y
                print('wpłaciłeś %i zł, posiadasz teraz %i zł' % (y, saldo))
    else:
        print('Hasło nieprawidłowe')