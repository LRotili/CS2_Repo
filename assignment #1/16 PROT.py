from Bio.Seq import Seq

with open(r"assignment #1/prot.txt", "r") as file:
    my_seq = Seq(file.read())

my_prot = my_seq.translate(stop_symbol=" ")

print(my_prot)