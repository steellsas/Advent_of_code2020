import re

with open("input.txt", 'r') as f:
    content = f.read()
    line_list = [re.sub('bags|bag', '', line) for line in content.split('\n')]

my_color = "shiny gold"
mydict = {}

for line in line_list:
    color_dic = {}
    a = line.split('contain')
    key = a[0].strip()
    value = a[1]
    color_dic[key] = [element.strip() for element in value.replace('.', '').split(',')]
    mydict.update(color_dic)


def check_color_in_decs_key(color: str, my_dic: dict):
    for key, value in my_dic.items():
        if color == key:
            return my_dic[color]
        else:
            return False


def calc_bags(my_color):
    total_count = 0
    contain = mydict[my_color]
    if contain:
        for item in contain:
            new_color = re.sub(r'\d+', '', item).strip()
            if re.findall(r'\d+', item):
                num = int(re.findall(r'\d+', item)[0])
                total_count = total_count + (num + num * calc_bags(new_color))

        return total_count


sk = calc_bags(my_color)
print(sk)
