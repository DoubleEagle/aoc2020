input_file = open('day10_2dummyinput.txt')

jolts = input_file.read().split('\n')
jolts = [0] + jolts + [jolts[-1] + 3]

for i in range(0, len(jolts)):
    jolts[i] = int(jolts[i])

jolts.sort()

highest_number = max(jolts)

count = 0

print(highest_number)
print(jolts)
