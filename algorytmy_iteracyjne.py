#Zapisz algorytm w wybranej przez siebie notacji, obliczający sumę liczb parzystych mniejszych od 100.


def  oblicz_sume_liczb_parzystych_mniejszych_od_100():
    sum = 0
    for i in range(0, 100):
        if i % 2 == 0:
            sum = i + sum # sum +- i
    print(sum)

oblicz_sume_liczb_parzystych_mniejszych_od_100()


#Zapisz algorytm w wybranej przez siebie notacji, obliczający silnię z zadanej liczby.

def oblicz_silnie(liczba):
    i = 0
    suma = 1
    while(liczba!=i):
        i+=1
        suma = suma * i
        print(suma)

oblicz_silnie(5)

#Przedstaw algorytm iteracyjny (w formie pseudokodu, listy kroków lub kodu języka programowania) obliczający sumę liczb nieparzystych mniejszych od 100.

def obliczSumeLiczbNieparzystych():
    sum = 0
    for i in range (0,100):
        if i % 2 == 1:
            sum = i + sum
    print(sum)

obliczSumeLiczbNieparzystych()

#Przedstaw algorytm iteracyjny (w formie pseudokodu, listy kroków lub kodu języka programowania) obliczający sumę pierwszych pięciu elementów ciągu,
# w którym pierwszym elementem jest liczba 2, a każdy kolejny element to poprzednia liczba podniesiona do potęgi. Tzn.: 2, 4, 16,
# 256 itd.

def sumaCiagu(liczba):
    wartosc = 2
    sum = wartosc
    for i in range (1,liczba):
        wartosc *= wartosc
        sum = sum + wartosc
    print(sum)

sumaCiagu(5)

#Przedstaw algorytm iteracyjny (w formie pseudokodu, listy kroków lub kodu języka programowania) obliczający kwotę z odsetek uzyskaną w ciągu 5 lat.
# Załóż, że kwota startowa to 10 000 zł, rocznie kwota zwiększana jest o 5%, a z zysku rocznego należy odprowadzić 19% podatku.



def oblicz_kwote_odsetek():
    kwota_startowa = 10000
    kwota_odsetek = 0
    kwota_odsetek_opodatkowanych = 0
    suma_odsetek = 0
    wynik = 0
    for i in range(0,5):
        kwota_odsetek = kwota_startowa * 0.05
        kwota_odsetek_opodatkowanych = kwota_odsetek + 0.81
        kwota_startowa = kwota_startowa + kwota_odsetek_opodatkowanych
        wynik = wynik + kwota_odsetek_opodatkowanych
    print(wynik)

oblicz_kwote_odsetek()