"""
# Python'da bir değişken nasıl tanımlanır?
a = 1
b = "hakan"
c = 3.5

# Python'da sık kullanılan temel veri tiplerini (int, float, string, list, dict) kısaca açıklayabilir misin?
int = tam sayıları tanımlamak için
float = küsüratlı sayıları tanımlamka için
string = metin tnımlamak için kullanılır
list = liste tanımlamka için kullanılır
dict = sözlüktür key value mantığı ile çalışır
"""

test = [3, 1, 4, 1, 5, 9]

test.sort()

max_value = max(test)
min_value = min(test)

print("Sıralı liste", test)
print("En büyük değer", max_value)
print("En küçük değer", min_value)

"""
# Python'da max() ve min() fonksiyonları nasıl çalışır? 

max() = oluşturulan diziyi kontrol eder en büyük değeri ekrana yazdırır
min() = oluşturulan diziyi kontrol eder en küçük değeri ekrana yazdırır
"""

# Hangi veri tipleri ile kullanılabilir?

# Liste ile kullanım
numbers = [10, 20, 30, 40]
print(max(numbers))  # 40
print(min(numbers))  # 10

# Demet ile kullanım
tuple_numbers = (5, 15, 25, 35)
print(max(tuple_numbers))  # 35
print(min(tuple_numbers))  # 5

# Küme ile kullanım
number_set = {8, 6, 7, 5}
print(max(number_set))  # 8
print(min(number_set))  # 5

# String ile kullanım
text = "python"
print(max(text))  # 'y' (Unicode değeri en yüksek olan karakter)
print(min(text))  # 'h' (Unicode değeri en düşük olan karakter)

