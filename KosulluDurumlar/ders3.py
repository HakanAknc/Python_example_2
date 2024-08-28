# Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.

a = int(input("a : ")) 
b = int(input("b : "))
c = int(input("c : "))

if a>b and a>c:
    print("a büyüktür")
elif b>a and b>a:
    print("b büyüktür")
else:
    print("c büyüktür")