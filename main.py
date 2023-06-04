#main.py
import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

try:
    # İnsan sınıfı için 2 nesne oluşturdu ve bilgileri ekrana yazdırdı.
    print("İnsan sınıfı:\n")
    insan1 = Insan("15197302863", "Ebrar", "Koyulmuş", 24, "Kadın", "Türk")
    insan2 = Insan("98814432108", "Mehmet", "Demir", 49, "Erkek", "Türk")
    print(insan1)
    print(insan2)

    # İşsiz sınıfı için 3 nesne oluşturdu ve bilgileri ekrana yazdırdı.
    print("İşsiz sınıfı:\n")
    issiz1 = Issiz("58396281034", "Hanife", "Karaca", 43, "Kadın", "Türk", "Bilgisayar Mühendisi")
    issiz2 = Issiz("24601627893", "H.Hüseyin", "Öztürk", 28, "Erkek", "Türk", "Mimar")
    issiz3 = Issiz("63849865899", "Zeynep", "Yıldız", 32, "Kadın", "Türk", "Hemşire")
    print(issiz1)
    print(issiz2)
    print(issiz3)

    # Çalışan sınıfı için 3 nesne oluşturdu ve bilgileri ekrana yazdırdı.
    print("Çalışan sınıfı:\n")
    calisan1 = Calisan("84720990202", "Zeliha", "Durmuş", 40, "Kadın", "Türk", "Turizm", 60, 9000)
    calisan2 = Calisan("93846518923", "Miray", "Maviay", 28, "Kadın", "Türk", "Sağlık", 36, 12000)
    calisan3 = Calisan("45678909876", "Kamil", "Yılmaz", 35, "Erkek", "Türk", "Muhasebe", 84, 10000)
    print(calisan1)
    print(calisan2)
    print(calisan3)

    # Mavi yaka sınıfı için 3 nesne oluşturdu ve bilgileri ekrana yazdırdı.
    print("Mavi yaka sınıfı:\n")
    maviyaka1 = MaviYaka("56492749271", "Fatma", "Sarı", 29, "Kadın", "Türk", "Üretim", 24, 8000, 0.2)
    maviyaka2 = MaviYaka("92747683924", "Faruk", "Çakır", 31, "Erkek", "Türk", "Pazarlama", 48, 14000, 0.5)
    maviyaka3 = MaviYaka("26910638927", "Şükran", "Gürsoy", 27, "Kadın", "Türk", "Eğitim", 72, 9500, 0.3)
    print(maviyaka1)
    print(maviyaka2)
    print(maviyaka3)

    # Beyaz yaka sınıfı için 3 nesne oluşturdu ve bilgileri ekrana yazdırdı.
    print("Beyaz yaka sınıfı:\n")
    beyazyaka1 = BeyazYaka("97659202314", "Hakan", "Koca", 33, "Erkek", "Türk", "Mühendislik", 24, 15000, 500)
    beyazyaka2 = BeyazYaka("87620924920", "Beyza", "Er", 30, "Kadın", "Türk", "Sağlık", 60, 18000, 2500)
    beyazyaka3 = BeyazYaka("13456765498", "Senanur", "İlkay", 35, "Kadın", "Türk", "Finans", 96, 22000, 1000)
    print(beyazyaka1)
    print(beyazyaka2)
    print(beyazyaka3)
    
    # Çalışan, mavi yaka ve beyaz yaka nesnelerinin tüm değerlerini içeren bir DataFrame oluşturuldu.
    data = {
        "Nesne Türü": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka",
                       "Beyaz Yaka", "Beyaz Yaka"],
        "TC No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), maviyaka1.get_tc_no(),
                  maviyaka2.get_tc_no(), maviyaka3.get_tc_no(), beyazyaka1.get_tc_no(), beyazyaka2.get_tc_no(),
                  beyazyaka3.get_tc_no()],
        "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), maviyaka1.get_ad(), maviyaka2.get_ad(),
               maviyaka3.get_ad(), beyazyaka1.get_ad(), beyazyaka2.get_ad(), beyazyaka3.get_ad()],
        "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), maviyaka1.get_soyad(),
                  maviyaka2.get_soyad(), maviyaka3.get_soyad(), beyazyaka1.get_soyad(), beyazyaka2.get_soyad(),
                  beyazyaka3.get_soyad()],
        "Yaş": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), maviyaka1.get_yas(),
                maviyaka2.get_yas(), maviyaka3.get_yas(), beyazyaka1.get_yas(), beyazyaka2.get_yas(),
                beyazyaka3.get_yas()],
        "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(),
                     maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(),
                     beyazyaka1.get_cinsiyet(), beyazyaka2.get_cinsiyet(), beyazyaka3.get_cinsiyet()],
        "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), maviyaka1.get_uyruk(),
                  maviyaka2.get_uyruk(), maviyaka3.get_uyruk(), beyazyaka1.get_uyruk(), beyazyaka2.get_uyruk(),
                  beyazyaka3.get_uyruk()],
        "Sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), maviyaka1.get_sektor(),
                   maviyaka2.get_sektor(), maviyaka3.get_sektor(), beyazyaka1.get_sektor(), beyazyaka2.get_sektor(),
                   beyazyaka3.get_sektor()],
        "Tecrübe": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(), maviyaka1.get_tecrube(),
                    maviyaka2.get_tecrube(), maviyaka3.get_tecrube(), beyazyaka1.get_tecrube(),
                    beyazyaka2.get_tecrube(), beyazyaka3.get_tecrube()],
        "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), maviyaka1.get_maas(),
                 maviyaka2.get_maas(), maviyaka3.get_maas(), beyazyaka1.get_maas(), beyazyaka2.get_maas(),
                 beyazyaka3.get_maas()],
        "Yıpranma Payı": [0, 0, 0, maviyaka1.get_yipranma_payi(), maviyaka2.get_yipranma_payi(),
                          maviyaka3.get_yipranma_payi(), 0, 0, 0],
        "Teşvik Prim": [0, 0, 0, 0, 0, 0, beyazyaka1.get_tesvik_primi(), beyazyaka2.get_tesvik_primi(),
                        beyazyaka3.get_tesvik_primi()],
        "Yeni Maaş": [calisan1.zam_hesabi(), calisan2.zam_hesabi(), calisan3.zam_hesabi(), maviyaka1.zam_hesabi(),
                      maviyaka2.zam_hesabi(), maviyaka3.zam_hesabi(),beyazyaka1.zam_hesabi(), beyazyaka2.zam_hesabi(),
                      beyazyaka3.zam_hesabi()]
    }
    df = pd.DataFrame(data)

    # Bazı değişken değerleri diğer nesneler için boş ise 0 atandı.
    df.fillna(0)

    gruplandir = df.groupby("Nesne Türü")

    ort_tecrube = gruplandir["Tecrübe"].mean()
    ort_yeni_maas = gruplandir["Yeni Maaş"].mean()
    print("Ortalama tecrübe değerleri: ")
    print(ort_tecrube)
    print()
    print("Ortalama yeni maaş değerleri: ")
    print(ort_yeni_maas)
    print()

    # Maaşı 15000 TL üzerinde olan kişilerin sayısı
    maas_15k_ustu = df[df["Maaş"] > 15000]
    maas_15k_sayisi = len(maas_15k_ustu)
    print("Maaşı 15000 TL üzeri kişi sayısı:", maas_15k_sayisi)
    print()

    # Yeni maaşa göre DataFrame'i küçükten büyüğe sırala ve yazdır
    df_sirali = df.sort_values(by="Yeni Maaş")
    print("Yeni Maaşa Göre Sıralanmış DataFrame:")
    print(df_sirali)
    print()

    # Tecrübesi 3 seneden fazla olan Beyaz yakalıları bul ve yazdır
    beyazyaka_tecrube_3 = df[(df["Nesne Türü"] == "Beyaz Yaka") & (df["Tecrübe"] > 3)]
    print("Tecrübesi 3 Seneden Fazla Olan Beyaz Yakalılar:")
    print(beyazyaka_tecrube_3)
    print()

    # Yeni maaşı 10000 TL üzerinde olanlar için 2-5 satır arası olanları seç ve tc_no ve yeni_maaş sütunlarını göster
    yeni_maas_10k_ustu = df[df["Yeni Maaş"] > 10000]
    yeni_maas_10k_ustu_secili = yeni_maas_10k_ustu.iloc[2:5, [1, -1]]
    print("Yeni Maaşı 10000 TL üzerinde olan 2-5 Satır Arası Veriler:")
    print(yeni_maas_10k_ustu_secili)
    print()

    # Ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame oluştur ve yazdır
    yeni_df = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]
    print("Yeni DataFrame:")
    print(yeni_df)

except Exception as hata:
    print("Hata:", str(hata))
