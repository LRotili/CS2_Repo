from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

current_id = None

maximum_id = ''
maximum_gc = 0

with open('assignment #1/gc.txt', 'r') as file:
    for record in SeqIO.parse(file, 'fasta'):
        curr_gc_frac = gc_fraction(record)
        current_id = record.id
        if curr_gc_frac > maximum_gc:
            maximum_gc = curr_gc_frac
            maximum_id = current_id
        
print(maximum_id, maximum_gc*100)