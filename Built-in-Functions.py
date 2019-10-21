###--------------------Kenarları verilen dikdörtgenlerin, map fonksiyonu kullanarak  alan hesabı---------------------###
def alan_hesapla(x):
    return x[0]*x[1]

liste=list(map(alan_hesapla,[(3,4),(10,3),(7,8),(1,9),(7,6),(3,2)]))
print(liste)
#----------------------------------------------------------------------------------------------------------------------#

###--------------------Kenarları verilen dikdörtgenlerin, map fonksiyonu kullanarak  alan hesabı---------------------###
#YOL 2
liste1=([(3,4),(10,5),(5,6),(1,9),(7,6),(3,2),(13,1)])
liste2=list(map(lambda x : x[0]*x[1],liste1))
print(liste2)
#----------------------------------------------------------------------------------------------------------------------#


###----------Kenar değerleri verilen  üçgenlerin , üçgen belirtip belirtmediğini filter fonsiyonu ile bulma----------###
def ucgen_kontrol(x):
    if (x[0]+x[1]>x[2] & abs(x[0]-x[1])<x[2]) != True:
        return False
    elif (x[0]+x[2]>x[1] & abs(x[1]-x[2])<x[1]) != True:
        return False
    elif  (x[2]+x[1]>x[0] & abs(x[2]-x[1])<x[0]) != True:
        return False
    else:
        return True

liste3=[(3,4,5),(6,8,10),(3,10,7),(12,2,14),(7,14,6),(5,12,13)]
liste4=list(filter(ucgen_kontrol,liste3))
print(liste4)
#----------------------------------------------------------------------------------------------------------------------#


###----Listedeki sayılardan çift olanları filter fonksiyonuyla bulup çift sayılar toplamını reduce ile elde etme-----###
from functools import reduce
liste5=[1,2,3,4,5,6,7,8,9,10]
liste6=list(filter(lambda x : x%2==0, liste5 ))
toplam=reduce(lambda x,y : x+y , liste6)
print(toplam)
#----------------------------------------------------------------------------------------------------------------------#


###-----İsim ve soyisimleri iki ayrı listede verilen kişilerin , tam adlarını zip fonksiyonu kullanarak yazdırma-----###
isimler=["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler=["Gelmez","Öztürk","Altın","Yıldırım","Dikmen","Kaya","Polat"]

liste7=list(zip(isimler,soyisimler))
for i in liste7:
   print("İsim: {} , Soyisim: {}".format(i[0],i[1]))
#----------------------------------------------------------------------------------------------------------------------#