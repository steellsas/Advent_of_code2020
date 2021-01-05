
with open("input.txt") as file:
    data = file.read()
    data_lst = [int(number) for number in data.split()]
#print(data_lst)


# cheking number - sum two numbers of sublst
def check_number(sub_lst,num):
    for n in sub_lst:
        search_nm = num - n
        if search_nm in sub_lst:
            return True
    return False


test = [35, 20, 15, 25, 47]
nn = 40

#print(check_number(test,nn))

def find_number(lst):
    start = 0
    end = 26
    while end <= len(lst):
        sub_lst =lst[start:end]
        number = sub_lst[-1]

       # print(sub_lst[:-1],number)
        valid = check_number(sub_lst[:-1],number)
        if not valid:
            return number

        start = start + 1
        end = end +1

print(find_number(data_lst))