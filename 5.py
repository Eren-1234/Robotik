class Ogrenci:

    def __init__(self,id,ad,soyad,sinif,yas,cinsiyet):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.sinif = sinif
        self.yas = yas
        self.cinsiyet = cinsiyet
    
    def Kayit(self):
        with open("kayit.txt","a",encoding="utf-8") as file:
            file.write("İd: "+self.id+" Ad: "+self.ad+" Soyad: "+self.soyad+" Sinif: "+self.sinif+" Yas: "+self.yas+" Cinsiyet: "+self.cinsiyet+"\n")


    def OgrenciSorgulama(id_soru):
        with open("kayit.txt","r",encoding="utf-8") as file:
            lines = file.readlines()
            file.seek(0)
            for line in range(len(lines)):
                if lines[line].count(id_soru) == 1 :
                    print(lines[line])
                

    def OgrenciSilme(id_soru):
        with open("kayit.txt","r+",encoding="utf-8") as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if line.count(id_soru) == 1 :
                    continue
                file.write(line)
            file.truncate()


while True:

    soru = input("Kayit olmak için 1, Ogrenci bilgileri sorgulama icin 2, Ogrenci silme icin 3, cikis icin 0 a basiniz:  ")
    
    if soru == "1":
        id = input("id giriniz: ")
        ad = input("ad giriniz: ")
        soyad = input("soyad giriniz: ")
        sinif = input("sinif giriniz: ")
        yas = input("yas giriniz: ")
        cinsiyet = input("cinsiyet giriniz => erkek = True , kiz = False: ")
        ogrenci = Ogrenci(id,ad,soyad,sinif,yas,cinsiyet)
        ogrenci.Kayit()
        continue

    if soru == "2":
        id_soru = input("Ogrenci bilgileri sorgulama icin ogrencinin id numarasini giriniz: ")
        Ogrenci.OgrenciSorgulama(id_soru)
    
    if soru == "3":
        id_soru = input("Silmek istediginiz ogrencinin id numarasini giriniz: ")
        Ogrenci.OgrenciSilme(id_soru)
        
    if soru == "0":
        print("İşleminiz bitmiştir.")
        break


