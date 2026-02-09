# menghitung rata-rata nilai mahasiswa dari sebuah daftar nilai

nilai_mahasiswa = [80, 75, 90, 60, 85]

def hitung_rata_rata(nilai):
    total = sum(nilai)
    jumlah = len(nilai)
    rata_rata = total / jumlah
    return rata_rata

rata_rata_nilai = hitung_rata_rata(nilai_mahasiswa)
print("Rata-rata nilai mahasiswa adalah:", rata_rata_nilai)



