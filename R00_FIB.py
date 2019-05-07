def rec_fib(n):
    if n <= 1:
        return n
    else:
        return rec_fib(n-2) + rec_fib(n-1)


def dp_fib(n):
    fib_list = [0, 1]
    while len(fib_list) < n + 1:
        fib_list.append(0)

    if n <= 1:
        return n
    else:
        if fib_list[n-1] == 0:
            fib_list[n-1] = dp_fib(n-1)
        if fib_list[n-2] == 0:
            fib_list[n-2] = dp_fib(n-2)

    fib_list[n] = fib_list[n-2] + fib_list[n-1]
    return fib_list[n]


print(rec_fib(10))
print(dp_fib(10))