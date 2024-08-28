print("""***************************
Atm Makinesine Hoşgeldiniz.
      
İşlemler;
      
      1 - Bakiye sorgulama

      2 - Para Yatırma

      3 - Para Çekme

Programdan çıkmak için ''q' ya basın.
*************************************
""")

bakiye  = 1000

while True:
    islem = input("İşlem seçiniz: ")

    if (islem == "q"):
        print("Yine bekleriz.")
        break

    elif (islem == "1"):
        print("Bakiyeniz {} TL dir.".format(bakiye))

    elif (islem == "2"):
        miktar = int(input("Miktarı giriniz: "))
        bakiye += miktar

    elif (islem == "3"):
        miktar = int(input("Miktarı giriniz: "))

        if (bakiye - miktar < 0):
            print("Böyle bir miktar çekemezsiniz...")
            continue
        bakiye -= miktar
        
    else:
        print("Geçersiz işlme...")