B = [7,4,6,7,9,13,1,10,4]
A2 = set()
# WYNIK: 10

A.sort(reverse=True)
print(A)

# O(n)
def znajdz_2_max(A):
    max = A[0]
    max_2 = A[0]

    for liczba in A:
        if liczba > max:
            if max > max_2:
                max_2 = max
            max = liczba
        elif liczba > max_2:
            max_2 = liczba

print(max_2)