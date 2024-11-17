from math import factorial as fact
import itertools

n = 7
initial_list = []

permutations = list(itertools.permutations(range(1, n+1)))

with open("assignment #2/output_perm.txt", "w") as file:
    file.write(f"{fact(n)}\n") 

    for perm in permutations:
       file.write(" ".join(map(str, perm)) + "\n")