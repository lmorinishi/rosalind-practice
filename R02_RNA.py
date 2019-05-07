filename = 'data/rosalind_rna.txt'
with open(filename) as file:
    dna_string = file.read()

output = ''
for letter in dna_string:
    if letter == 'T':
        output = output + 'U'
    else:
        output = output + letter

print(output)
