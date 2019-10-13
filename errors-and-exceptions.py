def rakamlar(x):
    for i in x:
        list1=[]
        try:
            a=int(i)
            list1.append(i)
            print(list1)
        except(ValueError):
            print("Bu karakter dizisi int forma çevrilemez:'{}'".format(i))

liste = ["345","sadas","324a","14","kemal"]
rakamlar(liste)
