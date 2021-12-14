from collections import defaultdict

transformations = {}
pairs = {}

with open('input.txt', 'r') as f:
    list_f = list(f)
    template = list_f[0].strip()
    last_char = template[-1]
    for pair, element in map(lambda x: x.strip().split(' -> '), list_f[2:]):
        transformations[pair] = element
        pairs[pair] = 0

for i in range(len(template) - 1):
    pairs[template[i:i + 2]] += 1

for _ in range(10):
    new_pairs = defaultdict(int)
    for pair, frequency in pairs.items():
        inserted = transformations[pair]
        new_pairs[pair[0] + inserted] += frequency
        new_pairs[inserted + pair[1]] += frequency
    pairs = new_pairs

singles = defaultdict(int)

for pair, frequency in pairs.items():
    singles[pair[0]] += frequency

sorted_singles = sorted(singles.items(), key=lambda x: x[1])
least_frequent = sorted_singles[0][1] + 1 if sorted_singles[0][0] == last_char else sorted_singles[0][1]
most_frequent = sorted_singles[-1][1] + 1 if sorted_singles[-1][0] == last_char else sorted_singles[-1][1]

print(f'Part 1: {most_frequent - least_frequent}')

for _ in range(30):
    new_pairs = defaultdict(int)
    for pair, frequency in pairs.items():
        inserted = transformations[pair]
        new_pairs[pair[0] + inserted] += frequency
        new_pairs[inserted + pair[1]] += frequency
    pairs = new_pairs

singles = defaultdict(int)

for pair, frequency in pairs.items():
    singles[pair[0]] += frequency

sorted_singles = sorted(singles.items(), key=lambda x: x[1])
least_frequent = sorted_singles[0][1] + 1 if sorted_singles[0][0] == last_char else sorted_singles[0][1]
most_frequent = sorted_singles[-1][1] + 1 if sorted_singles[-1][0] == last_char else sorted_singles[-1][1]

print(f'Part 2: {most_frequent - least_frequent}')
