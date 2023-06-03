# BeyazYaka.py
from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    # Tüm değişkenler get/set metotları ile tanımlandı
    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hesabi(self):
        try:
            if self.get_tecrube() < 24:
                return self.get_tesvik_primi()
            elif 24 <= self.get_tecrube() <= 48 and self.get_maas() < 15000:#tecrube değeri 24 ve 48 arasında ve maaş 15000 altındaysa maaşın tecrübe ile bölümünden kalanın 5 katı, teşvik primi ile maaşı topla
                return ((self.get_maas() % self.get_tecrube()) * 5) + self.get_tesvik_primi() + self.get_maas()
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:#tecrube değeri 48'den büyükse ve maaş 25000 altındaysa maaşın tecrübeye bölümünden kalanın 4 katı, teşvik primi ile maaşı topla
                return ((self.get_maas() % self.get_tecrube()) * 4) + self.get_tesvik_primi() + self.get_maas()
            else:
                return self.get_maas()
        except Exception as hata:
            print(f"Bir hata oluştu: {str(hata)}") #hata varsa hata mesajı yazdırılır

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.get_tecrube()}\nMaaş: {self.get_maas()}\nYeni Maaş: {self.zam_hesabi()}\n"
