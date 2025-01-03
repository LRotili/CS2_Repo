array = []
keys = []

with open(r"assignment #1/bins.txt", "r") as file:
    n = int(file.readline())  
    m = int(file.readline())  
    str_array = file.read().strip().split()
    for numb in range(n):
        array.append(int(str_array[numb].strip())) 
    for numb in range(n, n + m):
        keys.append(int(str_array[numb].strip()))

result = []
for key in keys:
    left, right = 0, len(array) - 1
    found = False
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == key:
            result.append(mid + 1)
            found = True
            break
        elif array[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    if not found:
        result.append(-1)

with open("assignment #1/bins_output.txt", 'w') as file:
    file.write(" ".join(map(str, result)))
