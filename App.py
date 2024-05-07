import random



def tas_kagit_makas():
    kullanici_skor = 0
    bilgisayar_skor = 0
    
    for _ in range(3):  # Kullanıcıyı 3 kez oynat
        # Kullanıcıdan seçim al
        kullanici_secim = input("Taş mı (t), Kağıt mı (k), Makas mı (m)? ").lower()
        
        # Bilgisayarın seçimini belirle
        bilgisayar_secim = random.choice(['t', 'k', 'm'])
        
        # Seçimleri ekrana yazdır
        print("Sen:", kullanici_secim)
        print("Bilgisayar:", bilgisayar_secim)
        
        # Kazananı belirle
        if kullanici_secim == bilgisayar_secim:
            print("Berabere!")
        elif (kullanici_secim == 't' and bilgisayar_secim == 'm') or \
             (kullanici_secim == 'k' and bilgisayar_secim == 't') or \
             (kullanici_secim == 'm' and bilgisayar_secim == 'k'):
            print("Kazandın!")
            kullanici_skor += 1
        else:
            print("Kaybettin!")
            bilgisayar_skor += 1
    
    # Sonuçları yazdır
    if kullanici_skor > bilgisayar_skor:
        print("Oyun bitti. Kazandın! Senin skorun:", kullanici_skor, "Bilgisayarın skoru:", bilgisayar_skor)
    elif kullanici_skor < bilgisayar_skor:
        print("Oyun bitti. Kaybettin! Senin skorun:", kullanici_skor, "Bilgisayarın skoru:", bilgisayar_skor)
    else:
        print("Oyun bitti. Berabere! Senin skorun:", kullanici_skor, "Bilgisayarın skoru:", bilgisayar_skor)

# Oyunu başlat
tas_kagit_makas()