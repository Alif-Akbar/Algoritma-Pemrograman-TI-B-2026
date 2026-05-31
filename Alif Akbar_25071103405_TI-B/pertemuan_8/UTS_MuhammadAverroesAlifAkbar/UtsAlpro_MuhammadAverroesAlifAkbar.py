'''

Game tebak angka berbasis terminal. Program menyimpan sekumpulan angka dalam
sebuah list yang sudah ditentukan. Pada setiap ronde, satu angka diambil sebagai angka
rahasia. Pemain diminta menebak angka tersebut dan akan mendapat petunjuk:
• "Terlalu kecil" — jika tebakan lebih kecil dari angka rahasia
• "Terlalu besar" — jika tebakan lebih besar dari angka rahasia
• "Benar!" — jika tebakan tepat
Skor pemain dihitung berdasarkan sisa percobaan saat berhasil menebak. Seluruh riwayat
permainan disimpan dalam matrix 2D dan ditampilkan sebagai leaderboard di akhir sesi.

'''

import random

DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]

nama = input(print("Siapa Namamu?"))
pilihan = input(print(f"Halo {nama}, Tekan 1 untuk bermain..."))

def tebak_angka():
    nomor_ronde = input(print("Masukkan angka dari 1 - 10"))
    angka_rahasia = DAFTAR_ANGKA[nomor_ronde]
    maks_percobaan = 7
    berhasil = False
    n = int(print("Silahkan Tebak Angkanya..."))
    while maks_percobaan >= 0 :
        if n > angka_rahasia :
            print("Terlalu Besar.")
            sisa_percobaan = maks_percobaan - 1
        if n < angka_rahasia :
            print("Terlalu Kecil.")
            sisa_percobaan = maks_percobaan - 1
        if n is angka_rahasia :
            print("Benar!")
            berhasil = True
            sisa_percobaan = maks_percobaan
    return hitung_skor        

def hitung_skor(berhasil, sisa_percobaan):
    skor = sisa_percobaan * 10
    if berhasil in tebak_angka is True :
        print(f"Selamat, kamu berhasil. Skormu adalah {skor}")
    else:
        print(f"Maaf, kamu gagal. Skormu adalah {skor}")
    return tampilkan_leaderboard

def tampilkan_leaderboard():
    histori = [nama, hitung_skor]
    print(histori)

if pilihan is 1 :
    print(tebak_angka)
else:
    print("Terima Kasih...")


