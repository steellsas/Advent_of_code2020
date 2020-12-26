with open('../part2/input.txt', 'r') as file:
    content = file.read()
    bord_code = [bord for bord in content.split()]


def find_my_row(code: str):
    start_p = 0
    end_p = 127
    mid = None
    for letter in code:
        if letter == 'F':
            end_p = (start_p + end_p) // 2
            mid = end_p
        else:
            start_p = (start_p + end_p) // 2 + 1
            mid = start_p
    return mid


def find_colim(code: str):
    start_p = 0
    end_p = 7
    mid = None
    for letter in code:
        if letter == 'L':
            end_p = (start_p + end_p) // 2
            mid = end_p
        else:
            start_p = (start_p + end_p) // 2 + 1
            mid = start_p
    return mid


def calc_seat_id(b_codes):
    id_lst = []
    for row in b_codes:
        my_row = find_my_row(row[:-3])
        colum = find_colim(row[-3:])
        id = my_row * 8 + colum
        id_lst.append(id)
        print(f'id {id} row {my_row}, colum {colum}')

    return max(id_lst)

# seat = find_colim('RRR')
# seat1 = find_colim('RLL')
# seat2 = find_colim('RLR')
# print(seat,seat1,seat2)

# answer = find_my_row('BFFFBBF')
# print('atsakymas',answer)
# answer1 = find_my_row('BBFFBBF')
# print('BBFFBBF atsakymas1',answer1)
# answer2 = find_my_row('FFFBBBF')
# print('FFFBBBF atsakymas2',answer2)

answer = calc_seat_id(bord_code)
print(answer)
