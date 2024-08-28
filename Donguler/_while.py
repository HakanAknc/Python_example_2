# sayi = 0

# while sayi < 10:
#     #sayi = sayi + 1
#     print(sayi)
#     sayi = sayi +1

"""Harf notu Hesaplama Programı"""

while True:

    vize = int(input("Vize notu : "))
    final = int(input("Final notu : "))
    ortalama = (vize * 0.4) + (final * 0.6)

    if (ortalama >= 85):
        print("Harf notunuz: AA")
    elif (ortalama >= 70 and ortalama < 85):
        print("Harf notunuz : BA")
    elif (ortalama >= 60 and ortalama < 70):

        print("Harf notunuz : BB")

    elif (ortalama >= 45 and ortalama < 60):

        print("Harf notunuz : CB")

    elif (ortalama >= 0 and ortalama < 45):

        print("Harf notunuz : FF")