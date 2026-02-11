'''

Polymorphism adalah konsep dalam pemrograman berorientasi objek yang memungkinkan
objek dari kelas yang berbeda untuk diakses melalui antarmuka yang sama. Dengan
polymorphism, metode yang sama dapat berperilaku berbeda pada kelas yang berbeda.
Contohnya, metode "move" dapat diimplementasikan dalam berbagai kelas seperti
"Car", "Boat", dan "Plane", di mana setiap kelas memiliki cara berbeda untuk
mengimplementasikan metode tersebut sesuai dengan karakteristiknya masing-masing.

'''

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()  #Output: #Drive!
                     #Sail!
                     #Fly!
            

            