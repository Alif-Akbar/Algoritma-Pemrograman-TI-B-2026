# Iterator adalah sebuah objek yang dapat diiterasi, artinya kita dapat melintasi elemen-elemennya satu per satu.
# Iterator biasanya digunakan dalam loop seperti for loop untuk mengakses setiap elemen dalam koleksi data seperti list, tuple, atau string.

my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
for item in my_iterator:
    print(item) # Output: 1 2 3 4 5