"""
3. Fonksiyonlar
Soru:
Python'da bir fonksiyon nasıl tanımlanır ve bu fonksiyon nasıl çağrılır? Parametreli ve parametresiz fonksiyonlar arasındaki fark nedir?
Görev:
Bir sayının faktöriyelini hesaplayan bir fonksiyon yaz.
"""

"""
Fonksiyon Tanımlama ve Çağırma
Fonksiyon Tanımlama: Python'da bir fonksiyon def anahtar kelimesi ile tanımlanır. Fonksiyon adı ve parametreler parantez içinde yazılır, ardından iki nokta (:) koyularak fonksiyon bloğuna geçilir.

def fonksiyon_adı(parametreler):
    # Fonksiyonun gövdesi
    pass
"""

def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)
    
print(faktoriyel(5))