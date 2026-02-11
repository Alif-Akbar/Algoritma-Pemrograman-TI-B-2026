#INHERITANCE!

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info_produk(self, name, price, guarantee, expire_date):
        return f"Nama Produk: {name}, Harga: {price}" 

class Electronic(Product):
    def __init__(self, name, price, guarantee):
        super().__init__(name, price)
        self.guarantee = guarantee

    def info_produk(self, name, price, guarantee):
        return f"Nama Produk: {name}, Harga: {price}, Garansi: {guarantee}"
        

class FnB(Product):
    def __init__(self, name, price, expire_date):
        super().__init__(name, price)
        self.expire_date = expire_date

    def info_produk(self, name, price, expire_date):
        return f"Nama Produk: {name}, Harga: {price}, Expire Date: {expire_date}"

a = Electronic("TV", "3.000.000" , "2 tahun")
b = FnB("Roti", "15.000" , "12-12-2026")

a.info_produk(a.name, a.price, a.guarantee)
b.info_produk(b.name, b.price, b.expire_date)






