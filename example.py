import time
class pc ():
    def __init__ (self,model,renk,ram,storage,disk_type,app,sayı):
        self.model=model
        self.renk=renk
        self.ram= ram
        self.storage=storage
        self.disk_type=disk_type
        self.app=app
        self.sayı=sayı
    def ram_update(self):
        x=input("Yeni ram GB değerini girin:")
        print("RAM için geçerli değerler güncelleniyor...")
        time.sleep(1)
        self.ram=x
        print("RAM güncellendi, Yeni ram:",self.ram)
    def new_app(self):
        x=input("Yüklenecek uygulamanın ismini girin:")
        self.app.append(x)
    def storage_update(self):
        x=int(input("Hafızaya ne kadar daha ekleme yapılacak?"))
        print("Ekleme işlemi gerçekleştiriliyor...")
        time.sleep(1)
        self.storage += x
        print("Güncel hafıza:",self.storage)
    def __str__(self):
         return "Model:{}\nRenk:{}\nRAM:{}\nStorage:{}\nDisk Türü:{}\nUygulamalar{}|\nUygulama Sayısı:{}".format(self.model,self.renk,self.ram,self.storage,self.disk_type,self.app,self.sayı)
    def __len__(self):
        return self.sayı

x=input("Bilgisayarınızın modelini girin:")
y=input("Bilgisayarınızın rengini girin:")
z=int(input("Bilgisayarınızın takılı RAM değerini girin:"))
q=int(input("Bilgisayarınızın kaç GB depolama alanı olduğunu girin:"))
w=input("Bilgisayarınızda takılı olan disk tipini  girin:")
e=list(input("Bilgisayarınızın Uygulamaları girin girin:"))
r=len(e)

pc1=pc(x,y,z,q,w,e,r)

print(pc1)
print(len(pc1))
pc.ram_update(pc1)
pc.storage_update(pc1)
pc.new_app(pc1)
print("Güncel Hal:",pc1)