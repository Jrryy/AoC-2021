def init_tree(depth: int, max_depth: int, current: list) -> None:
    if depth <= max_depth:
        current += [[], [], []]
        init_tree(depth + 1, max_depth, current[0])
        init_tree(depth + 1, max_depth, current[1])


def find_oxygen(current: list) -> str:
    if len(current[2]) == 1:
        return current[2][0]
    if len(current[0][2]) > len(current[1][2]):
        return find_oxygen(current[0])
    return find_oxygen(current[1])


def find_carbon(current: list) -> str:
    if len(current[2]) == 1:
        return current[2][0]
    if len(current[0][2]) <= len(current[1][2]):
        return find_carbon(current[0])
    return find_carbon(current[1])


numbers: list
with open('input.txt', 'r') as f:
    numbers = list(f)

tree = []
frequencies = []
bitmask = 0
for i, item in enumerate(numbers):
    item = item.strip()
    if i == 0:
        frequencies = [[0, 0] for _ in item]
        init_tree(0, len(item), tree)
        for _ in item:
            bitmask <<= 1
            bitmask += 1
    branch = tree
    for frequency, bit in zip(frequencies, item):
        frequency[int(bit)] += 1
        branch = branch[int(bit)]
        branch[2].append(item)

gamma = 0
for zeros, ones in frequencies:
    gamma <<= 1
    if zeros > ones:
        gamma += 1

epsilon = ~gamma & bitmask
part_1 = gamma * epsilon
print(f'Part 1 {part_1}')

oxygen = int('0b' + find_oxygen(tree), 2)
carbon = int('0b' + find_carbon(tree), 2)
part_2 = oxygen * carbon
print(f'Part 2 {part_2}')