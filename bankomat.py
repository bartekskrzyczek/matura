pin_użytkownika = '0055'
stan_konta = 1000

# Napisz swój kod poniżej...

def weryfikujPin():
    iloscProb = 2
    while True:
        pin = input('Podaj PIN: ')
        if (pin_użytkownika == pin):
            wybierzMenu(stan_konta=1000)
            break

        elif (iloscProb == 0):
            print('Zbyt duża ilość prób. Zostałeś wylogowany')
            break

        else:
            iloscProb = iloscProb - 1
            print('Ilość logowań do wykorzystania ' + str(iloscProb))

def wybierzMenu(stan_konta=1000):
    kurs_euro = 4.7
    numerOpchesseracji = 0
    wyplata = 0
    print('1.Wyświetl stan konta\n2.Wpłać środki\n3.Wypłać środki\n4.Wyświetl stan konta w EURO\n5.Zakończ')
    numerOperacji = int(input('Wybierz numer operacji: '))
    print(numerOperacji)
    if numerOperacji == 1:
        print('Twój stan konta wynosi: ' + str(stan_konta))
        wybierzMenu(stan_konta)
    elif numerOperacji == 2:
        print(stan_konta)
        kwota = 0
        kwota = int(input('Podaj kwotę, którą chcesz wpłacić: '))
        if kwota > 0:
            stan_konta = stan_konta + kwota
            print('Wpłacono ' + str(kwota) + ' złotych')
            print(stan_konta)
            wybierzMenu(stan_konta)
        else:
            print('Podana kwota nie jest poprawna')
            wybierzMenu(stan_konta)
    elif numerOperacji == 3:
        wyplata = int(input('Podaj kwotę, którą chcesz wypłacić: '))
        if (stan_konta > 0 and wyplata > 0):
            print(stan_konta)
            stan_konta = stan_konta - wyplata
            print(stan_konta)
            wybierzMenu(stan_konta)
        else:
            print('operacja się nie udała, ponieważ podano niepoprawną kwotę.')
            wybierzMenu()
    elif numerOperacji == 4:
        stan_konta_w_euro = stan_konta / kurs_euro
        print('Twój stan konta w euro wynosi: ' + str(stan_konta_w_euro))
        wybierzMenu()
    elif numerOperacji == 5:
        weryfikujPin()
    else:
        print('Nie rozpoznano operacji. Sprawdź podany numer operacji.')
        wybierzMenu()

weryfikujPin()
