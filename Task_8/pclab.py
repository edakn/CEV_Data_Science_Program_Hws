# -*- coding: utf-8 -*-

import time

class Pclab():
    def __init__(self, lab_isim="Anroid Lab", lab_durum="Açık", kayitli_ogrenciler=["1","2","5","19","11"], kayitli_ogrenci_sayisi=5, bos_bilgisayar_sayisi=15, dolu_bilgisayar_sayisi=5):
        self.lab_isim = lab_isim
        self.lab_durum=lab_durum
        self.kayitli_ogrenciler = kayitli_ogrenciler
        self.kayitli_ogrenci_sayisi = kayitli_ogrenci_sayisi
        self.bos_bilgisayar_sayisi = bos_bilgisayar_sayisi
        self.dolu_bilgisayar_sayisi = dolu_bilgisayar_sayisi

    def bilgiler(self):
        print("Lab Adı: {}\nDurum: {}\nKayıtlı Öğrenciler: {}\nKayıtlı Öğrenci Sayısı: {}\nBoş Bilgisayar Sayısı: {}\nDolu Bilgisayar Sayısı: {}".format(self.lab_isim,self.lab_durum,self.kayitli_ogrenciler,self.kayitli_ogrenci_sayisi,self.bos_bilgisayar_sayisi,self.dolu_bilgisayar_sayisi))




class Asistan(Pclab):
    def lab_ac(self):
        if (self.lab_durum == "Kapalı"):
            self.lab_durum = "Açık"
            print("Laboratuvar açılıyor...")
        else:
            print("Laboratuvar zaten açık.")
    
    def lab_kapa(self):
        if (self.lab_durum == "Açık"):
            self.lab_durum = "Kapalı"
            print("Laboratuvar kapanıyor...")
        else:
            print("Laboratuvar zaten kapalı.")
    
    def ogrenci_ekle(self, ogrenci_no):
        if ogrenci_no in self.kayitli_ogrenciler:
            print("Öğrenci zaten kayıtlı.")
        else:
            print("Öğrenci ekleniyor...")
            time.sleep(1)
            self.kayitli_ogrenciler.append(ogrenci_no)
            self.kayitli_ogrenci_sayisi += 1
            print("Öğrenci kaydedildi.")
            print("Öğrenci listesi: {}".format(self.kayitli_ogrenciler))

    def ogrenci_listele(self):
        print(self.kayitli_ogrenciler)



class Ogrenci(Pclab):
    def bilgisayar_doldur(self):
        if (self.bos_bilgisayar_sayisi > 0):
            print("Masaya oturuluyor..")
            time.sleep(1)
            self.bos_bilgisayar_sayisi -= 1
            self.dolu_bilgisayar_sayisi += 1
        else:
            print("Laboratuvarda boş bilgisayar bulunmamaktadır.")

    def bilgisayar_boşalt(self):
        print("Masadan kalkılıyor..")
        time.sleep(1)
        self.bos_bilgisayar_sayisi -= 1
        self.dolu_bilgisayar_sayisi += 1
        print("Laboratuvarda boş bilgisayar bulunmaktadır.")


lab=Pclab()
ogrenci=Ogrenci(Pclab)
asistan=Asistan(Pclab)

while True:
    secim = input("Lütfen kişi seçimini yapınız.\n 1-Asistan\n\n2-Öğrenci \n")
    if (secim == "1"):

        print("""
            1.Öğrenci ekle
            2.Öğrenci listele
            3.Bilgileri göster
            4.Laboratuvar'ı Aç.
            5.Laboratuvar'ı Kapa.
            6.Çıkış
            
            """)

        islem1 = input("Hoşgeldiniz lütfen yapacağınız işlem için seçim yapınız: ")

        if islem1 == "1":
            ogrenci_no = input("Öğrenci numarasını giriniz.")
            asistan.ogrenci_ekle(ogrenci_no)
        elif islem1 == "2":
            asistan.ogrenci_listele()
        elif islem1 == "3":
            lab.bilgiler()
        elif islem1 == "4":
            asistan.lab_ac()
            print("Laboratuvar açıldı.")
        elif islem1 == "5":
            asistan.lab_kapa()
            print("Laboratuvar kapatıldı.")
        elif islem1== "6":
          break
        else:
            print("Geçersiz işlem seçtiniz.")

    elif (secim == "2"):
        print("""
        1.Bir bilgisayar masasına otur.
        2.Bir bilgisayar masasından kalk.
        3.Bilgileri göster
        4.Çıkış
        """)
        islem2 = input("Hoşgeldiniz lütfen yapacağınız işlem için seçim yapınız: ")
        if islem2 == "1":
            ogrenci.bilgisayar_doldur()
        elif islem2 == "2":
            ogrenci.bilgisayar_bosalt()
        elif islem2 == "3":
            ogrenci.bilgiler()
        elif islem2 == "4":
            break
        else:
            print("Geçersiz işlem seçtiniz.")