# menentukan apakah sebuah bilangan adalah bilangan prima atau bukan di dalam rentang tertentu

n = input("Masukkan sebuah bilangan bulat positif: ")

for num in range(1, int(n)):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, "adalah bilangan prima")