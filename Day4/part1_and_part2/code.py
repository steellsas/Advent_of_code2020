import re

with open('input.txt', 'r') as f:
    content = f.read()
    passports = [p for p in content.split('\n\n')]

    print(len(content), len(passports))


# check_data = ['byr', 'iyr', ' eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
# test_dic1 = {'eyr':1972, 'cid':100,'hcl':'#18171d', 'ecl':'amb', 'hgt':"170cm", 'pid':'18600','iyr':2018, 'byr':1926}

def prepare_data(passport_lst):
    sum = 0
    for item in passport_lst:
        passport_data = item.split()

        if len(passport_data) == 8:
            paassport_dic1 = listtodic(passport_data)

            if validate_passport(paassport_dic1):
                sum = sum + 1

        elif len(passport_data) == 7:
            paassport_dic = listtodic(passport_data)
            if 'cid' not in paassport_dic.keys():

                if validate_passport(paassport_dic):
                    sum = sum + 1

    return sum


def validate_passport(test_dic):
    valid_lst = []
    if 1920 <= int(test_dic['byr']) <= 2002:
        valid_lst.append(True)
    else:
        valid_lst.append(False)

    if 2010 <= int(test_dic['iyr']) <= 2020:
        valid_lst.append(True)
    else:
        valid_lst.append(False)

    if 2020 <= int(test_dic['eyr']) <= 2030:
        valid_lst.append(True)
    else:
        valid_lst.append(False)

    if test_dic['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        valid_lst.append(True)
    else:
        valid_lst.append(False)

    if re.match('^#[0-9a-f]{6}$', test_dic['hcl']):
        valid_lst.append(True)
    else:
        valid_lst.append(False)

    if re.match('^\d{9}$', test_dic['pid']):
        valid_lst.append(True)
    else:
        valid_lst.append(False)

    if validate_in_or_cm(test_dic['hgt']):
        valid_lst.append(True)
    else:
        valid_lst.append(False)

    if False in valid_lst:
        return False
    else:
        return True


def listtodic(lst):
    d = {}
    for d1 in lst:
        key, value = d1.split(':')
        d[key] = value
    return d


def validate_in_or_cm(value: str):
    if value[-2:] == 'cm':
        if 150 <= int(value[:-2]) <= 193:
            return True
        else:
            return False

    elif value[-2:] == 'in':
        if 59 <= int(value[:-2]) <= 76:
            return True
        else:
            return False


# asn = validate_passport(test_dic1)
answer = prepare_data(passports)
print(answer)
