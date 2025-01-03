# no solution by the deadline 
with open(r"assignment #1/med.txt", "r") as file:
    n = int(file.readline())  
    str_array = file.read().strip().split()
    array = []
    for item in str_array: array.append(int(item.strip())) 
    m = array.pop()

import random

def kth_smallest(A, n, k):
    def quickselect(A, low, high, k):
        if low == high:  
            return A[low]
        pivot_index = random.randint(low, high)
        pivot_value = A[pivot_index]
        A[pivot_index], A[high] = A[high], A[pivot_index]
        store_index = low
        for i in range(low, high):
            if A[i] < pivot_value:
                A[store_index], A[i] = A[i], A[store_index]
                store_index += 1
        A[store_index], A[high] = A[high], A[store_index]
        if k == store_index:
            return A[k]
        elif k < store_index:
            return quickselect(A, low, store_index - 1, k)
        else:
            return quickselect(A, store_index + 1, high, k)
    return quickselect(A, 0, n - 1, k - 1)

print(kth_smallest(array, n, m))