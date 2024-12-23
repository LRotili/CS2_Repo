# no solution by the deadline 
array = []
with open(r"assignment #1/hea.txt", "r") as file:
    n = file.readline()
    array_str = file.read().split(" ")
    for numb in array_str: array.append(int(numb))

def heapify(A, n, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and A[left] > A[largest]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)

def build_max_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

def permute_to_max_heap(array):
    build_max_heap(array)
    return array

results = permute_to_max_heap(array)
print(" ".join(map(str, results)))

with open("assignment #1/hea_output.txt", 'w') as file:
    file.write(" ".join(map(str, results)))

