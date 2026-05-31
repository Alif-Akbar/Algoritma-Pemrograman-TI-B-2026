list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = len(list)

i_count = 0
j_count = 0
count = 0
swap = False

for i in range (n-1):
    i_count += 1
    for j in range (n-i-1):
        j_count += 1
        if list[j] > list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
            count += 1
            swap = True
    if not swap:
        break

print(f"i loop : {i_count}")
print(f"j loop : {j_count}")
print(f" : {count}")
print(list)