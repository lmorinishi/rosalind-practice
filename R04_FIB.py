filename = 'data/rosalind_fib.txt'
with open(filename) as file:
    n, k = file.read().strip().split(' ')


def rabbit_love(gen0, months, n_offspring, totals={}):
    if months <= 2:
        if months not in totals.keys():
            totals[months] = gen0
        return totals
    else:
        if months not in totals.keys():
            totals = rabbit_love(gen0, months-2, n_offspring, totals)
            totals = rabbit_love(gen0, months-1, n_offspring, totals)
            totals[months] = totals[months-1] + totals[months-2]*n_offspring
        return totals


def get_population(gen0, months, n_offspring):
    output_dict = rabbit_love(gen0, months, n_offspring, totals={})
    return output_dict[months]


print(get_population(1, int(n), int(k)))
