import random

def tas_kagit_makas_KADER_TUGBA_YARAMİS():

    print("Taş, Kağıt, Makas Oyununa Hoşgeldiniz!")
    print("Kurallar: Taş makası yener, makas kağıdı yener ve kağıt taşı yener.")
    print("Üst üste iki tur kazanan oyuncu yener. ")
    print("Her turda Taş, Kağıt veya Makas seçebilirsiniz. Oyunun sonunda size bitirmek isteyip istemediğiniz sorulacaktır.")
    
    toplam_oyun_sayisi = 0
    secenekler = ["taş", "kağıt", "makas"]

    while True:
        toplam_oyun_sayisi += 1
        
        print(f"\nOyun: {toplam_oyun_sayisi}")
        oyuncu_skoru = 0
        bilgisayar_skoru = 0
        turlar = 0

        while oyuncu_skoru < 2 and bilgisayar_skoru < 2:
            turlar += 1
            print(f"\nTur {turlar}:")
            
            oyuncu_secimi = ""
            while oyuncu_secimi not in secenekler:
                oyuncu_secimi = input("Taş, Kağıt, veya Makas seçin: ").lower()
                if oyuncu_secimi not in secenekler:
                    print("Geçersiz! Lütfen tekrar deneyin.")
            
            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
            
            if oyuncu_secimi == bilgisayar_secimi:
                print("Beraberlik!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş"):
                print("Oyuncuya 1 puan!")
                oyuncu_skoru += 1
            else:
                print("Bilgisayara 1 puan!")
                bilgisayar_skoru += 1
            
            print(f"Oyuncu Skoru: {oyuncu_skoru}, Bilgisayar Skoru: {bilgisayar_skoru}")

        if oyuncu_skoru == 2:
            print("Tebrikler, oyunu kazandınız!")
        else:
            print("Bilgisayar oyunu kazandı. Şansını tekrar dene!")

        devam_et_oyuncu = input("Yeni bir oyun oynamak ister misiniz? (evet/hayır): ").lower()
        
        devam_et_bilgisayar = random.choice(["evet", "hayır"])
        
        if devam_et_oyuncu == "evet" and devam_et_bilgisayar == "evet":
            print("iki oyuncuda devam etmeye karar verdi. Yeni oyun başlasın!")
        else:
            if devam_et_oyuncu == "hayır":
                print("Kullanıcı oyuna devam etmek istemiyor.")
            if devam_et_bilgisayar == "hayır":
                print("Bilgisayar oyuna devam etmek istemiyor.")
            print(f"Toplam {toplam_oyun_sayisi} oyun oynandı. Tekrar görüşmek üzere!")
            break

tas_kagit_makas_KADER_TUGBA_YARAMİS()
