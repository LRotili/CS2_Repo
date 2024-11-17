from Bio import SeqIO
from Bio.Seq import Seq

with open("assignment #2/revp.txt", 'r') as f:
    straight_seq = SeqIO.read(f, "fasta").seq
    
complement_seq = straight_seq.reverse_complement()

results = []
for length in range(4, 13):
    for start in range(len(straight_seq) - length + 1):  
        substring = straight_seq[start:start + length]
        if substring == complement_seq[start:start + length]:
            results.append((start + 1, length))  

for position, length in results:
    print(position, length)
