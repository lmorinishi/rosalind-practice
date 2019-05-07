filename = 'data/rosalind_dna.txt'
with open(filename) as file:
    dna_string = file.read()

dna_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for letter in dna_string.strip():
    dna_dict[letter] += 1

ordered_counts = [str(value) for (key, value) in sorted(dna_dict.items())]
print(' '.join(ordered_counts))
