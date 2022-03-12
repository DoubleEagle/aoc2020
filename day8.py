input_file = open('day8_input.txt')

original_steps = input_file.read().split('\n')


def find_out_if_this_works(steps):
    pointer = 0

    accumulator = 0

    visited_pointers = []

    stop = False

    while not stop:
        print('=== status: pointer = ', pointer, ', accumulator = ', accumulator, ' now executing: ', steps[pointer])
        instruction = steps[pointer]
        action, value = instruction.split(' ')
        value = int(value)
        print(value)

        if action == 'jmp':
            pointer += value
            # print('jmp', value, pointer)
        elif action == 'acc':
            accumulator += value
            # print('acc', value, accumulator)
            pointer += 1
        elif action == 'nop':
            # print('nop')
            pointer += 1
        else:
            print('helluuuuupppp', action)



        if pointer in visited_pointers:
            stop = True
            print('Already encountered this pointer: ', pointer)
            return False
        else:
            visited_pointers.append(pointer)

        if pointer == len(steps):
            print('Yay last value! ', accumulator, pointer)
            stop = True
            return True


for i in range(0, len(original_steps)):
    print('============== now at option: ', i)

    if original_steps[i][0:3] == 'jmp':
        steps_for_bruteforce = original_steps.copy()
        # print(steps_for_bruteforce)
        steps_for_bruteforce[i] = steps_for_bruteforce[i].replace('jmp', 'nop')
        # print(steps_for_bruteforce)
        if find_out_if_this_works(steps_for_bruteforce):
            exit('found it!')