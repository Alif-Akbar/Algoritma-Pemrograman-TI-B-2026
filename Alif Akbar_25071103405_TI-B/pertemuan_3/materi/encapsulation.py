'''

Encapsulation adalah salah satu prinsip utama dalam pemrograman berorientasi objek (OOP) 
yang mengacu pada pengelompokan data (atribut) dan metode (fungsi) yang beroperasi pada 
data tersebut dalam satu unit, yaitu kelas. Encapsulation juga menyembunyikan detail 
implementasi dari pengguna kelas, sehingga hanya metode publik yang dapat diakses oleh pengguna.
Dalam Python, encapsulation dapat dicapai dengan menggunakan atribut dan metode yang 
bersifat "private (dengan awalan underscore `_`) atau protected (dengan awalan dua underscore `__`)."

Dalam Python, tidak ada konsep private yang benar-benar tersembunyi seperti dalam bahasa lain, 
tetapi dengan menggunakan konvensi penamaan, kita dapat memberikan indikasi bahwa suatu atribut 
atau metode seharusnya tidak diakses secara langsung dari luar kelas.

'''

class Person:
  def __init__(self, fname, lname, year):
    self.firstname = fname
    self.lastname = lname
    self._year = year  # Atribut protected

  def greet(self):
    print("Hello, my name is " + self.firstname + " " + self.lastname)  

  def get_year(self):
    print("Age:", self._year)  # Metode publik untuk mengakses atribut protected

  def setYear(self, newYear):
    self._year = newYear
    if self._year < 0:
        print("Year cannot be negative.")
    if self._year > 150:
        print("Year seems unrealistic.")
    else:
        print("Year set to:", self._year)       


p1 = Person("John", "Doe", 20)
p1.greet()  # Output: Hello, my name is John Doe
# print(p1._year)  # Akan menghasilkan error karena _year adalah atribut private
p1.get_year()  # Output: Age: 20
p1.setYear(21)  # Output: Year updated to: 21
p1.get_year()  # Output: Age: 21

'''

Name Mangling adalah teknik yang digunakan Python untuk mengubah nama atribut
atau metode yang diawali dengan dua underscore (`__`) menjadi nama yang unik.
Dengan name mangling, atribut atau metode tersebut tidak dapat diakses langsung
dari luar kelas, sehingga memberikan tingkat perlindungan tambahan terhadap
akses tidak sah.

'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age)  # Not recommended!
# Output: 30