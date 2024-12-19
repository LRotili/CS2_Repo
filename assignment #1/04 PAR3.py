# no solution by the deadline

with open(r"assignment #1/par3.txt") as file:
    input = []
    for line in file:
        input.append(line.split())

array = []

for number in input[1]:
    array.append(int(number))

pivot = array[0]
left_side, middle, right_side = [], [], []

for number in array:
    if number < pivot:
        left_side.append(number)
    elif number > pivot:
        right_side.append(number)
    else:
        middle.append(number)

total_arr = left_side + middle + right_side

for number in total_arr:
    print(number, end=' ')


with open("assignment #1/par3_output.txt", 'w') as file:
    file.write(" ".join(map(str,total_arr)))
