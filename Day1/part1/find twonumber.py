# um_list = [1721, 979, 366, 299,675, 1456]

# Before you leave, the Elves in accounting just need you to fix your expense report
# (your puzzle input); apparently, something isn't quite adding up.
#
# Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
# For example, suppose your expense report contained the following:
# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299.
# Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.
# Of course, your expense report is much larger.
# Find the two entries that sum to 2020; what do you get if you multiply them together?


test_list = []
# reading from file


with open('numbers.txt', 'r') as f:
    content = f.read()
    test_list = content.split()


def convert_list_str_to_int(s_list) -> object:
    i_list = []
    for i in range(0, len(s_list)):
        i_list.append(int(s_list[i]))
    return i_list


def find_nummbers(n_list):
    for num in range(len(n_list)):
        first_num = int(n_list[num])
        need_to_find = 2020 - int(n_list[num])
        if need_to_find in n_list:
            return (first_num, need_to_find)


a = convert_list_str_to_int(test_list)

couple = find_nummbers(a)
print(f"Answer {couple[0] * couple[1]}")
