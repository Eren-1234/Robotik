def Faktoriyal(sayi):

    if sayi<0:
        sayi = sayi*(-1)
        Faktoriyal(sayi)
        
    elif sayi>0:
        result = sayi**0.5
        print(result)
    
sayi = int(input("Karekökü alinacak sayiyi giriniz: "))
Faktoriyal(sayi)


# Mutlak değerini alacak şekilde yaptım mesela -9 un karekökü 3 oluyo recursive kullanmak için böyle yaptım