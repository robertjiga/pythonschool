import math

l = [10, 20, 30, 1, 4, 6, 100, 34, 50, 56]


def cautare_secventiala():
    n = len(l)
    for i in range(n):
        if ls[i] == val:
            return i
        return -1


def cautare_suma():
    cautat = int(input("Introduceti elementul cautat: "))
    # print("Introduceti elementul cautat: ")
    # cautat = int(input())
    s = 0
    for index in range(len(l)):
        if index >= 3 and index <= 7:  # cautare de la index 3 inclusiv la index 7 inclusiv
            s += l[index]
            if l[index] == cautat:
                print('Am gasit elementul la index: ', index)


def cautare_salt():
    val = int(input('Introduceti valoarea cautata: '))
    ls = sorted(l)  # sortarea listei
    n = len(ls)  # lungimea listei sortate
    salt = int(math.sqrt(n))  # pasul, radical din n
    for i in range(0, n, salt):  # i de la 0 la n
        if ls[i] < val:
            st = i
        elif ls[i] == val:
            return i
        else:
            break
    for i in range(st, st + salt):
        if ls[i] == val:
            return i
        return -1


if __name__ == '__main__':
    # cautare_suma()
    cautare_salt()
