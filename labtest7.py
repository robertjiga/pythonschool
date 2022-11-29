import math

l = [1, 6, 23, 65, 85, 1278, 88, 69, 420, 33, 16]

# def jumatati_prod():
#     element = []
#     # produs = 0
#     for index in range[len(l)]:
#         if index > 5:
#            elj = element/2
#            produs = math.prod(elj)
#            # produs *= l[elj]
#            print("Produsul jumatatilor este: ", produs)
#
#
# def cautare_element():
#     cautare = int(input('Elementul cautat este: '))
#     n = len(l)
#         for element in n:
#             if element == cautare
#                 return element
#             return -1
#     print(element * element/2 + element**4)

# def cautareprof():
#     val = int(input())
#     for i in range(len(l))
#         print(val*val/2 + val ** 4)
#
# def produsprof():
#     produs = 1
#     for i in range(len(l)):
#         if i > 5:
#             produs = produs * l[i]/2
#     print(produs)

# print(l[5:])


def cautareenspe():
    l.sort()
    n = len(l)
    salt = int(math.sqrt(n))
    val = int(input())
    for i in range(0, n, salt):
        if l[i] < val :
            start_lista_viitoare = i
        elif l[i] == val :
            print(i)
        else:
            break
    #daca am gasit zona din lista unde se gaseste elementul meu, continuam cu o cautare secventiala
    flg = 0
    for i in range(start_lista_viitoare, start_lista_viitoare + salt):
        if l[i] == val:
            print(i)
            flg = 1
    if flg == 0:
        print("Nu am gasit elementul")



print(l.sorted())


if __name__ == '__main__':
    # jumatati_prod()
    # cautare_element()
    cautareenspe()



