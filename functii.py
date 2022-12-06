import math

sumaglobala = 0 # variabila globala; ca sa fie gasita o declaram ca "global sumaglobala"

def adunare(*a):
    s = 0
    for element in a:
        s += element
    return s

def produs(*b):
    p = 1
    for element in b:
        p = element
    return p

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f*i
    return f

# sa se defineasca o functie care sa adune toate elementele din lista
def adunareelementlista(lista):
    s = 0
    for e in lista:
        s += e
    return s

def adunareelementelistacametoda(lista):
    global sumaglobala      #variabila sumaglobala a devenit variabila global, deci este cautata global(sus)
    for e in lista:
        sumaglobala += e

#citesc de la tastatura un int si vreau sa-l scriu invers

def oglinda(nr):
    return int(str(nr)[::-1])

def prim(n):
    if n <= 1:
        return 0
    if n <= 3:
        return 1

def primulnumarprimmaimic(n):
    ok = 0
    while ok == 0:
        if(prim(n) == 1): #daca nr respectiv este prim(datorita algoritmului precedent)
            ok = 1
        n = n - 1 # numaurl prim gasit devine numarul prim gasit -1
    return n

def lista2(lista, s = 0):
    for e in lista:
        s += e
    return s

def lista3(lista, p = 1):
    for e in lista:
        p *= e
    return p

if __name__ == "__main__":
    # print(adunare(1, 2, 3, 4))
    # print(produs(1, 2, 3, 1))
    # print(factorial(3))
    # print(factorial(4))
    # print(factorial(5))
    # print(factorial(6))
    # print(adunareelementlista([1, 2, 3]))
    # print(adunareelementelistacametoda([1, 2, 3]))
    # adunareelementelistacametoda([1, 2, 3])
    # print(sumaglobala)
    # print(oglinda(678))
   print(lista3([1, 2, 3, 4, 5], 10))
