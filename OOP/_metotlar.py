"""
Self: Burdaki selfin anlamı şu:
Ben bir obje oluşturdum ve bir de metot oluşturdum
o selfi kullanarak bu metotdun içinde objeme ait yani classıma ait 
variable'leri kullanmak istiyorsun.
"""

class Square(object):

    edge = 5  # metre

    def area(self):
        area = self.edge * self.edge   # 5 * 5
        print(area)

s1 = Square()

print(s1)
print(s1.edge)
print(s1.area())
