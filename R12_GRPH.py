filename = 'data/rosalind_grph.txt'
with open(filename) as file:
    dna_strings = file.read().strip().split('>')


dna_strings = [x.strip().split('\n', 1) for x in dna_strings if x != '']
names = [x[0] for x in dna_strings]
sequences = [x[1].replace('\n', '') for x in dna_strings]
prefixes = [x[1][:3] for x in dna_strings]

output = []
for i in range(len(names)):
    suffix = sequences[i][-3:]
    for j in range(len(prefixes)):
        if i != j and suffix == prefixes[j]:
            output.append([names[i], names[j]])


with open('data/rosalind_grph_test_output.txt', 'w') as text_file:
    for i in range(len(output)):
        text_file.write(' '.join(output[i]))
        text_file.write('\n')
