

jum_bil = int(input("Masukkan jumlah bilangan dalam array: "))
n = 0
arr_bil = []

while n < jum_bil :
    bil = int(input(f"Masukkan angka yang ingin diurutkan: "))
    n += 1
    while bil <= 0 :
        n -= 1
        del bil
        raise IndexError("Tidak bisa memasukan angka negatif..")
    arr_bil.append(bil)

print("Array sebelum diurutkan:", arr_bil)


def radixSort(arr):
    radixArray = [[], [], [], [], [], [], [], [], [], []]
    maxVal = max(arr)
    exp = 1

    while maxVal // exp > 0:

        while len(arr) > 0:
            val = arr.pop()
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        for bucket in radixArray:
            while len(bucket) > 0:
                val = bucket.pop()
                arr.append(val)

        exp *= 10
    return arr

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

def mergeSort(arr):
  step = 1 # Starting with sub-arrays of length 1
  length = len(arr)

  while step < length:
    for i in range(0, length, 2 * step):
      left = arr[i:i + step]
      right = arr[i + step:i + 2 * step]

      merged = merge(left, right)

      # Place the merged array back into the original array
      for j, val in enumerate(merged):
        arr[i + j] = val

    step *= 2 # Double the sub-array length for the next iteration

  return arr



radixsorted = radixSort(arr_bil)
mergesorted = mergeSort(arr_bil)

print("Radix sort:", radixsorted)
print("Merge sort:", mergesorted)
