list_film_1 = ["Danur", 50000 ]
list_film_2 = ["Inside Out 2", 45000 ]
list_film_3 = ["Drak System", 20000]

list_film = [list_film_1, list_film_2, list_film_3]
print(list_film)

pilih_nomor = int(input("Masukkan Film yang ingin dipilih: "))

def pilihpilih(pilih_nomor):
    if pilih_nomor == 1 :
        print(list_film_1)
    if pilih_nomor == 1 :
        print(list_film_2)
    if pilih_nomor == 1 :
        print(list_film_3)


def pilihfilm(pilih_nomor):
    if pilih_nomor == 1 :
        print("Film yang kamu ingin beli:")
        return list_film_1
    if pilih_nomor == 2 :
        print("Film yang kamu ingin beli:")
        return list_film_2
    if pilih_nomor == 2 :
        print("Film yang kamu ingin beli:")
        return list_film_3
    else:
        print("Error...")

pilihfilm()    














