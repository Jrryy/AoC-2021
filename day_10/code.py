match = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
points = {
    ')': (3, 1),
    ']': (57, 2),
    '}': (1197, 3),
    '>': (25137, 4),
}

part_1 = 0
part_2_scores = []

with open('input.txt', 'r') as f:
    for line in f:
        stack = []
        corrupted = False
        for char in line.strip():
            if char in match:
                stack.append(char)
                continue
            last_opened = stack.pop()
            if char != match[last_opened]:
                part_1 += points[char][0]
                corrupted = True
        if not corrupted:
            score = 0
            while stack:
                last_opened = stack.pop()
                score = score * 5 + points[match[last_opened]][1]
            part_2_scores.append(score)

print(f'Part 1: {part_1}')
print(f'Part 2: {sorted(part_2_scores)[len(part_2_scores)//2]}')
