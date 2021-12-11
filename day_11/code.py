from copy import deepcopy
from pprint import pprint as pp

adjacent_positions = (
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 1),
)

part_1 = 0
part_2 = 100

with open('input.txt', 'r') as f:
    octopuses = [[0] + list(map(int, line)) + [0] for line in f.read().strip().split('\n')]
    octopuses = [[0] * len(octopuses[0])] + octopuses + [[0] * len(octopuses[0])]


for _ in range(100):
    for i in range(1, len(octopuses) - 1):
        for j in range(1, len(octopuses) - 1):
            octopuses[i][j] += 1
    while True:
        next_octopuses = deepcopy(octopuses)
        for i in range(1, len(octopuses) - 1):
            for j in range(1, len(octopuses) - 1):
                if next_octopuses[i][j] >= 10:
                    next_octopuses[i][j] = 0
                    part_1 += 1
                    for h, v in adjacent_positions:
                        if next_octopuses[i + h][j + v] != 0:
                            next_octopuses[i + h][j + v] += 1
        _octopuses = deepcopy(octopuses)
        octopuses = deepcopy(next_octopuses)
        if next_octopuses == _octopuses:
            break

while True:
    if all(
        [not any(line) for line in octopuses]
    ):
        break
    for i in range(1, len(octopuses) - 1):
        for j in range(1, len(octopuses) - 1):
            octopuses[i][j] += 1
    while True:
        next_octopuses = deepcopy(octopuses)
        for i in range(1, len(octopuses) - 1):
            for j in range(1, len(octopuses) - 1):
                if next_octopuses[i][j] >= 10:
                    next_octopuses[i][j] = 0
                    for h, v in adjacent_positions:
                        if next_octopuses[i + h][j + v] != 0:
                            next_octopuses[i + h][j + v] += 1
        _octopuses = deepcopy(octopuses)
        octopuses = deepcopy(next_octopuses)
        if next_octopuses == _octopuses:
            break
    part_2 += 1

print(f'Part 1: {part_1}')
print(f'Part 2: {part_2}')
