with open('input.txt', 'r') as f:
    content = f.read()

lst_slopes = content.split()


def travel_by_toboggan(lst_slopes, iter, ):
    star_p = 0
    my_road = ''
    multi = 1
    i_num = 1
    down = 0
    sum_tree = 0
    # iter = 3
    end_p = iter

    for slope in lst_slopes:

        v_slope = slope * multi
        if v_slope[down] == '#':
            sum_tree = sum_tree + 1

        my_road = my_road + v_slope[star_p:end_p]
        star_p = end_p
        down = end_p
        end_p = star_p + iter

        if (len(v_slope) // iter) == i_num:
            multi = multi + 1
        i_num += 1

    return sum_tree


multi_road = 1
condition_lst = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for condition in condition_lst:
    turn = condition[0]
    go_down = condition[1]
    if go_down == 1:
        road = travel_by_toboggan(lst_slopes, turn)
    else:
        road = travel_by_toboggan(lst_slopes[::2], turn)
    print(road)
    multi_road = multi_road * road

print(multi_road)

# print(len(lst_slopes), len(lst_slopes[0]))
# print(f" my answer:  {road}")


# ..#O#.X..O#.X..X#.O..X.#X#.X..X.#
