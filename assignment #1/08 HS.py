# no solution by the deadline 

array = []
with open(r"assignment #1/hs.txt", "r") as file:
    n = file.readline()
    array_str = file.read().split(" ")
    for numb in array_str: array.append(int(numb))

def heapify(A, n, i):
    largest = i 
    left = 2 * i + 1  
    right = 2 * i + 2 
    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  
        heapify(A, n, largest)  

def heap_sort(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)
    return A

with open("assignment #1/hs_output.txt", 'w') as file:
    file.write(" ".join(map(str, heap_sort(array))))


