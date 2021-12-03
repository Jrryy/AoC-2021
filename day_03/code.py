numbers = None
with open('input.txt', 'r') as f:
    numbers = list(f)

frequencies = []
bitmask = 0
for i, item in enumerate(numbers):
    item = item.strip()
    if i == 0:
        frequencies = [[0, 0] for _ in item]
        for _ in item:
            bitmask <<= 1
            bitmask += 1
    for frequency, bit in zip(frequencies, item):
        frequency[int(bit)] += 1

gamma = 0
for zeros, ones in frequencies:
    gamma <<= 1
    if zeros > ones:
        gamma += 1

epsilon = ~gamma & bitmask
part_1 = gamma * epsilon
print(f'Part 1 {part_1}')

