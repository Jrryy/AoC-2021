part_1 = part_2 = 0

with open('input.txt', 'r') as f:
    for line in f:
        all_numbers, output = line.split('|')
        output_list = [''.join(sorted(list(output_digit))) for output_digit in output.split()][::-1]
        part_1 += len(list(filter(lambda x: len(x) in (2, 3, 4, 7), output_list)))

        all_numbers_list = sorted(all_numbers.split(), key=lambda x: len(x))
        _1 = all_numbers_list[0]
        _7 = all_numbers_list[1]
        _4 = all_numbers_list[2]
        _235 = set(all_numbers_list[3:6])
        _069 = set(all_numbers_list[6:9])
        _8 = all_numbers_list[9]

        _3 = next(filter(lambda x: all([segment in x for segment in _1]), _235))

        _25 = _235 - {_3}
        _2, _5 = sorted(_25, key=lambda x: sum([segment in x for segment in _4]))

        _9 = next(filter(lambda x: all([segment in x for segment in _3]), _069))

        _06 = _069 - {_9}
        _6, _0 = sorted(_06, key=lambda x: sum([segment in x for segment in _1]))

        numbers_repr = {
            ''.join(sorted(list(v))): i
            for i, v in enumerate([_0, _1, _2, _3, _4, _5, _6, _7, _8, _9])
        }
        part_2 += sum(map(lambda x: numbers_repr[x[1]]*10**x[0], enumerate(output_list)))


print(f'Part 1: {part_1}')
print(f'Part 2: {part_2}')
