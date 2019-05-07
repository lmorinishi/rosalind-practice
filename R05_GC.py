filename = 'data/rosalind_gc.txt'
with open(filename) as file:
    fasta_file = file.read().strip()


def compute_gc(dna_string):
    g_or_c = 0
    for letter in dna_string:
        if letter in ['C', 'G']:
            g_or_c += 1
    return round(g_or_c/len(dna_string) * 100, 6)


fasta_items = fasta_file.split('>')
fasta_items = [(x.split('\n', 1)[0], x.split('\n', 1)[1].replace('\n', '')) for x in fasta_items if x != '']
best_gc_name = 'none'
best_gc = 0

for dna_string in fasta_items:
    current_gc = compute_gc(dna_string[1])
    if current_gc > best_gc:
        best_gc_name = dna_string[0]
        best_gc = current_gc


print(best_gc_name + '\n' + str(best_gc))
