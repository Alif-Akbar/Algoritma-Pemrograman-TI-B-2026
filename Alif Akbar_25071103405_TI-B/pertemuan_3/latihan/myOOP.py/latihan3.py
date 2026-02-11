#ENCAPSULATION

class Mahasiswa:
    def __init__(self, nama, nilai):
        self.__nama = nama
        self.__nilai = nilai

    def get_nilai(self):
        return self.__nilai

    def set_nilai(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
        else:
            return "Nilai tidak valid"

Mahasiswa_a = Mahasiswa("Alif", 85)
print(Mahasiswa_a.get_nilai())