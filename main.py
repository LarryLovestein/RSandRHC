from logic import *
import matplotlib.pyplot as plt
import time

def principal():
    ok = True
    while ok == True:
        afisareMeniu()
        x = input("Introdu numarul corespunzaotr: ")
        if x == "1":
            greutateGhiozdan = int(input("greutatea ghiozdnaului"))
            n = int(input("Numarul de elemente a vectorului"))
            print("Citeste lista greutatilor si valorilor corespunzatoare")
            greutati, valori = citireTastatura(n)
            pozitii = generareRandom(n)

        if x == "2":
            numefis=input("numele fisierului:")
            n, greutati, valori, greutateGhiozdan = citireFisier(numefis)

        if x == "3":
            pozitii = generareRandom(n)
            print("Vectorul de pozitii este:",pozitii)
            print("vectorul de greutati este:", greutati)
            if(verificareGhiozdan(greutati, greutateGhiozdan, pozitii)!=-1):
                print("Obiectele incap in ghiozdan"+ str(verificareGhiozdan(greutati, greutateGhiozdan, pozitii)))
            else:
                print("Nu incap in ghiozdna")
        if x == "4":
            start_time = time.time()
            nrRulari=input("Numarul de rulari:")
            i=0
            f = open("BestRH20.txt", "w")
            f.write("")
            f.close()
            f = open("BestRH200.txt", "w")
            f.write("")
            f.close()
            k = int(input("introduceti nr de sol generate"))
            while i<int(nrRulari):
                if n==20:
                    f=open("Istoric.txt","w")
                    f.write("")
                    f.close()
                    detCele10Teste(k,greutati,greutateGhiozdan,valori,n,"Istoric.txt")
                    lvalori, lgreutati = readValWeight(k, "Istoric.txt")
                    avg, maxim, calitate = detBestAvg(citireIstoric("Istoric.txt"))
                    lgrmaxime=detGreutateMaxima(maxim,lvalori,lgreutati)
                    writeBestAvg(maxim, avg, calitate, "Istoric.txt")
                    writeInFile("BestRH20.txt",i,maxim,lgrmaxime)
                    print("Valoarea maxima:"+ str(maxim))
                    print("Valoare medie:"+ str(avg))
                    print("Calitatea solutiei:" +str(calitate))
                if n==200:
                    f = open("Istoric200.txt", "w")
                    f.write("")
                    f.close()
                    detCele10Teste(k, greutati, greutateGhiozdan, valori, n, "Istoric200.txt")
                    lvalori, lgreutati = readValWeight(k, "Istoric200.txt")
                    avg, maxim, calitate = detBestAvg(citireIstoric("Istoric200.txt"))
                    lgrmaxime = detGreutateMaxima(maxim, lvalori, lgreutati)
                    writeBestAvg(maxim, avg, calitate, "Istoric200.txt")
                    writeInFile("BestRH200.txt", i, maxim, lgrmaxime)
                if n!=20 and n!=200:
                    f = open("Tastatura.txt", "w")
                    f.write("")
                    f.close()
                    detCele10Teste(k, greutati, greutateGhiozdan, valori, n, "Tastatura.txt")
                    avg, maxim, calitate = detBestAvg(citireIstoric("Tastatura.txt"))
                    print("Valoarea maxima:" + str(maxim))
                    print("Valoare medie:" + str(avg))
                    print("Calitatea solutiei:" + str(calitate))
                i+=1
            print("--- %s seconds ---" % (time.time() - start_time))

        if x== "5":


            f = open("BestRHC.txt", "w")
            f.write("")
            f.close()
            k=input("introduceti nr de sol generate")
            incercari = input("Citeste nr de incercari maxim admise: ")
            nrRulari=input("Numarul de rulari: ")
            j=1
            start_time = time.time()
            while j <= int(nrRulari):
                f = open("RHC.txt", "w")
                f.write("")
                f.close()
                i = 1
                while i <= int(k):
                    punctC = generarePctRndValid(n, greutati, greutateGhiozdan)
                    print(punctC)
                    #print(greutati)
                    c=RHC(incercari, punctC, greutati, greutateGhiozdan)
                    #print("Calculat:")
                    print(c)
                    valoarea =detValoare(c,valori)
                    greutate= verificareGhiozdan(greutati,greutateGhiozdan,c)
                    writeInFile("RHC.txt", i, valoarea, greutate)
                    i= i+1

                lvalori, lgreutati = readValWeight(k, "RHC.txt")
                avg, maxim, calitate = detBestAvg(citireIstoric("RHC.txt"))
                lgrmaxime = detGreutateMaxima(maxim, lvalori, lgreutati)
                writeInFile("BestRHC.txt", j, maxim, lgrmaxime)

                writeBestAvg(maxim, avg, calitate, "RHC.txt")
                f=open("RHC.txt","a")
                f.write("Numarul de incercari maxim admise: " + incercari)
                f.close()
                j+=1
            print("--- %s seconds ---" % (time.time() - start_time))
        if x=="6":

            afisareSubmeniu()
            y=input("Introdu numarul pentru ce instanta doresti plotarea:")
            if y== "1":
                lvalori, lgreutati = readValWeight(k, "Istoric.txt")
            if y== "2":
                lvalori, lgreutati = readValWeight(k, "Istoric200.txt")
            if y== "3":
                lvalori, lgreutati = readValWeight(k, "RHC.txt")
            #lvalori,lgreutati=readValWeight(k,"RHC.txt")
            if y== "2" or y == "1":
                plt.title("Val. din " + numefis + " cu k= " + str(k) + " nr sol generate ")
            if y== "3":
                plt.title("Val. din "+numefis+" cu k= "+str(k)+" nr sol generate si incercari:" +str(incercari) )
            plt.scatter(lvalori,lgreutati, s=70, alpha=0.3)
            lgrmaxime=detGreutateMaxima(maxim,lvalori ,lgreutati)
            for i in lgrmaxime:
                plt.plot(maxim,i,"ro", label = "Valoare Maxima")
            #plt.plot(lvalori,lgreutati,"*")
            plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left', numpoints =1)
            plt.tight_layout()
            plt.ylabel('Greutatea')
            plt.xlabel('Valorile')
            plt.show()
        if x == "0":
            ok = False
    print("Programul s-a incheiat cu succes!")


principal()
