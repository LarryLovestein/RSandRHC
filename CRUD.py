def afisareMeniu():
    print("1.Citire de la tastatura")
    print("2.Citire din fisier")
    print("3.Verifica daca incap in ghiozdan")
    print("4.Generare cele k cazuri, aflare best value and avg ")
    print("5.Random Hill-Climbing")
    print("6.Plotare fisier")
    print("0.EXIT")
def afisareSubmeniu():
    print("1.Random search(20)")
    print("2.Random search(200)")
    print("3.Random Hill Climbing")

def citireTastatura(n):
    listaGreutati = list()
    listaValori = list()
    for i in range(0, n):
        greutate = int(input("Greutate: "))
        valoare = int(input("Valoare: "))
        listaGreutati.append(greutate)
        listaValori.append(valoare)

    return listaGreutati, listaValori
def citireFisier(numefis):
    listaGreutate=list()
    listaValori=list()
    f=open(numefis,"r")
    n=int(f.readline())
    for i in range(n):
        line=f.readline()
        listaGreutate.append(int(line.split()[1]))
        listaValori.append(int(line.split()[2]))
    greutateGhiozdan=int(f.readline())
    f.close()
    return n, listaGreutate, listaValori, greutateGhiozdan

def writeInFile(numefis,nrIteratiei,valoarea, greutate):
    f=open(numefis,"a")
    f.write(str(nrIteratiei)+" "+str(valoarea)+" "+str(greutate)+"\n")
    f.close()

def citireIstoric(numefis):
    f=open(numefis,"r")
    listaValori=list()
    while True:
        line = f.readline()
        if not line:
            break
        listaValori.append(line.split()[1])
    f.close()
    return listaValori
def writeBestAvg(best, avg,calitatea , numefis):
    f=open(numefis,"a")
    f.write("Cea mai mare valoare este: "+ str(best)+"\n")
    f.write("Valoarea medie este: " + str(avg)+"\n")
    f.write("Calitatea solutiei este: " + str(calitatea) + "\n")

    f.close()

def readValWeight(n,numefis):
    f=open(numefis,"r")
    listaValori=list()
    listaGreutati=list()
    for i in range(int(n)):
        line=f.readline()
        listaValori.append(int(line.split()[1]))
        listaGreutati.append(int(line.split()[2]))
    f.close()
    return listaValori,listaGreutati