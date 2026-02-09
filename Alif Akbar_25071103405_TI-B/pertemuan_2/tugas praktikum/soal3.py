# menghitung jumlah seluruh digit dalam sebuah bilangan bulat positif

n = input("Masukkan sebuah bilangan bulat positif: ")

def hitung_jumlah_digit(angka):
    total = 0
    for digit in str(angka):
        total += int(digit)
    return total

jumlah_digit = hitung_jumlah_digit(n)
print("Jumlah seluruh digit dalam bilangan", n, "adalah:", jumlah_digit)