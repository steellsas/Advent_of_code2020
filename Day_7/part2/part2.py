import re

with open("../part1/input.txt", 'r') as f:
    content = f.read()
    line_list = [re.sub('bags|bag','', line) for line in content.split('\n')]
    print(line_list)
#  color: color1,color2
my_color = "shiny gold"

dic_lst= []

for line in line_list:
    color_dic = {}
    contains ={}
    a = line.split('contain')
    key = a[0]
    value = a[1]
    #value = re.sub('\d', '',a[1] )
    #print(value.replace('.', ''))
    color_dic[key]=[element.strip() for element in value.replace('.', '').split(',') ]
    dic_lst.append(color_dic)
    #print(type(color_dic[key]))
    # patt = re.sub('bags','', a[0])
    # print(patt.rstrip(), len(patt.rstrip()), len(patt))
print(dic_lst)

