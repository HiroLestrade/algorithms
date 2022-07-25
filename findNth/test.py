from findNth import findNth

arr = [10,5,7,9,1,2,8,4,6,3]
len = len(arr)
nth = int((len/2 - 1, len/2)[len%2 != 0]) #índiceBuscado #media

findNth(arr, len, nth)

print(arr)
print(arr[nth])