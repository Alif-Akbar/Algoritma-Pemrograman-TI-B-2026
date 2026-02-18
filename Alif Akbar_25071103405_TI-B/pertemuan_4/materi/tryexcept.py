'''Contoh penggunaan try-except untuk menangani error saat pembagian'''

try:
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    hasil = a / b
    print(f"Hasil pembagian: {hasil}")

except ValueError:
    print("Input tidak valid. Harap masukkan angka.")

except ZeroDivisionError:
    print("Error: Pembagian dengan nol tidak diperbolehkan.")
print("Program selesai.")


try:
    hasil = 10 / 0 
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")



try:
    umur = int(input("Masukkan umur Anda: "))
    print(f"Umur Anda adalah {umur}")
except ValueError: # menangani error jika input tidak bisa dikonversi ke integer
    print("Error: Input harus berupa angka valid!")










