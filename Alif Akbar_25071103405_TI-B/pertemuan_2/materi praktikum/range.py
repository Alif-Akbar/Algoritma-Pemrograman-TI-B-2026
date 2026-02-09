'''
Range adalah fungsi bawaan Python yang digunakan untuk menghasilkan urutan bilangan bulat.
Fungsi ini sering digunakan dalam loop untuk mengulangi sejumlah iterasi tertentu.
Fungsi range() dapat dipanggil dengan satu, dua, atau tiga argumen:
1. range(stop): Menghasilkan bilangan bulat dari 0 hingga stop-1.
2. range(start, stop): Menghasilkan bilangan bulat dari start hingga stop-1
3. range(start, stop, step): Menghasilkan bilangan bulat dari start hingga stop-1 dengan increment sebesar step.
'''

for i in range(5):
  print(i)

for i in range(2, 6):
  print(i)

for i in range(1, 10, 2):
  print(i)