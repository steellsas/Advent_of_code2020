import re

with open('input.txt', 'r') as f:
    test_list = [x for x in f.read().split('\n')]

corect_sum = 0
for item in test_list:

    # number list num list
    num_list = re.findall('\d+', item)
    line_list = re.split(':', item)
    first_p = int(num_list[0])
    second_p = int(num_list[1])
    # leter
    letter = line_list[0].split()[1]
    # password string
    password = line_list[1]

    if (password[first_p] == letter) or (password[second_p] == letter):
        if password[first_p] != password[second_p]:
            corect_sum += 1

print(corect_sum, len(test_list))
