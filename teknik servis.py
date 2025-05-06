import datetime


class ServisKayitlari:
    def __init__(self):
        self.kayıtlar = []

    def kayit_ekle(self):
        isim = input("müşteri ismi: ")
        telefon = input("telefon numarası: ")
        cihaz = input("cihaz türü: ")
        marka = input("marka\model: ")
        ariza = input("arıza türü: ")
        tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        yeni_kayit = {
            "isim": isim,
            "telefon": telefon,
            "cihaz": cihaz,
            "marka_model": marka,
            "ariza": ariza,
            "tarih": tarih,
            "durum": "Kayıt Alındı"
        }
        self.kayıtlar.append(yeni_kayit)
        print("kayıt başarıyla alındı.")

    def kayitlari_listele(self):
        if not self.kayıtlar:
            print("hiç kayıt bulunamadı.")
        else:
            print("servis kayıtları:")
            for kayit in self.kayıtlar:
                print(kayit)

    def durum_guncelle(self):
        print("--- Durum Güncelle ---")
        if not self.kayitlar:
            print("Hiç kayıt yok.")
            return

        self.kayitlari_listele()
        try:
            sec = int(input("Güncellemek istediğiniz kaydın numarası: ")) - 1
            if 0 <= sec < len(self.kayitlar):
                yeni_durum = input("Yeni Durum (örnek: Tamir Edildi, Teslim Edildi): ")
                self.kayitlar[sec]["durum"] = yeni_durum
                print("Durum güncellendi.")
            else:
                print("Geçersiz seçim.")
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    def menu(self):
        while True:
            print("=== Teknik Servis Programı ===")
            print("1. Yeni Kayıt Ekle")
            print("2. Kayıtları Listele")
            print("3. Durum Güncelle")
            print("4. Çıkış")

            secim = input("Seçiminiz: ")

            if secim == "1":
                self.kayit_ekle()
            elif secim == "2":
                self.kayitlari_listele()
            elif secim == "3":
                self.durum_guncelle()
            elif secim == "4":
                print("Çıkılıyor...")
                break
            else:
                print("Geçersiz seçim. Tekrar deneyin.")


# Programı başlat
if __name__ == "__main__":
    uygulama = ServisKayitlari()
    uygulama.menu()