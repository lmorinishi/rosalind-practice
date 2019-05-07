filename = 'data/rosalind_cons.txt'
with open(filename) as file:
    dna_strings = file.read().strip().split('>')


dna_strings = [i.split('\n', 1)[1].replace('\n', '') for i in dna_strings if i != '']
str_length = len(dna_strings[0])

output = [{'A': 0, 'C': 0, 'G': 0, 'T': 0} for i in range(str_length)]
for dna_string in dna_strings:
    for i in range(str_length):
        output[i][dna_string[i]] += 1


print(''.join([max(i.keys(), key=lambda k: i[k]) for i in output]))
for letter in ['A', 'C', 'G', 'T']:
    print(' '.join([letter + ':'] + [str(i[letter]) for i in output]))

