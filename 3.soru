import random as r  # Bunu Quick Sort ta kullandım

liste = [4,1,67,8,2,43,54,12]

def Selection_Sort(liste):
    for i in range(len(liste)):
        deger = liste[i]
        indis = i
        for j in range(i+1,len(liste)):
            if deger > liste[j]:
                deger = liste[j]
                indis = j
        flag = liste[i]
        liste[i] = liste[indis]
        liste[indis] = flag
    print(liste)

def Bubble_Sort(liste):
    for i in range(len(liste)):
        for j in range(len(liste) - i -1):
            if liste[j] > liste[j+1]:
                flag = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = flag
    print(liste)

def İnsertion_Sort(liste):
    for i in range(1,len(liste)):
        j = i-1
        deger = liste[i]
        while j >= 0 and deger < liste[j]:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = deger
    print(liste)
        
def Merge_Sort(liste):
    if len(liste) > 1:
        orta = len(liste) // 2
        sol = liste[:orta]
        sag = liste[orta:]
        Merge_Sort(sol)
        Merge_Sort(sag)

        i = 0
        j = 0
        k = 0
        
        while i < len(sol) and j < len(sag):
            if sol[i] <= sag[j]:
              liste[k] = sol[i]
              i += 1
            else:
                liste[k] = sag[j]
                j += 1
            k += 1

        while i < len(sol):
            liste[k] = sol[i]
            i += 1
            k += 1

        while j < len(sag):
            liste[k]=sag[j]
            j += 1
            k += 1

def Quick_Sort(liste):
    pivot = r.choice(liste)
    sol = []
    sag = []
    
    for i in range(len(liste)):
        if liste[i] == pivot:
            continue
        if pivot < liste[i]:
            sag.append(liste[i])
        if liste[i] < pivot:
            sol.append(liste[i])
        sol.sort()
        sag.sort()
    sol.append(pivot)
    liste = sol + sag
    print(liste)
