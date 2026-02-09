
# booleans menunjukkan tipe data boolean di python dan cara penggunaannya

#static typing = nilainya tetap
#dinamic typing = nilainya berubah-ubah

print(10 > 5)
print(11 == 9)
print(10 == 10)
print(10 < 7)

a = 93
b = 93

if b > a:
  print("b lebih besar dari a")
if b == a:
  print("b sama dengan a")
else:
  print("b lebih kecil dari a")

  
#ada nilai, tak ada perbandingan = nilainya selalu TRUE 
print(bool("Hello"))
print(bool(15))