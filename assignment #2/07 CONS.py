from Bio import SeqIO
sequences = []
with open("assignment #2/cons.txt") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        sequences.append(record.seq)

n = len(sequences[0])

profile_matrix = {
    'A': [0]*n,
    'C': [0]*n,
    'G': [0]*n,
    'T': [0]*n
    }

for a in sequences:
    for position, nucleotide in enumerate(a):  
        profile_matrix[nucleotide][position] += 1

result = [] 
for position in range(n):
    max_count = 0
    max_nucleotide = None
    for nucleotide in ['A', 'C', 'G', 'T']:
        count = profile_matrix[nucleotide][position]
        if count > max_count:
            max_count = count
            max_nucleotide = nucleotide
    result.append(max_nucleotide)

consensus = ''.join(result)

print(profile_matrix)

print(consensus)