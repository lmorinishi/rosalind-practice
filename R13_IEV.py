filename = 'data/rosalind_iev.txt'
with open(filename) as file:
    dna_strings = file.read().strip()


# 1 AA-AA
# 2 AA-Aa
# 3 AA-aa
# 4 Aa-Aa
# 5 Aa-aa
# 6 aa-aa
n_couples = [int(x) for x in dna_strings.split(' ')]
p_couples = [1, 1, 1, 0.75, 0.5, 0]

print(list(zip(n_couples, p_couples)))
pA = [2 * x * y for (x, y) in zip(n_couples, p_couples)]
print(sum(pA))

