kontakty = {'Paweł':123456789, 'Marek':147258369, 'Julia':147963258, 'Katarzyna':123654789, 'Ola':159482673}
co = 0
while co != 4:
    co = int(input('Co chcesz zrobić?:\n'
                '1 - wyświetl listę kontaktów\n'
                '2 - dodaj kontakt\n'
                '3 - usuń kontakt\n'
                '4 - wyjdź'))
    if co == 1:
        for kontakt,numer in kontakty.items():
            print(kontakt, 'ma numer telefonu:', numer)
        continue
    elif co == 2:
        x = str(input('Podaj imię:'))
        if x in kontakty:
            print('Ten kontakt już istnieje')
            break
        y = int(input('Podaj numer telefonu:'))
        kontakty[x] = y
        print(x, 'został dodany. Jego numer to ', y, '.')
    elif co == 3:
        d = str(input('Podaj imię kontaktu do usunięcia:'))
        if d in kontakty:
            kontakty.pop(d)
            print('Kontakt "%s" został usunięty.' % d)
        else:
            print('Taki kontakt nie istnieje.')
    elif co == 4:
        print('Do widzenia!')
    else:
        print('Niestety podałeś nieprawidłową komendę :/')