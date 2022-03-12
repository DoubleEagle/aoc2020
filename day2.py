input_file = open('day2_input.txt')

lines = input_file.read().split('\n')

result = 0
result_content = []

# for l in lines:
#     count, letter, password = l.split(' ')
#     # print(count, letter, password)
#
#     min, max = count.split('-')
#     min = int(min)
#     max = int(max)
#     letter = letter[0]
#
#     if min <= password.count(letter) <= max:
#         result += 1
#         result_content.append(l)
#
#
# print(result)
# print(result_content)

for l in lines:
    count, letter, password = l.split(' ')
    # print(count, letter, password)

    min, max = count.split('-')
    first_pos = int(min) - 1
    second_pos = int(max) - 1
    letter = letter[0]

    first_letter = password[first_pos]
    second_letter = password[second_pos]

    print(l, first_pos, second_pos, password[first_pos], password[second_pos])

    if first_letter != second_letter:
        if first_letter == letter or second_letter == letter:
            result += 1
            result_content.append(l)

print(result)
print(result_content)

# print(lines)
