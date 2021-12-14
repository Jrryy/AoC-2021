transformations = {}

with open('input.txt', 'r') as f:
    list_f = list(f)
    template = list_f[0].strip()
    for pair, element in map(lambda x: x.strip().split(' -> '), list_f[2:]):
        transformations[pair] = element

for _ in range(10):
    new_template = ''
    for i in range(len(template) - 1):
        new_template += template[i] + transformations[template[i:i + 2]]
    template = new_template + template[-1]

chars_frequence = sorted([template.count(x) for x in set(template)])

print(f'Part 1: {chars_frequence[-1] - chars_frequence[0]}')

for _ in range(30):
    new_template = ''
    for i in range(len(template) - 1):
        new_template += template[i] + transformations[template[i:i + 2]]
    template = new_template + template[-1]

chars_frequence = sorted([template.count(x) for x in set(template)])

print(f'Part 2: {chars_frequence[-1] - chars_frequence[0]}')