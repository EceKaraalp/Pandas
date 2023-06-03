# Calisan.py
from Insan import Insan
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk) #insan sınıfının özelliklerini kalıtım yoluyla aldı
        #sektor, tecrube ve maas değişkenleri tanımlandı
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

    # Tüm değişkenler get/set metotları ile tanımlandı
    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hesabi(self):
        try:
            if self.__tecrube < 24:
                return 0
            elif 24 <= self.__tecrube <= 48 and self.__maas < 15000: #tecrube değeri 24 ve 48 arasında ve maaş 15000 altındaysa maaşın tecrübe ile bölümünden kalan ile maaşı topla
                return (self.__maas % self.__tecrube) + self.get_maas()
            elif self.__tecrube > 48 and self.__maas < 25000: #tecrube değeri 48'den büyükse ve maaş 25000 altındaysa maaşın tecrübeye bölümünden kalanın yarısı ile maaşı topla
                return (self.__maas % self.__tecrube) / 2 + self.get_maas()
            else:
                return self.__maas
        except Exception as hata:
            print(f"Bir hata oluştu: {str(hata)}") #hata varsa hata mesajı yazdırılır

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrübe: {self.__tecrube}\nMaaş: {self.get_maas()}\nYeni Maaş: {self.zam_hesabi()}\n"
