filename = 'data/rosalind_iprb.txt'
with open(filename) as file:
    all_data = file.read().strip()


def get_prob_pick(p1, p2, total_population):
    return (p1/total_population) * (p2/(total_population-1))


def breed(p1, p2):
    if p1 == 0 or p2 == 0:
        return 1
    elif p1 == 1 & p2 == 1:
        return 0.75
    elif p1 == 1 or p2 == 1:
        return 0.5
    else:
        return 0


# k are homozygous dominant, m are heterozygous, n are homozygous rec`essive
all_data = [int(i) for i in all_data.split(' ')]
total_pop = sum(all_data)

all_combos = 0
for i in range(len(all_data)):
    for j in range(len(all_data)):
        if i == j:
            prob_pick = get_prob_pick(all_data[i], all_data[j]-1, total_pop)
        else:
            prob_pick = get_prob_pick(all_data[i], all_data[j], total_pop)

        all_combos += breed(i, j) * prob_pick


print(round(all_combos, 6))


