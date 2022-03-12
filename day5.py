input_file = open('day5_input.txt')

lines = input_file.read().split('\n')


def convert_row_to_number(input):
    input = input.replace('F', '0')
    input = input.replace('B', '1')
    return int(input, 2)


def convert_seat_to_number(input):
    input = input.replace('L', '0')
    input = input.replace('R', '1')
    return int(input, 2)


# results = []
#
# for line in lines:
#     row_letters = line[0:7]
#     seat_letters = line[7:10]
#     results.append(convert_row_to_number(row_letters) * 8 + convert_seat_to_number(seat_letters))
#
# print(max(results))


all_seats = []
for i in range(0,128):
    for j in range(0,8):
        all_seats.append(str(i) + "_" + str(j))

print(all_seats)

for line in lines:
    row_letters = line[0:7]
    seat_letters = line[7:10]
    # print(str(convert_row_to_number(row_letters)) + "_" + str(convert_seat_to_number(seat_letters)))
    all_seats.remove(str(convert_row_to_number(row_letters)) + "_" + str(convert_seat_to_number(seat_letters)))

for i in all_seats:
    print(i)