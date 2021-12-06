def repopulate(p: list) -> list:
    return [
        p[1],
        p[2],
        p[3],
        p[4],
        p[5],
        p[6],
        p[7] + p[0],
        p[8],
        p[0],
    ]


with open('input.txt', 'r') as f:
    initial_items = list(map(int, f.read().strip().split(',')))
    population = [initial_items.count(item) for item in range(9)]

for _ in range(80):
    population = repopulate(population)

print(f'Part 1: {sum(population)}')

for _ in range(176):
    population = repopulate(population)

print(f'Part 2: {sum(population)}')
