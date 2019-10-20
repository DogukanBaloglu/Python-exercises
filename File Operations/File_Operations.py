def nothesapla(notlar):
    a=notlar.split(",")
    isim=a[0]
    not1 = int(a[1])
    not2 = int(a[2])
    not3 = int(a[3])
    ortalama=not1*0.3+not2*0.3+not3*0.4
    return (isim) , (ortalama)
# Öğrencinin not ortalamasını hesaplayan fonksiyon
#-------------------------------------------------

def Pass(liste,liste2):
    file=open("Geçenler.txt","w",encoding="utf-8")
    file.write("GEÇENLER\n\n")
    for i in liste:
        file.write("{}------>{}\n".format(i[0],i[1]))
    file.write("\n")
    file.write("DERSİ GEÇENMESİNE RAĞMEN TEKRAR ALABİLECKLER\n\n")
    for i in liste2:
        file.write("{}------>{}\n".format(i[0],i[1]))
    file.close()
#Geçen öğrencileri ve şartlı geçen öğrencileri dosya ya yazan fonksiyon
#----------------------------------------------------------------------

def again(liste):
    file=open("Kalanlar.txt","w",encoding="utf-8")
    file.write("DERSİ TEKRAR ALACAKLAR\n\n")
    for i in liste:
        file.write("{}------>{}\n".format(i[0],i[1]))
    file.close()
#Kalan öğrencileri dosyaya yazan fonksiyon
#-----------------------------------------

file=open("dosya.txt","r",encoding="utf-8")
liste1=[]
for i in file :
    liste1.append(nothesapla(i))
file.close()
#Dosya içerisinden bilgiler alınıp liste1'in içine atanması
#----------------------------------------------------------

liste_pass = []
liste_optional = []
liste_again = []
for i in range(0, len(liste1)):
    if liste1[i][1] >= 90:
        liste_pass.append(liste1[i])
    elif liste1[i][1] >= 85:
        liste_pass.append(liste1[i])
    elif liste1[i][1] >= 80:
        liste_pass.append(liste1[i])
    elif liste1[i][1] >= 75:
        liste_pass.append(liste1[i])
    elif liste1[i][1] >= 70:
        liste_pass.append(liste1[i])
    elif liste1[i][1] >= 65:
        liste_pass.append(liste1[i])
    elif liste1[i][1] >= 50:
        liste_optional.append(liste1[i])
    else:
        liste_again.append(liste1[i])
#geçenlerin  ve kalanların  belirlenerek listelerin içine atanaması
#------------------------------------------------------------------

Pass(liste_pass,liste_optional)
again(liste_again)
#Geçen ve kalanların dosyaya yazma işlemi için gerekli fonksiyona yönlendirilmesi
#--------------------------------------------------------------------------------