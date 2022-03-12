import re

input_file = open('day4_input.txt')

passports = input_file.read().split('\n\n')

def four_digits(input):
    return bool(re.fullmatch('[0-9]{4}', str(input)))


def between(min, max, value):
    return min <= value <= max

def height_is_good(input):
    if not bool(re.fullmatch('[0-9]+((cm)|(in))', str(input))):
        return False
    if 'cm' in input:
        return between(150, 193, int(input[:-2]))
    else:
        return between(59, 76, int(input[:-2]))


def hcl_is_good(input):
    return bool(re.fullmatch('#[0-9a-z]{6}', str(input)))


def ecl_is_good(input):
    options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return input in options


def pid_is_good(input):
    return bool(re.fullmatch('[0-9]{9}', str(input)))


def contains_required_fields(passport):
    required_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]
    passport = passport.replace('\n', ' ')
    pass_fields = passport.split(' ')

    if len(pass_fields) < 7:
        # misses too many fields
        return False

    return all(field in passport for field in required_fields)


result_count = 0
results = []

wrong = []


for passport in passports:
    if contains_required_fields(passport):
        passport = passport.replace('\n', ' ')
        pass_fields = passport.split(' ')
        invalid = False
        for field in pass_fields:
            field_name, field_value = field.split(':')
            if field_name == 'byr':
                if not between(1920, 2002, int(field_value)):
                    print('byr wrong', passport)
                    wrong.append(passport)
                    invalid = True
            elif field_name == 'iyr':
                if not between(2010, 2020, int(field_value)):
                    print('iyr wrong', passport)
                    wrong.append(passport)
                    invalid = True
            elif field_name == 'eyr':
                if not between(2020, 2030, int(field_value)):
                    print('eyr wrong', passport)
                    wrong.append(passport)
                    invalid = True
            elif field_name == 'hgt':
                if not height_is_good(field_value):
                    print('hgt wrong', passport)
                    wrong.append(passport)
                    invalid = True
            elif field_name == 'hcl':
                if not hcl_is_good(field_value):
                    print('hcl wrong', passport)
                    wrong.append(passport)
                    invalid = True
            elif field_name == 'ecl':
                if not ecl_is_good(field_value):
                    print('ecl wrong', passport)
                    wrong.append(passport)
                    invalid = True
            elif field_name == 'pid':
                if not pid_is_good(field_value):
                    print('pid wrong', passport)
                    wrong.append(passport)
                    invalid = True

            if invalid:
                break

        if not invalid:
            result_count += 1
            results.append(passport)




print(result_count)
print(results)
print(wrong)
