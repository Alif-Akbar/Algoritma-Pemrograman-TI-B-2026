def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

data = [59, 40, 36, 40, 30, 26, 97, 8, 23, 31, 2, 40, 99, 70, 64, 36, 43, 20, 1, 9]
angka = input(f"Masukkan angka yang ingin dicari: ")

linear = linearSearch(data, angka)
binary = binarySearch(data, angka)

if angka != -1:
   print("Found at index", result)
else:
   print("Not found")
   return -1

print("Linear search: ", linear)
print("Binary Search: ", binary)






