def toplam(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def carpma(a,b):
    return a*b

def bolme(a,b):
    return a/b

def mod(a,b):
    return a%b

def usalma(a,b):
    return a**b

while True:
    secim = input("Bir seçim yapınız: ")
    if secim == "q":
        exit()

    a = int(input("a sayısı: "))
    b = int(input("b sayısı: "))

    if secim=="1":
        print("Sonuç :", toplam(a, b))
    elif secim =="2":
        print("Sonuç :", cikarma(a,b))
    elif secim =="3":
        print("Sonuc :",carpma(a,b))
    elif secim=="4":
        print("Sonuç :",bolme(a,b))
    else:
        print("Yanlış seçim lütfen tekrar deneyin")
        exit()