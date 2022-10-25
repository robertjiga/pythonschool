def adunare2():
    print('Introduceti un natural de doua cifre:')
    n = int(input())
    x = n // 10
    y = n % 10
    print('Numarul rezultat prin adunarea cifrelor zecilor si unitatilor este:', x+y)


def adunare3():
    print('Introduceti un natural de TREI cifre:')
    n = int(input())
    x = n // 100
    y = (n // 10 ) % 10
    z = n % 10
    print('Numarul rezultat prin adunarea cifrelor sutelor, zecilor si unitatilor este:', x+y+z)

def adunare4():
    print('Introduceti numarul de gaini(G) din curte:')
    g = int(input())
    print('Introduceti numarul de oi(O) din curte')
    o = int(input())
    print('Suma capetelor animalelor este:', g+o, ', iar suma picioarelor este: ', g*2 + o*4)

def arievolum():
    print('Introduceti lungimea laturii(metri):')
    l = int(input())
    print('Aria cubului este:',(l**2)*6,'metri patrati, iar volumul cublui este:', l**3, 'metri cubi')

def adunare5():
    print('Introduceti un natural de TREI cifre:')
    n = int(input())
    x = n // 100
    y = n % 10
    print('Numarul rezultat prin eliminarea cifrei din mijloc este:', str(x) + str(y))

def calcultimp():
    print('Introduceti ora: ')
    h = input()
    print('Introduceti minutul: ')
    m1 = int(input())
    print('Introduceti perioada de timp in minute: ')
    m2 = int(input())
    mx = str(m1 + m2)
    print('Peste', m2, 'minute, ceasul va fi',h, 'ore si' ,mx, 'minute')

def produscifre():
    print('Introduceti un natural din TREI cifre:')
    n = int(input())
    x = n // 100
    z = n % 10
    print('Produsul cifrei sutelor cu cifra unitatilor este:', x*z)

def totalgloburi():
    print('Introduceti numarul de globuri albe: ')
    a = int(input())
    r = a*2
    v = r-3
    print('Numarul de globuri rosii este: ',r)
    print('Numarul de globuri verzi este: ',v)
    print('Numarul total de globuri este: ',a+r+v)

def sumaluigauss():
    print('Introduceti un numar natural:')
    a = int(input())
    g = (a*(a+1))/2
    print('Suma lui Gauss pentru',a, 'este',g,)

def sumaanimale():
    print('Introduceti numarul de caini: ')
    c = int(input())
    p = 2*c
    g = 2*p
    print('Numarul de pisici este ' ,p, ', numarul de gaini este' ,g,', iar numarul de animale in total este' ,c+p+g)

if __name__ == '__main__':
    # adunare2()
    # adunare3()
    # adunare4()
    # arievolum()
    # adunare5()
    # calcultimp()
    # produscifre()
    # totalgloburi()
    # sumaluigauss()
    sumaanimale()