# menghitung pangkat dari sebuah bilangan bulat positif

n = input("Masukkan sebuah bilangan bulat positif: ")
p = input("Masukkan pangkat yang diinginkan: ")

def hitung_pangkat(angka, pangkat):
    hasil = 1
    for _ in range(int(pangkat)):
        hasil *= int(angka)
    return hasil

hasil_pangkat = hitung_pangkat(n, p)
print(n, "pangkat", p, "adalah:", hasil_pangkat)