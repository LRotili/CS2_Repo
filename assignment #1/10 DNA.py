'''my_seq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
a = 0
c = 0
g = 0
t = 0

for i in my_seq: 
    if i == "A":
        a = a +1
    elif i == "C":
        c +=1
    elif i == "G":
        g +=1
    else:
        t +=1

print(a, c, g, t)

'''

#or with BioPython
from Bio.Seq import Seq

with open("assignment #1/dna.txt", "r") as f:
    my_seq = Seq(f.read())

a = my_seq.count("A")
c = my_seq.count("C")
g = my_seq.count("G")
t = my_seq.count("T")

print(a, c, g, t)