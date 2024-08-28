"""
2. Kontrol Yapıları
Soru:
Python'da if, elif, else ifadelerini nasıl kullanırsınız? Bu yapıları kullanarak bir sayı pozitif, negatif veya sıfır olup olmadığını kontrol eden bir kod yazabilir misiniz?
Görev:
1 ile 100 arasındaki tüm tek sayıları listeleyen bir döngü yazın.
"""

# a = 5

# if a > 0:
#     print("a pozitiftir.")
# elif a == 0:
#     print("a sıfırdır")
# else:
#     print("a negatifitr.")


# for i in range(1, 101):
#     if i % 2!= 0:
#         print(i)

# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)


toplam = 0
sayac = 1

while sayac < 10:
    toplam += sayac
    sayac += 1

print(toplam)