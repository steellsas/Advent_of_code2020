import re

test_list = []
with open('input.txt', 'r') as f:
    test_list = [x for x in f.read().split('\n')]

# findall numbers in string

corect_sum = 0

for item in test_list:
    pattern = '\d+'
    # number list num list
    num_list = re.findall(pattern, item)
    line_list = re.split(':', item)
    min_num = int(num_list[0])
    max_num = int(num_list[1])
    # leter
    letter = line_list[0].split()[1]
    # password string
    password = line_list[1]
    # cheking passwords is correct
    letter_count = password.count(letter)

    if letter_count >= min_num and letter_count <= max_num:
        corect_sum = corect_sum + 1

print(corect_sum, len(test_list))
