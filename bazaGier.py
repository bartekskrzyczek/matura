baza = [{"tytuł": "GTA V", "rok wydania": 2013, "gatunek": "gra akcji", "ocena": "9"}, {"tytuł": "GTA IV", "rok wydania": 2011, "gatunek": "gra akcji", "ocena": "8"},
        {"tytuł": "GTA III", "rok wydania": 2009, "gatunek": "gra akcji", "ocena": "7"}, {"tytuł": "Driver", "rok wydania": 2007, "gatunek": "gra akcji", "ocena": "6"},
        {"tytuł": "AA", "rok wydania": 2007, "gatunek": "gra akcji", "ocena": "6"}]

#baza.sort(key=lambda x: x.get('tytuł'))
#print(baza['tytuł'], end='\n\n')
#ten sposób na



def wyswietlMenu():
    while True:
        print(
            '1.Wyświetl nazwy wszystkich gier w bazie\n2.Wyświetl wszystkie gry w bazie\n3.Wyświetl TOP 5 gier w bazie\n4.Wyświetl gry z gatunku\n5.Dodaj grę do bazy\n6.Edytuj grę w bazie\n7.Usuń grę z bazy\n8.Wyświetl informacje o grze\n9.Oceń grę\n10.Zapisz dane do pliku\n11.Odczytaj dane z pliku\n12.Zakończ')
        numerOperacji = int(input('Wybierz numer operacji: '))

        if (numerOperacji == 1):
            baza.sort(key=lambda x: x.get('tytuł'))
            for gra in baza:
                print(gra["tytuł"])
            wyswietlMenu()

        if (numerOperacji == 2):
            baza.sort(key=lambda x: x.get('tytuł'))
            for gra in baza:
                print(gra)
            wyswietlMenu()

        if (numerOperacji == 3):
            baza.sort(key=lambda x: x.get('ocena'),reverse=True)
            for gra in baza:
                print(gra)
            wyswietlMenu()




wyswietlMenu()



