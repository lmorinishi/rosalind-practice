filename = 'data/rosalind_fibd.txt'
with open(filename) as file:
    n, m = file.read().strip().split(' ')


# rabbits after n months if they live for m months
# n(t) = n(t-1) + n(t-2) - n(t-m)

def get_rabbits(gen0, months, survival, totals):
    if months in totals.keys():
        return totals
    elif months <= 2:
        totals[months] = gen0
        return totals
    elif months <= survival:
        totals = get_rabbits(gen0, months - 1, survival, totals)
        totals = get_rabbits(gen0, months - 2, survival, totals)
        totals[months] = totals[months - 1] + totals[months - 2]
        return totals
    else:
        alive_count = 0
        totals = get_rabbits(gen0, months - 1, survival, totals)
        for i in range(months-survival, months-1):
            alive_count += totals[i]
        totals[months] = alive_count
        return totals


my_result = get_rabbits(1, int(n), int(m), {})
print(my_result[int(n)])
