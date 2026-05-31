'''
Insertion Sort adalah algoritma pengurutan yang bekerja dengan membagi daftar menjadi dua bagian: bagian yang sudah diurutkan dan bagian yang belum diurutkan. Algoritma ini secara iteratif mengambil elemen dari bagian yang belum diurutkan dan menyisipkannya ke posisi yang benar dalam bagian yang sudah diurutkan. Proses ini diulang hingga seluruh daftar terurut.
Langkah-langkah Insertion Sort:
1. Mulai dari elemen kedua (indeks 1) hingga akhir daftar, lakukan langkah berikut:
   a. Simpan elemen saat ini (current_value) yang akan disisipkan.
    b. Bandingkan current_value dengan elemen-elemen sebelumnya dalam bagian yang sudah diurutkan.
    c. Geser elemen-elemen yang lebih besar dari current_value ke kanan untuk membuat ruang bagi current_value.
    d. Setelah menemukan posisi yang benar untuk current_value, sisipkan current_value ke posisi tersebut.
2. Ulangi langkah 1 hingga seluruh daftar terurut.
'''


mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist) # menghitung panjang list

for i in range(1,n): # loop untuk mengiterasi elemen dari indeks 1 sampai n-1
  insert_index = i # menyimpan indeks saat ini untuk penyisipan
  current_value = mylist[i] # menyimpan nilai saat ini untuk dibandingkan dengan elemen sebelumnya
  for j in range(i-1, -1, -1): # loop untuk membandingkan elemen saat ini dengan elemen sebelumnya, dimulai dari indeks i-1 hingga 0
     if mylist[j] > current_value: # jika elemen sebelumnya lebih besar dari nilai saat ini, geser elemen tersebut ke kanan
       mylist[j+1] = mylist[j] # geser elemen ke kanan
       insert_index = j # update indeks penyisipan ke posisi sebelumnya
     else: # jika elemen sebelumnya tidak lebih besar dari nilai saat ini, maka posisi yang benar untuk nilai saat ini telah ditemukan
       break # keluar dari loop karena posisi yang benar telah ditemukan
  mylist[insert_index] = current_value # sisipkan nilai saat ini ke posisi yang benar setelah semua elemen yang lebih besar telah digeser ke kanan

print(mylist)
