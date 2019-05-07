filename = 'data/rosalind_prot.txt'
with open(filename) as file:
    rna_string = file.read().strip()


codon_filename = 'data/codon_table.txt'
with open(codon_filename) as file:
    codon_table = file.read().split('\n')


translate = {}
for codon_pair in codon_table:
    split_codon = codon_pair.split(' ')
    translate[split_codon[0]] = split_codon[1]

print(translate.keys())


codons = [rna_string[i:i+3] for i in range(0, len(rna_string), 3)]
protein = ''
for codon in codons:
    aa = translate[codon]
    if aa == 'Stop':
        break
    else:
        protein += translate[codon]


print(protein)

