import random
import time

class kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses="0",kanal_listesi=["TRT"],kanal="TRT"):
        self.tv_durum= tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal

    def tv_ac(self):
        if(self.tv_durum =="Açık"):
            print("TV açık")
        else:
            print("TV açılıyor..")
            self.tv_durum= "Açık"
    def tv_kapat(self):
        if(self.tv_durum =="Kapalı"):
            print("TV Kapalı")
        else:
            print("TV kapatılıyor...")
            self.tv_durum="Kapalı"

    def ses_ayarları(self):
        while True:
            x = input("Sesi azalt:'<'\n Sesi arttır:'>'\n Çıkış:q")
            if(x== "<"):
                if(self.tv_ses != 0):
                    self.tv_ses-=1
                    print("Ses:{}".format(self.tv_ses))
                else:
                    print("Ses:0")

            elif(x==">"):
                if(self.tv_ses !=100):
                    self.tv_ses+=1
                    print("Ses:",self.tv_ses)
                else:
                    print("Ses:100")
            else:
                print("Ses Güncellendi",self.tv_ses)
                break

    def kanal_ekle(self,kanak_ismi):
        print("kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanak_ismi)
        print("Kanal eklendi")

    def rastgele(self):
        y=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal =self.kanal_listesi[y]
        print("Şu anki kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "TV durumu{}\nTV ses:{}\nKanal Listesi:{}\nŞu anki kanal:{}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

kumanda1=kumanda()

print("""
KUMANDA

1.TV Aç
2.TV Kapat
3.Ses Ayarları
4.Kanal Ekle
5.Kanal Sayısı Öğren
6.Rastgele Kanal
7.TV Bilgileri

Çıkmak için 'e' ye basın.
""")
while True:
    işlem=input("İşlem seçiniz:")
    if(işlem=="e"):
        print("Kumanda kapatılıyor...")
        break
    elif(işlem=="1"):
        kumanda.tv_ac()
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif(işlem=="3"):
        kumanda.ses_ayarları()
    elif(işlem=="4"):
        kanal_islemleri=input("Kanal isimlerini ',' ile ayırarak girin:")
        kanal_listesi=kanal_islemleri.split(",")
        for i in kanal_listesi:
            kumanda.kanal_ekle(i)
    elif(işlem=="5"):
        print("Kanal Sayısı:",len(kumanda))
    elif(işlem=="6"):
        kumanda.rastgele()
    elif(işlem=="7"):
        print(kumanda)
    else:
        print("Hatalı giriş yaptınız.")
