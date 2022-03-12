input_file = open('day3_input.txt')

lines = input_file.read().split('\n')

width = len(lines[0])
height = len(lines)

print('width, height: ', width, height)

def count_trees(right_step, down_step):
    tree_counter = 0

    horizontal_counter = 0
    for vertical_counter in range(0, height, down_step):
        if vertical_counter == 0:
            continue
        horizontal_counter = (horizontal_counter + right_step) % width
        # print(vertical_counter, horizontal_counter, lines[vertical_counter][horizontal_counter])
        if lines[vertical_counter][horizontal_counter] == '#':
            tree_counter += 1

    return tree_counter


print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2))

print(count_trees(1, 1))
print(count_trees(3, 1))
print(count_trees(5, 1))
print(count_trees(7, 1))
print(count_trees(1, 2))