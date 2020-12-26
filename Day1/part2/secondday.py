# -- Part Two ---
# The Elves in accounting are thankful for your help;
# one of them even offers you a starfish coin they had left over from a past vacation.
# They offer you a second one if you can find three numbers in your expense report that meet the same criteria.
# Using the above example again, the three entries that sum to 2020 are 979, 366, and 675.
# Multiplying them together produces the answer, 241861950.
# In your expense report, what is the product of the three entries that sum to 2020?

# ------- naudojame taimingui
from functools import wraps
from time import time


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")

    return _time_it


# -----------------------------------------

test_list = []
with open('../part1/numbers.txt', 'r') as f:
    test_list = [int(x) for x in f.read().split()]


# def find_tree_numbers(i_list):
#
#     for i_num in range(len(i_list)-1):
#         sum = int(i_list[i_num]) + int(i_list[i_num+1])
#         print(sum)
#         if sum < 2020:
#             # patikriname ar  sumai yra skaicius
#
#              number3 = find_number(i_list, sum)
#              print(number3)
#              if number3:
#                  print([i_list[i_num], i_list[i_num+1], number3])

@measure
def find_numbers(i_list):
    asw = None

    for n in test_list:
        dif = 2020 - n
        avaible = [x for x in test_list if x < dif]
        for item in avaible:
            dif2 = dif - item
            if dif2 in avaible:
                asw = n * item * dif2
                print(asw)
                break
        if asw is not None:
            break


find_numbers(test_list)
