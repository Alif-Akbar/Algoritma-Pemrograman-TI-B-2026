#JAWABAN SOAL 3

print("Masukkan Nilaimu:")

nilai = input()

nilai_siswa = int(nilai)


if nilai_siswa > 60 :
    print("Kamu lulus,")
    if nilai_siswa > 75 :
        print("Kamu berhasil,")
        if nilai_siswa > 90 :
            print("Kamu telah menguasainya...")
        else :
            print("Pertahankan prestasimu...")             
    else :
        print("Tingkatkan lagi ya...") 
else :
    print("Maaf, kamu harus mengulanginya lagi...")
