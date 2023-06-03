# MaviYaka.py
from Calisan import Calisan
class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas) #Calisan sınıfının özelliklerini kalıtım yoluyla aldı
        self.__yipranma_payi = yipranma_payi

    # Tüm değişkenler get/set metotları ile tanımlandı
    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hesabi(self):
        try:
            if self.get_tecrube() < 24:
                return self.__yipranma_payi * 10
            elif 24 <= self.get_tecrube() <= 48 and self.get_maas() < 15000:#tecrube değeri 24 ve 48 arasında ve maaş 15000 altındaysa maaşın tecrübe ile bölümünden kalanın yarısı, yıpranma payının 10 katı ile maaşı topla
                return (self.get_maas() % self.get_tecrube()) / 2 + (self.__yipranma_payi * 10) + self.get_maas()
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:#tecrube değeri 48'den büyükse ve maaş 25000 altındaysa maaşın tecrübeye bölümünden kalanın üçte biri, yıpranma payının 10 katı ile maaşı topla
                return (self.get_maas() % self.get_tecrube()) / 3 + (self.__yipranma_payi * 10) + self.get_maas()
            else:
                return self.get_maas()
        except Exception as hata:
            print(f"Bir hata oluştu: {str(hata)}") #hata varsa hata mesajı yazdırılır

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()}\nMaaş: {self.get_maas()}\nYeni Maaş: {self.zam_hesabi()}\n"
