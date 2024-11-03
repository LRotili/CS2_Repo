array = []
with open(r"assignment #1/par.txt", "r") as file:
    
    el_numb = file.readline()
    whole = file.read()
    array_str = whole.split(" ")
    for numb in array_str: array.append(int(numb))

rightside, leftside, pivotwins = [], [], []

for numb in array:
    if numb > array[0]: rightside.append(numb)
    elif numb < array[0] : leftside.append(numb)
    else: pivotwins.append(numb)

sorted = leftside + pivotwins + rightside

sorted = ('[', ' '.join(str(x) for x in sorted), ']')

with open('assignment #1/par_result.txt', 'w') as f:
    f.write(str(sorted))
