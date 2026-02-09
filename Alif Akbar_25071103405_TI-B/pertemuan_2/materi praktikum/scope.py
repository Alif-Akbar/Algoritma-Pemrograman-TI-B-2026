'''
Scope adalah area dimana sebuah variabel dapat diakses atau dikenali dalam program.
Ada beberapa jenis scope dalam Python:
1. Local Scope: Variabel yang didefinisikan di dalam sebuah fungsi hanya dapat diakses di dalam fungsi tersebut.
2. Global Scope: Variabel yang didefinisikan di luar semua fungsi dapat diakses di mana saja dalam file tersebut.
'''

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()