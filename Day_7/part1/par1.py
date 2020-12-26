import re

with open("input.txt", 'r') as f:
    content = f.read()
    line_list = [re.sub('bags|bag', '', line) for line in content.split('\n')]
    # print(line_list)
#  color: color1,color2
my_color = "shiny gold"

dic_lst = []
count = 0
for line in line_list:
    color_dic = {}
    a = line.split('contain')
    key = a[0]
    value = re.sub('\d', '', a[1])
    # print(value.replace('.', ''))
    color_dic[key] = [element.strip() for element in value.replace('.', '').split(',')]
    dic_lst.append(color_dic)
    # print(type(color_dic[key]))
    # patt = re.sub('bags','', a[0])
    # print(patt.rstrip(), len(patt.rstrip()), len(patt))


# print(dic_lst)

def color_have(lst):
    for dic_c in lst:
        print(dic_c)


# color_have(dic_lst)
yes_lst = []


def check_all_colors(color_search, my_bags_lst=[]):
    bags = check_in_all_dics(color_search)
    if bags:
        my_bags_lst = my_bags_lst + bags
        for c in bags:
            bag = check_all_colors(c.strip(), my_bags_lst)
            my_bags_lst = bag
    else:
        return my_bags_lst
    return my_bags_lst


# checking color is in d_color list (in dic value)
def check_color(color, dic_color):
    for d_key, d_color in dic_color.items():
        if color in d_color:
            return d_key


# checking in dict key
def check_in_all_dics(color_search):
    yes_lst = []
    for dic_color in dic_lst:
        direct = check_color(color_search, dic_color)
        if direct != None:
            yes_lst.append(direct)

    return yes_lst


# print(check_in_all_dics('muted yellow', dic_lst))
# print(check_in_all_dics('light red'))
# print(check_all_colors('muted yellow'))
aa = check_all_colors(my_color)
print(len(set(aa)))
