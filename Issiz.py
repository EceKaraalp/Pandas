# Issiz.py
from Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk) #insan sınıfının özelliklerini kalıtım yoluyla aldı
        self.__tecrube = tecrube #tecrube değişkeni private olarak tanımlandı

    #Tüm değişkenler get/set metotları ile tanımlandı
    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def statu_bul(self):
        #satatüleri ve etki eden değerlerini içeren sözlük oluşturuldu.
        statuler = {
            "mavi yaka": 0.2,
            "beyaz yaka": 0.35,
            "yönetici": 0.45
        }
        #en yüksek değer bulunur
        max_deger = max(statuler.values())
        #en yüksek değere sahip statü bulunur.
        en_uygun_statu = [statu for statu, etki in statuler.items() if etki == max_deger]
        return en_uygun_statu[0]

    def __str__(self):
        return super().__str__() + f"Tecrübe: {self.__tecrube}\n"
