from collections import defaultdict
from typing import DefaultDict, List, Optional


def find_paths(
    current: str,
    caves: DefaultDict[str, List[str]],
    visited: List[str],
) -> int:
    if current == 'end':
        return 1
    return sum(
        find_paths(cave, caves, visited + [cave])
        if cave.islower()
        else find_paths(cave, caves, visited)
        for cave in caves[current] if cave not in visited
    )


def find_paths_2(
    current: str,
    caves: DefaultDict[str, List[str]],
    visited: List[str],
    double: Optional[str] = None,
) -> int:
    if current == 'end':
        return 1
    count = 0
    for cave in caves[current]:
        if cave not in visited and cave.islower():
            count += find_paths_2(cave, caves, visited + [cave], double)
        elif cave in visited and not double and cave != 'start':
            count += find_paths_2(cave, caves, visited, cave)
        elif cave.isupper():
            count += find_paths_2(cave, caves, visited, double)
    return count


_caves = defaultdict(list)

with open('input.txt', 'r') as f:
    for line in f:
        cave_1, cave_2 = line.strip().split('-')
        _caves[cave_1].append(cave_2)
        _caves[cave_2].append(cave_1)

print(f"Part 1: {find_paths('start', _caves, ['start'])}")
print(f"Part 2: {find_paths_2('start', _caves, ['start'])}")
