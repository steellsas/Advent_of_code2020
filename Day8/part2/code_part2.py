with open("input.txt") as f:
    content = f.read()
    lines_lst = [line.split() for line in content.split('\n')]


def last_jmp(new_lst):
    valid_f = True
    line = 0
    acum = 0
    step_lst = []
    while True:

        com = new_lst[line][0]
        num = int(new_lst[line][1])

        # checking have all lines visit
        if len(new_lst) - 1 == line:
            valid_f = False
        # check have visti line
        if line in step_lst:
            valid_f = False
            return acum, valid_f

        if com == "acc":
            acum = acum + num
            step_lst.append(line)
            line = line + 1

        if com == 'jmp':
            step_lst.append(line)
            line = line + num

        if com == "nop":
            line = line + 1

        if valid_f == False:
            return acum, True

    return acum, False


def part_two(lines_lst):
    new_lst = lines_lst.copy()
    for line in range(1, len(new_lst)):
        com = lines_lst[line][0]
        num = int(new_lst[line][1])
        # change command and check is lines lst finish

        if com == 'jmp':
            com = "nop"
        elif com == "nop":
            com = 'jmp'

        new_lst = lines_lst.copy()
        new_lst[line] = com, num

        acum, valided = last_jmp(new_lst)

        if valided:
            return acum


answer = part_two(lines_lst)
print(answer)
