filename = 'data/rosalind_revc.txt'
with open(filename) as file:
    dna_string = file.read()

output_string = ''
translate = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
for letter in dna_string.strip()[::-1]:
    output_string = output_string + translate[letter]

print(output_string)
