from typing import List


def find_basin_size(
    _heightmap: List[List[int]],
    _x: int,
    _y: int,
    visited: List[List[int]],
) -> int:
    if (
        [_x, _y] in visited
        or not 0 <= _x <= len(_heightmap) - 1
        or not 0 <= _y <= len(_heightmap) - 1
        or _heightmap[_x][_y] == 9
    ):
        return 0
    visited.append([_x, _y])
    return (
        1 +
        find_basin_size(_heightmap, _x + 1, _y, visited) +
        find_basin_size(_heightmap, _x - 1, _y, visited) +
        find_basin_size(_heightmap, _x, _y + 1, visited) +
        find_basin_size(_heightmap, _x, _y - 1, visited)
    )


with open('input.txt', 'r') as f:
    heightmap = [list(map(int, list(line.strip()))) for line in f]

low_points = []
basins = []
size = len(heightmap)
risk = 0

for i in range(size):
    for j in range(size):
        current = heightmap[i][j]
        up = heightmap[i - 1][j] if i > 0 else 10
        left = heightmap[i][j - 1] if j > 0 else 10
        down = heightmap[i + 1][j] if i < size - 1 else 10
        right = heightmap[i][j + 1] if j < size - 1 else 10
        if all((current < up, current < left, current < down, current < right)):
            risk += current + 1
            low_points.append((i, j))

for x, y in low_points:
    basins.append(find_basin_size(heightmap, x, y, []))

_1, _2, _3, *_ = sorted(basins, reverse=True)

print(f'Part 1: {risk}')
print(f'Part 2: {_1 * _2 * _3}')
