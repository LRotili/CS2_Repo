#from Bio.Seq import Seq

with open(r"assignment #1/subs.txt", "r") as file:
    s = file.readline()
    t = file.readline()

#Seq(s).count_overlap(t))


pos_list = [ ]

if len(t) <= len (s):
    for position in range(len(s)):
        if s[position:].startswith(t):
            pos_list.append(position+1)

print(pos_list)

#for rosalind            
print('[', ' '.join(str(x) for x in pos_list), ']')