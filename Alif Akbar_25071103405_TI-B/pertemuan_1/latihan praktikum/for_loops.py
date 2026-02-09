
# for_loops.py menunjukkan penggunaan perulangan for di python

# Contoh penggunaan for dengan range
for count in range(5):
    print("Count is:", count)
print("Perulangan selesai!")

# Contoh penggunaan for dengan list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)
print("Daftar buah selesai!")

# Contoh penggunaan for dengan string
word = "hello"
for letter in word:
    print("Letter:", letter)
print("Perulangan huruf selesai!")

# Contoh penggunaan for dengan dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(f"{key}: {person[key]}")
print("Informasi orang selesai!")