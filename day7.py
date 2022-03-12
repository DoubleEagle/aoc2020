input_file = open('day7_input.txt')

rules = input_file.read().replace('bags', 'bag').split('.\n')

print(rules)

rules_dict = dict()

parent_bags = dict()
number_of_bags = 0

# for rule in rules:
#     if 'no other bags' in rule:
#         rules_dict[rule.split(' no other bags')[0]] = {}
#     else:
#         outer_bag, contents = rule.split(' contain ')
#         rules_dict[outer_bag] = {}
#         # for content in contents.split(', '):
#         #     if 'bags' in content:
#         #         rules_dict[outer_bag][con]


def get_possible_parent_bags_of_one_bag(bag):
    occurences_rules = [rule for rule in rules if bag in rule]
    parent_bags = []

    for rule in occurences_rules:
        outer_bag, contents = rule.split(' contain ')
        if bag in contents:
            parent_bags.append(outer_bag)

    return parent_bags


def get_parent_bag_count(bag):
    parents = get_possible_parent_bags_of_one_bag(bag)
    parent_bags.update(parents)

    for parent in get_possible_parent_bags_of_one_bag(bag):
        get_parent_bag_count(parent)


def how_many_bags_can_i_contain(bag, multiplier):
    print('============ new recursion... ', bag, multiplier)
    occ_rule = [rule for rule in rules if rule.startswith(bag)]
    # print(occ_rule)
    own_children_count = 0
    grand_children_count = 0
    if not 'no other bag' in occ_rule[0]:
        outer_bag, contents = occ_rule[0].split(' contain ')
        childs = contents.split(', ')
        print(childs)
        for child in childs:
            own_children_count += int(child[0])
            update_number_of_bags(int(child[0]) * multiplier)
            grand_children_count += how_many_bags_can_i_contain(child[2:], multiplier * int(child[0]))

    return 1 + own_children_count + grand_children_count


def update_number_of_bags(n_o_b):
    global number_of_bags
    number_of_bags += n_o_b


# get_parent_bag_count('shiny gold bag')

# print(len(parent_bags))

print(how_many_bags_can_i_contain('shiny gold bag', 1))

print(number_of_bags)