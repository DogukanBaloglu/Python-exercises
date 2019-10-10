class developer():

    def __init__(self,name,surname,number,salary,ability):
        self.name = name
        self.surname = surname
        self.number =number
        self.salary = salary
        self.ability = ability
    def showinfo(self):
        print("""
        Name: {}
        Surname: {}
        Number: {}
        Salary: {}
        Ability: {}  
        """.format(self.name,self.surname,self.number,self.salary,self.ability))

    def addability(self):
        ablty=input("Yeni beceri girişi yapın:")
        self.ability.append(ablty)
        print("Adding ability...")

    def plussalary(self):
        plus=int(input("Ne kadar zam yapılacak:"))
        self.salary+=plus
        print("Salary is increasing...")

dogukan =developer("Dogukan","Baloglu",5379583850,7500,["Python","C","HTML","CSS"])
dogukan.showinfo()

while(1):
    x = int(input("""Yapmak istediğiniz işlem numarasını seçin:
        1.Bilgi Görüntüleme 
        2.Yetenek ekleme
        3.Zam işlemi
        4.Çıkış   
        :
        """))
    if(x==4):
        print("Programdan çıkılıyor...")
        print("Bilgilerin güncellenmiş hali:")
        break
    elif(x==1):
        dogukan.showinfo()
    elif(x==2):
        dogukan.addability()
    elif(x==3):
        dogukan.plussalary()
    else:
        print("Hatalı Giriş Yaptınız ")

dogukan.showinfo()

