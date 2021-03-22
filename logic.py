import numpy as np
from CRUD import *
def generareRandom(n):
    pozitii = np.random.randint(2, size=n)
    return pozitii

'''
    Input: o lista cu greutati, greuatea maxima acceptata si un vector
        random de pozitii
    Output: returneaza suma daca este mai mica sau egala decat greutatea maxima
            si -1 daca este mai mare
'''
def verificareGhiozdan(greutati, greutateGhiozdan, pozitii):
    suma = 0
    for i in range(0,len(pozitii)):
        suma = suma + pozitii[i] * greutati[i]
    if suma <= greutateGhiozdan:
        return suma
    else:
        return -1

def detValoare(pozitii, valori):
    valoarea=0
    for i in range(0, len(pozitii)):
        valoarea=valoarea+pozitii[i]*valori[i]
    return valoarea


def detCele10Teste(k, greutati, greutateGhiozdan, valoari, n, numefis):

    i=1
    while i <= k:
        pozitii=generareRandom(n)
        if verificareGhiozdan(greutati,greutateGhiozdan,pozitii) != -1: #se verifica daca solutia generata incape in ghiozdan
            valoare=detValoare(pozitii,valoari)                              #se det valoarea ei
            greutate=verificareGhiozdan(greutati,greutateGhiozdan,pozitii)      #se det greutatea ei
            writeInFile(numefis, i, valoare,greutate)                       #se scrie in fisier nr iteratiei valoarea si greutate
            #print(pozitii,valoare, verificareGhiozdan(greutati,greutateGhiozdan,pozitii))
            i=i+1
        else:
            continue

def detBestAvg(listaValori):
    integer_map=map(int,listaValori)        # am folosit map sa fac dintr-o lista de string o lista de int
    listaVal=list(integer_map)
    avg = sum(listaVal)/len(listaVal)
    maxim= max(listaVal)
    calitate= maxim/avg
    return avg, maxim, calitate

def detGreutateMaxima( maxim, listaValori,listaGreutati ):
    listagrmaxime=list()
    for i in range(len(listaValori)):
        if listaValori[i] == maxim :
            listagrmaxime.append(listaGreutati[i])
    return listagrmaxime

def generarePctRndValid(n,greutati, greutateGhiozdan):
    while True:
        pozitii=generareRandom(n)
        if verificareGhiozdan(greutati, greutateGhiozdan, pozitii) != -1 and verificareGhiozdan(greutati, greutateGhiozdan, pozitii) != 0:
            break
        else:
            continue
    return pozitii

def RHC(incercari, punctC, greutati, greutateGhiozdan):# punctC ii vectorul de pozitii
    inc=0
    pozitii = punctC    # copie pentru pucntulC
    while inc <= int(incercari): #Daca numarul de incercari a fost atins atunci se intrerupe while-ul si se returneaza punctulC
        vecin = np.random.randint(0,len(punctC))        #luam un pct random intre 0 si lungeam listei
        if punctC[ vecin ] == 1:            #luam un veci, adica daca pe pct respectiv e 0 atunci il facem 1 si daca e 1 crestem nr de incercari
            inc = inc + 1
        if punctC[vecin] == 0:
            pozitii[ vecin ] = 1          #Daca pct a fost transformat in 1 atunci verificam daca depaseste greutatea ghiozdanului
            if verificareGhiozdan(greutati,greutateGhiozdan,pozitii) != -1:
                punctC = pozitii        #Daca nu depaseste greutatea ghiozdanului punctulC devine pozitia cea noua
            else:
                punctC[vecin] = 0
                inc = inc +1            #altfel creste inc care reprezinta nr de icnercari

    return punctC




