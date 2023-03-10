def greedy():
    # timp_munca = input('Timpul de lucru: ')
    # timp_masini = []
    # timp_ramas = timp_munca
    # n = int(input('Numarul total de masini: '))
    # for i in range(0, n):
    #         l = int(input())
    #         timp_masini.append(l)
    # timp_masini.sort()
    # print(timp_masini)
    #

    lista_timp_reparatie_masini = [2, 4, 20, 15, 60, 10, 25, 40]
    T = int(input('Timp maxim de lucru: '))
    lista_masini_reparate = []
    lista_timp_reparatie_masini.sort()
    t_ramas = T
    i = 0 # element de parcurgere

# Var 1 for

    # for i in range(len(lista_timp_reparatie_masini)):
    #     if lista_timp_reparatie_masini[i]>=t_ramas:
    #         t_ramas = t_ramas - lista_timp_reparatie_masini[i]
    #         lista_masini_reparate.append(lista_timp_reparatie_masini[i])
    # print(lista_masini_reparate)
    # print(t_ramas)

#Var 2 while

    # while t_ramas > 0 and i<len(lista_timp_reparatie_masini[i]:
    #     if lista_timp_reparatie_masini <= t_ramas:
    #         t_ramas = t_ramas - lista_timp_reparatie_masini[i]
    # i = i + 1
    # print(i)
    # print(lista_masini_reparate)
    # print(t_ramas)
def suma_rec(lista):
    lista = []
        if len(lista) == 1:
            return lista[0]
        else:
            mijloc = len(lista) // 2
            return suma_rec(lista[:mijloc]) + suma_rec(lista[mijloc:])

if __name__ == '__main__':
    suma_rec
