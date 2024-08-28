print("""***********
Hesap Makinesi Programı

      İşlemler

      1.Toplama İşlemi
      2.Çıkarma İşlemi
      3.Çarpma İşlemi
      4.Bölme İşlemi

*******************
""")

sayi1 = int(input("1. Sayıyı giriniz: "))
sayi2 = int(input("2. Sayıyı giriniz: "))

islem = input("İşlem giriniz: ")

if islem == "1":
    print("{} ile {} toplamı {} dir.".format(sayi1,sayi2,sayi1+sayi2))
elif islem == "2":
    print("{} ile {} in Farkı {} dir".format(sayi1, sayi2, sayi1 - sayi2))

elif     islem == "3":
            print("{} ile {} in çarpımı {} dir".format(sayi1, sayi2, sayi1 * sayi2))

elif islem == "4":
                print("{} ile {} in bölümü {} dir".format(sayi1, sayi2, sayi1 / sayi2))
else:
    print("***Geçersiz İşlem***")
