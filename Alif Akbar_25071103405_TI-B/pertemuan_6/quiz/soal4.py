import soal1
import soal2
import soal3

baris = 1
kolom = 3

rekap_penjualan_tiket = [[0 for i in range(baris)] for j in range(kolom)]

class Film:
    def __init__(self, JudulFilm, HargaFilm):
        JudulFilm = self.JudulFilm
        HargaFilm = self.HargaFilm

    def tampilkan(self, JudulFilm, HargaFilm):
        print(JudulFilm, -  HargaFilm )