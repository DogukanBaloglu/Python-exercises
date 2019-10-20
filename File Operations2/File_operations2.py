def listele(liste):
    liste=liste[:-1]    #satır sonundaki \n i kaldırmak işlemi
    liste=liste.split(",")
    return liste
#Dosyada yazanları alıp her satırı parçalayan fonksiyon
#------------------------------------------------------

with open("karışık.txt","r",encoding="utf-8") as file:
    liste=[]
    for i in file :
        liste.append(listele(i))
#Dosyadan verileri okurken fonksiyon ile birlikte satır listeye atanır.
#----------------------------------------------------------------------

file1=open("Galatasaray.txt","w",encoding="utf-8")
file2=open("Fenerbahçe.txt","w",encoding="utf-8")
file3=open("Beşiktaş.txt","w",encoding="utf-8")
for i in liste:
    if i[1] == "Galatasaray":
        file1.write("{}\n".format(i))
    elif i[1] == "Fenerbahçe":
        file2.write("{}\n".format(i))
    else:
        file3.write("{}\n".format(i))
file1.close()
file2.close()
file3.close()
#listeye atanmış olan değerlerin takımlara göre sınıflandırılması
#----------------------------------------------------------------