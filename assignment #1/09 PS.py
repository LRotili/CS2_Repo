# no solution by the deadline 
array = []
with open(r"assignment #1/ps.txt", "r") as file:
    k = file.readline()
    array_str = file.read().strip().split()
    for numb in array_str: 
        if numb.lstrip('-').isdigit():
            array.append(int(numb))

n = array.pop()

result = []
while n!=0:
    min_element = min(array)
    array.remove(min_element)
    if min_element not in result:
        result = result + [min_element]
        n-=1
    else: 
        pass

with open("assignment #1/ps_output.txt", 'w') as file:
    file.write(" ".join(map(str, result)))
