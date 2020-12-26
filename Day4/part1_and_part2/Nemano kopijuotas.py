import re

data = open('input.txt') \
    .read() \
    .split('\n\n')

data = [[tuple(key.split(':')) for key in ID.split()] for ID in data]
requirements = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
validID = []


def IDisValid(ID, requirements):
    valid = []

    if all([field in ID for field in requirements]):
        valid.append(True) if int(ID['byr']) >= 1920 and int(ID['byr']) <= 2002 else valid.append(False)
        valid.append(True) if int(ID['iyr']) >= 2010 and int(ID['iyr']) <= 2020 else valid.append(False)
        valid.append(True) if int(ID['eyr']) >= 2020 and int(ID['eyr']) <= 2030 else valid.append(False)
        valid.append(True) if re.match('^#[0-9a-f]{6}$', ID['hcl']) else valid.append(False)
        valid.append(True) if ID['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] else valid.append(False)
        valid.append(True) if re.match('^\d{9}$', ID['pid']) else valid.append(False)
        if ID['hgt'][-2:] == 'cm':
            if int(ID['hgt'][:-2]) >= 150 and int(ID['hgt'][:-2]) <= 193:
                valid.append(True)
            else:
                valid.append(False)
        elif ID['hgt'][-2:] == 'in':
            if int(ID['hgt'][:-2]) >= 59 and int(ID['hgt'][:-2]) <= 76:
                valid.append(True)
            else:
                valid.append(False)
        else:
            valid.append(False)

    else:
        valid.append(False)
    print(valid)
    print(ID)
    return all(valid)


for ID in data:
    if IDisValid(dict(ID), requirements):
        validID.append(ID)

if __name__ == '__main__':
    print(len(validID))