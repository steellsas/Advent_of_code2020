

with open("input.txt") as f:
    content = f.read()
    lines_lst =[ [line.split(), True] for line in content.split('\n') ]

ind = 0
acum = 0

while ind < len(lines_lst):

    com = lines_lst[ind][0][0]
    num = int(lines_lst[ind][0][1])
    flag = lines_lst[ind][1]

    if flag:
        lines_lst[ind][1] = False
        if com == "acc":
            acum = acum + num
        if com == 'jmp':
            ind = ind + num
            continue

    else:
        print(acum)
        break
    ind = ind +1
