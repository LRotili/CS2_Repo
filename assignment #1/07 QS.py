# no solution by the deadline 
with open(r"assignment #1/qs.txt", "r") as file:
    _ = int(file.readline()) 
    str_array = file.read().strip().split()
    array = [int(item.strip()) for item in str_array]  

def qs(array):
    def partition(arr, low, high):
        pivot = arr[high] 
        i = low - 1  
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i] 
        arr[i + 1], arr[high] = arr[high], arr[i + 1]  
        return i + 1 
    def rec_qs(arr, low, high):
        if low < high:
            partition_index = partition(arr, low, high)
            rec_qs(arr, low, partition_index - 1)  
            rec_qs(arr, partition_index + 1, high)  
    rec_qs(array, 0, len(array) - 1)  
    return array  

results = qs(array)

with open("assignment #1/qs_output.txt", 'w') as file:
    file.write(" ".join(map(str, results)))