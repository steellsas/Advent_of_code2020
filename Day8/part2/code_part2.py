
with open("input.txt") as f:
    content = f.read()
    lines_lst =[ [line.split(), True] for line in content.split('\n') ]

ind = 0
acum = 0

while ind < len(lines_lst):

    com = lines_lst[ind][0][0]
    num = int(lines_lst[ind][0][1])
    flag = lines_lst[ind][1]
    # if not flag:
    #     print(ind, flag)
    #     break
    print(com, num,'veliava', flag, ind)


    if com == "acc":
        acum = acum + num
    lines_lst[ind][1] = False
    if com == 'jmp':
        if not lines_lst[ind + num- 1][1]:
            print(lines_lst[ind + num- 1][1])
            lines_lst[ind][0][0] = 'nop'

        else:
            ind = ind + num
            continue


    print(acum)
    ind = ind +1


