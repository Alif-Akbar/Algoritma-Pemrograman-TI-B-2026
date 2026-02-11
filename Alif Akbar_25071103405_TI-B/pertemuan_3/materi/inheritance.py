'''

Inheritance (Pewarisan) adalah konsep dalam pemrograman berorientasi objek (OOP)
di mana sebuah kelas (kelas turunan atau subclass) dapat mewarisi atribut dan metode
dari kelas lain (kelas induk atau superclass). Dengan inheritance, kita dapat
membuat hierarki kelas yang memungkinkan penggunaan kembali kode dan memperluas
fungsionalitas kelas yang sudah ada tanpa harus menulis ulang kode tersebut.

Class terbagi menjadi dua jenis, yaitu:
1. Kelas Induk (Parent Class/Superclass): Kelas yang menjadi dasar bagi kelas lain.
    Kelas ini menyediakan atribut dan metode yang dapat diwariskan ke kelas turunan.
2. Kelas Turunan (Child Class/Subclass): Kelas yang mewarisi atribut dan metode dari kelas induk.
    Kelas turunan dapat menambahkan atribut dan metode tambahan atau mengubah perilaku
    yang diwarisi dari kelas induk.

'''



class Person:
  def __init__(self, fname, lname, year):
    self.firstname = fname
    self.lastname = lname
    self.year = year

  def printname(self):
    print(self.firstname, self.lastname, self.year)

  def berjalan(self):
    print("Saya sedang berjalan kaki.")

  def tidur(self):
    print("Saya sedang tidur.")    

class Student(Person):
  def __init__(self, fname, lname, year, graduationyear):
    super().__init__(fname, lname, year) # Menggunakan super() untuk mengakses konstruktor kelas induk
    self.graduationyear = graduationyear

  def belajar(self):
    print("Saya sedang belajar agar lulus tepat waktu.")  

x = Student("Mike", "Olsen", 2020, 2024)
print(x.graduationyear) # Output: 2024

y = Person("John", "Doe", 1995)
y.belajar() # Akan menghasilkan error karena kelas Person tidak memiliki metode belajar()
y.tidur()  # Output: Saya sedang tidur.