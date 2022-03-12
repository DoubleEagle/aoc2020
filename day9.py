input_file = open('day9_input.txt')

numbers = input_file.read().split('\n')

preamble_length = 25

already_calculated = dict()


def check_number(previous, number):
    if number / 2 < min(previous):
        print(number, min(previous), previous)
        print('number too small')
        return False

    if number / 2 > max(previous):
        print('number too large')
        return False

    for i in range(0, len(previous)):
        for j in range(i + 1, len(previous)):
            key = (previous[i], previous[j])
            # if key in already_calculated:
            #     if already_calculated[key] == number:
            #         return True
            # else:
            calculated = previous[i] + previous[j]
            # already_calculated[key] = calculated
            if calculated == number:
                return True
    return False


def find_contiguous_numbers(number_to_add_up_to, numbers):
    intermediate = 0
    left_pointer = 0
    right_pointer = 0
    for i in range(0, len(numbers)):
        right_pointer = i
        numbers[i] = int(numbers[i])

        intermediate += numbers[i]
        print(left_pointer, right_pointer, intermediate)
        if intermediate == number_to_add_up_to:
            print('found it!')
            return left_pointer, right_pointer
        while intermediate > number_to_add_up_to:
            print('number is bigger, so subtracting', numbers[left_pointer])
            intermediate = intermediate - numbers[left_pointer]
            left_pointer += 1
            if intermediate == number_to_add_up_to:
                print('found it after subtracting!')
                return left_pointer, right_pointer

# for i in range(0, len(numbers)):
#     numbers[i] = int(numbers[i])
#     if i < preamble_length:
#         continue
#
#     if not check_number(numbers[i-preamble_length:i], numbers[i]):
#         print('found it!', i, numbers[i])


x, y = find_contiguous_numbers(50047984, numbers)

print(min(numbers[x:y]) + max(numbers[x:y]))