def czyParzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False


print(czyParzysta(5000))


def oblicz_pierwiastek(liczba, stopien_pierwiastka):
    return liczba ** (1/stopien_pierwiastka) #dlaczego dla 8 i 2 nie zwraca 3.0?

print(oblicz_pierwiastek(8,2))


def oblicz_podzielne(lista_liczb, dzielnik):
    podzielne = 0
    for i in range(lista_liczb[0], lista_liczb[len(lista_liczb)-1]):
        print(lista_liczb[i])
        if i % dzielnik == 0:
            podzielne += 1
        else:
            continue
    return podzielne

print(oblicz_podzielne([1,2,3,4,5,6,7,8], 2))

def oblicz_podzielne1(lista_liczb, dzielnik):
    wynik = 0
    for i in lista_liczb:
        if i % dzielnik == 0:
            wynik += 1
        else:
            continue
    return wynik

print(oblicz_podzielne1([1,2,3,4,5,6,7,8], 2))