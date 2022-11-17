def fact(x):
    if x==1:
        return 1
    else:
        y = x*fact(x-1)
        return y
x = int(input("Faktoriyali alinacak sayiyi giriniz: "))
print(fact(x))


