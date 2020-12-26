with open('input.txt') as f:
    content = f.read()
    my_groups = [group for group in content.split('\n\n')]

    print(my_groups)


# find group unique letters
def not_reapeat_letter(groups):
    new_lst = []
    for group in groups:
        setas = list(set(group))
        if '\n' in setas:
            setas.remove('\n')
        new_lst.append(setas)
    return new_lst


new_groups = not_reapeat_letter(my_groups)
print(new_groups)


def count_yes(group_lst):
    sum_of_yes = 0
    for group in group_lst:
        group_yes = len(group)
        sum_of_yes = sum_of_yes + group_yes
    print(sum_of_yes)


count_yes(new_groups)
