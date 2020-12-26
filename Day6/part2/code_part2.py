from functools import reduce

with open('../part1/input.txt') as f:
    content = f.read()
    my_groups = [group for group in content.split('\n\n')]
    print(my_groups)

    total = 0
    for group in my_groups:
        set_lst_letter = [set(m) for m in group.strip().split('\n')]
        # print(set_lst_letter)
        yes_lst = reduce(set.intersection, set_lst_letter)
        print(yes_lst)
        total += len(yes_lst)

    print(total)
