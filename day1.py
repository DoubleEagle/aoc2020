input_file = open('day1_input.txt')

numbers = input_file.read().split('\n')

for i in range(0, len(numbers) - 1):
    for j in range(i + 1, len(numbers) - 1):
        for k in range(j + 1, len(numbers) - 1):

            print(i, j, k, numbers[i], numbers[j], numbers[k])
            if int(numbers[i]) + int(numbers[j]) + int(numbers[k]) == 2020:
                print('found it!', int(numbers[i])*int(numbers[j])*int(numbers[k]))
                exit()