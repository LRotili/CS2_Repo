a_lst = []
b_lst = []

with open('assignment #1/mer.txt', 'r') as file:
    length_array_a = file.readline()
    a_str = file.readline()
    length_array_b = file.readline()
    b_str = file.readline()

for num in a_str.split():
	a_lst.append(int(num))

for num in b_str.split():
    b_lst.append(int(num))

def merge_sorted_lists(list_a, list_b):
	output = []
	cursor_a=0
	cursor_b=0

	while cursor_a < len(list_a) and cursor_b < len(list_b):
		if list_a[cursor_a] < list_b[cursor_b]:
			output.append(list_a[cursor_a])
			cursor_a += 1
		else:
			output.append(list_b[cursor_b])
			cursor_b += 1
			
	while cursor_a < len(list_a):
		output.append(list_a[cursor_a])
		cursor_a += 1

	while cursor_b < len(list_b):
		output.append(list_b[cursor_b])
		cursor_b += 1
		
	return output

def stripcommas(array_with_commas):
	    print(''.join(str(array_with_commas).split(',')))
	

merged = (merge_sorted_lists(a_lst, b_lst))
stripcommas(merged)