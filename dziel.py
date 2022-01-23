def znajdx_max_2(A, max2, max, lewy, prawy):

    if lewy == prawy:

    if prawy - lewy == 1:


    # [1,2,3,4,5,6]
    srodek = (lewy + prawy) // 2
    max2, max = znajdz_max_2(A, max2, max, lewy, srodek)
    max2, max = znajdz_max_2(A, max2m, max, srodek + 1, prawy)