input_file = open('day6_input.txt')

batches = input_file.read().split('\n\n')

# print(batches)

result = 0

for batch in batches:
    letterjar = ['a',
                 'b',
                 'c',
                 'd',
                 'e',
                 'f',
                 'g',
                 'h',
                 'i',
                 'j',
                 'k',
                 'l',
                 'm',
                 'n',
                 'o',
                 'p',
                 'q',
                 'r',
                 's',
                 't',
                 'u',
                 'v',
                 'w',
                 'x',
                 'y',
                 'z'
                 ]
    personal_answers = batch.split('\n')
    for a in personal_answers:
        sorted_a = sorted(a)
        letterjar = list(set(letterjar) & set(a))
        print(personal_answers, a, sorted_a, sorted(letterjar))
    result += len(letterjar)
    print(len(letterjar), result)

# for batch in batches:
#     personal_answers = batch.split('\n')


print(result)
