
# while_loops.py menunjukkan penggunaan perulangan while di python

count = 0
while count < 5:
    print("Count is:", count)
    count += 1
print("Perulangan selesai!")

# Contoh penggunaan while dengan kondisi kompleks
number = 10
while number > 0:
    print("Number is:", number)
    number -= 2
print("Countdown selesai!")

# Contoh penggunaan while dengan break dan continue
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # Lewati angka genap
    if i > 7:
        break  # Hentikan perulangan jika i lebih dari 7
    print("Odd number:", i)