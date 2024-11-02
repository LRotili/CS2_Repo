'''DNAstring = 'GATGGAACTTGACTACGTAAATT'
RNAstring = ""

RNAstring = DNAstring.replace('T', 'U')

print(RNAstring)'''

from Bio.Seq import Seq
with open(r"assignment #1/rna.txt", "r") as file:
    DNAstring = Seq(file.read())

RNAstring = DNAstring.transcribe()
print(RNAstring)
