from Bio import SeqIO
from Bio.Seq import Seq
from functools import reduce

seq_list = []
with open(r"assignment #2/splc.txt", 'rt') as file:
    for record in SeqIO.parse(file, "fasta"):     

        seq_list = seq_list + [record.seq]

mRNA = str(seq_list[0])
seq_list.remove(mRNA)

introns = list()
for i in seq_list:
    my_int= str(i)
    introns.append(my_int)
 
res = reduce(lambda s, sub: s.replace(sub, ""), introns, mRNA)

protein = Seq(res).translate(stop_symbol = '', to_stop = True)

print(protein)