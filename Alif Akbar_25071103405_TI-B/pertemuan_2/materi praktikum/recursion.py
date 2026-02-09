'''
recursion adalah sebuah teknik pemrograman di mana sebuah fungsi memanggil dirinya sendiri untuk menyelesaikan suatu masalah.
Fungsi rekursif biasanya memiliki dua bagian utama:
1. Base Case: Kondisi di mana fungsi berhenti memanggil dirinya sendiri untuk mencegah loop tak berujung.
2. Recursive Case: Bagian di mana fungsi memanggil dirinya sendiri dengan argumen yang dimodifikasi untuk mendekati base case.
'''


def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)


def factorial(n):
  # Base Case
  if n == 0 or n == 1:
    return 1
  # Recursive Case
  else:
    return n * factorial(n - 1)

print(factorial(5))
