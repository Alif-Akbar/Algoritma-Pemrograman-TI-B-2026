'''
Array adalah struktur data yang digunakan untuk menyimpan beberapa nilai dalam satu variabel.
Array memungkinkan kita untuk mengelompokkan data yang berhubungan sehingga memudahkan pengelolaan dan manipulasi data tersebut.
Di Python, array dapat diimplementasikan menggunakan list atau modul array.
'''

cars = ["Ford", "Volvo", "BMW"]
cars.append("Audi")
cars.remove("Volvo")

x = cars[0]
y = len(cars)

print(x)
print(y)


for x in cars:
  print(x)

