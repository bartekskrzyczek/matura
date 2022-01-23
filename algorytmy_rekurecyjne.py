# Zapisz algorytm w wybranej przez siebie notacji, obliczający sumę liczb parzystych mniejszych od 100

def suma_liczb_parzystych(n):
    if n % 2 == 0:
        if n == 2:
            return 2
        else:
            return suma_liczb_parzystych(n-1) + n
    else:
        return suma_liczb_parzystych(n-1)

print(suma_liczb_parzystych(100))