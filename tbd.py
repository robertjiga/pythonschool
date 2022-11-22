
def matrice():
    n = 4
    sdp = 0 # Suma Diagonalei Principale
    sds = 0 # Suma Diagonalei Secundare
    matrice = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            if i < j:  # Deasupra Diagonalei PRINCIPALE
                sdp += matrice[i][j]
            if i + j < n - 1:  #  Deasupra Diagonalei SECUNDARE
                sds += matrice[i][j]
    print("SDP=", sdp)
    print("SDS=", sds)


# def matricipatrate():
#     print("x=", end=' ')
#     x = int(input())
#     y = [[0] * x for _ in range(x)]
#     for i in range(x):
#         for j in range(x):
#             print(i, " ", j, end="=")
#             y[i][j] = int(input())
#             y[i][j] = y[i][j] ** 2
#     print

def verificare100():
    n=2
    m=3
    matrice = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            matrice[i][j]=int(input())
            if matrice[i][j] == 100:
                print(i,' ',j)


def matricep2():
    m = 5
    n = 4
    matrice = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j]**2
    print(matrice2)

def matrice3():
    m = 5
    n = 4
    matrice = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            matrice[i][j] = matrice[i][j] + 10
    print(matrice3)


def matrice5():
    n = 3
    m = 4
    suma_p = 0
    suma_i = 0
    matrice = [[0] * n for i in range(m)]
    for i in range(n):
        for j in range(n):
            matrice[i][j] = int(input())
            if matrice[i][j]%2 == 0
                suma_p += matrice[[i][j]
            else 
                suma_i += matrice[[i][j]



if __name__ == '__main__':
    # matrice()
    # matricipatrate()
    # matrix()
    # matrice2()
    # matrice3()
    verificare100()
