filename = 'data/rosalind_hamm.txt'
with open(filename) as file:
    two_strings = file.read().strip().split('\n')


def str_hamm(str_1, str_2):
    if len(str_1) != len(str_2):
        print("Strings differ in length")
    else:
        n_mismatch = 0
        for letter_idx in range(len(str_1)):
            if str_1[letter_idx] != str_2[letter_idx]:
                n_mismatch += 1
    return n_mismatch


print(str_hamm(two_strings[0], two_strings[1]))

