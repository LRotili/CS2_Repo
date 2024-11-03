numbers = []

with open('assignment #1/ins.txt', 'r') as file:
    length_array = file.readline()
    data = file.read()

input_list=[]

for num in data.split():
    input_list.append(int(num))

counter = 0

for i in range (1 , len (input_list)) :
    key = input_list [ i ]
    j = i - 1
    while j >= 0 and key < input_list [j]:
        counter += 1
        input_list [ j +1] = input_list [ j ]
        j -= 1
    input_list [ j +1] = key
    
print(counter)