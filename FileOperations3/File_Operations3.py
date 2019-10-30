with open("şiir.txt","r",encoding="utf-8") as file :
    liste=[]
    liste2=[]
    liste3=[]
    for i in file:
        liste.append(i)
    for i in range(0,len(liste)):
        if i<7:
            liste2.append(liste[i][0:1])
        else:
            liste3.append(liste[i][0:1])
    isim=""
    for i in range(0,len(liste2)):
        isim+=liste2[i]
    isim+=" "
    for i in range(0,len(liste3)):
        isim+=liste3[i]
    print(isim)