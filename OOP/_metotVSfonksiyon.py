"""
metotlar classların içinde tanımlanır
fonskiyonlar ise classların dışında tanımlanır

"""

class Emp(object):

    age = 25
    salary = 1000
    
    #metotlar
    def ageSalaryRatio(self):
        a = self.age / self.salary
        print("metot: ", a)

e1 = Emp()
e1.ageSalaryRatio()

print()
# -----------------------------------------
#fonksiyonlar
def ageSalaryRatio(age, salary):
    a = age / salary
    print("fonksiyon: ", a)

ageSalaryRatio(30, 300)

print()
print("fonksiyon mini örnek")
pi = 3.14
r = 5
area = pi*r**2

def findArea(a, b):   # a = pi  ,b = r
    area = a*b**2
    print(area)
    return area

r1 = findArea(pi, r)   # 78.5

r2 = findArea(pi, 10)  # 314.0

print(r1 + r2)