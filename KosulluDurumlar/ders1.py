print(""""**************************
Hesap Makinesi Programı
      
İşlemler;

1. Toplma İşlemi

2. Çıkarama İşlemi

3. Çarma İşlemi

4. Bölme İşlemi

**************************
""")

a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))

işlem = input("İşlemi giriniz (1/2/3/4) : ")

if işlem == "1":
    print("{} ile {} in toplamı {} dir.".format(a,b,a+b))

elif işlem == "2":
    print("{} ile {} in çıkarımı {} dir.".format(a,b,a-b))

elif işlem == "3":
    print("{} ile {} in çarpımı {} dir.".format(a,b,a*b))

elif işlem == "4":
    print("{} ile {} in bölümü {} dir.".format(a,b,a/b))

else:
    print("Geçersiz işlem...")