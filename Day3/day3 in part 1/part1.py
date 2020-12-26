with open('test2_input.txt', 'r') as f:
    content = f.read()

lst_slopes = content.split()


# reikia pasidaryti =ymejima kai down  ir yra medis =ymeti x

def travel_by_toboggan(lst_slopes):
    star_p = 0

    my_road = ''
    multi = 1
    i_num = 1
    down = 0
    sum_tree = 0
    iter = 7
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


road = travel_by_toboggan(lst_slopes)

# # def count_tree(road):
# #      return road.count('#')
# print(count_tree(road))
print(len(lst_slopes), len(lst_slopes[0]))
print(f" my answer:  {road}")

