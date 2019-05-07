filename = 'data/rosalind_subs.txt'
with open(filename) as file:
    input_strings = file.read().strip().split('\n')


def is_substring(big_string, sub_string):
    if sub_string == '':
        return True
    elif len(sub_string) > len(big_string):
        return False
    elif big_string[0] == sub_string[0]:
        return is_substring(big_string[1:], sub_string[1:])
    else:
        return False


output = []
for idx in range(len(input_strings[0])):
    if is_substring(input_strings[0][idx:], input_strings[1]):
        output.append(str(idx+1))


print(' '.join(output))
