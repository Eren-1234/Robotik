# üçgen noktalarının koordinatlarını kullanıcı belirlesin 
x1= float(input("1. nokta koordinatlarini giriniz x1: "))
y1 = float(input("1. nokta koordinatlarini giriniz y1: "))
x2= float(input("2. nokta koordinatlarini giriniz x2: "))
y2 = float(input("2. nokta koordinatlarini giriniz y2: "))
x3= float(input("3. nokta koordinatlarini giriniz x3: "))
y3 = float(input("3. nokta koordinatlarini giriniz y3: "))

px = float(input("Aranmak istenen 1. nokta koordinatlarini giriniz x: "))
py = float(input("Aranmak istenen 2. nokta koordinatlarini giriniz y: "))

bx = x2 - x1
by = y2 - y1
cx = x3 - x1
cy = y3 - y1

x = px - x1
y = py - y1

d = bx*cy - cx*by

wa = (x*(by-cy)+y*(cx-bx)+bx*cy-cx*by)/d
wb = (x*cy-y*cx)/d
wc = (y*bx-x*by)/d

if (wa>=0 and wa<=1) and (wb>=0 and wb<=1) and (wc>=0 and wc<=1) == True:
    print(True)
    
else:
    print(False)