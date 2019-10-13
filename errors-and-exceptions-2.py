def ciftmi(x):
    if (x%2==0):
        print("Girmiş olduğunuz {} sayısı çift sayıdır.".format(x))
    else:
        raise ValueError("Girilen sayı çift sayı değilidir.")

def start():
    try:
        a = int(input("Bir  sayı girişi yapınız:"))
    except(ValueError):
        print("Yaptığınız giriş sadece rakamlardan oluşmalı....")
        return  start()
    ciftmi(a)
while True:
    start()