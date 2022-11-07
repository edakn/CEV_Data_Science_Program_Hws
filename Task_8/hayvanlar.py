# -*- coding: utf-8 -*-

class Hayvanlar():
    def __init__(self, isim,tur, boy, kilo, beslenmesekli):
        self.isim = isim
        self.tur=tur
        self.boy = boy
        self.kilo=kilo
        self.beslenmesekli = beslenmesekli
def info_hayvanlar(self):
        print("Canlıların bilgileri...")
        print("İsim : {}\nTür: {}\nBoy: {}\n Kilo:  {}\nBeslenme şekli: {}\n".format(self.isim,self.tur, self.boy, self.kilo,self.beslenmesekli))


class Dinozorlar(Hayvanlar):
    def __init__(self, isim,tur, boy, kilo, beslenmesekli):
        super().__init__(isim,tur,boy,kilo,beslenmesekli)
        self.sinif=sinif

    def __str__(self):
        return "İsim : {}\nTür: {}\nBoy:  {}\n Kilo:  {}\nBeslenme şekli:  {}\nSınıf:{}".format(self.isim,self.tur, self.boy,self.kilo, self.beslenmesekli,self.sinif)


class Kuslar(Hayvanlar):
    def __init__(self, isim,tur, boy, kilo, beslenmesekli):
        super().__init__(self, isim,tur, boy, kilo, beslenmesekli)
        self.hiz = hiz
        self.cinsiyet=cinsiyet
    
    def __str__(self):
        return "İsim : {}\nTür: {}\nBoy:  {}\n Kilo:  {}\nBeslenme şekli:  {}\nHız:  {}\nCinsiyet:  {}".format(self.isim,self.tur, self.boy, self.kilo,self.beslenmesekli,self.hiz,self.cinsiyet)

class Baliklar(Hayvanlar):
   def __init__(self, isim,tur, boy, kilo, beslenmesekli):
        super().__init__(self, isim,tur, boy, kilo, beslenmesekli)
        self.familya =familya

   def __str__(self):
        return "İsim : {}\nTür: {}\nBoy:  {}\n Kilo:  {}\nBeslenme şekli:  {}\nFamilya: ".format(self.isim,self.tur, self.boy,self.kilo,self.beslenmesekli,self.familya)



Massospondylus= Dinozorlar("Alisha","Massospondylus",6,1000,"Otçul","	Saurischia")
Massospondylus.info_hayvanlar()

Muhabbet=Kuslar("Limon","M. undulatus",0.18,0.040,"Otçul","32 km/h","Erkek")
Muhabbet.info_hayvanlar()

Levrek=Baliklar("Uşak","D. labrax",5,6.6,"Deniz Canlıları","Moronidae")
Levrek.info_hayvanlar()