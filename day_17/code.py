from math import sqrt
from itertools import product

with open('input.txt', 'r') as f:
    x, y = f.read().strip()[15:].split(', ')

x, X = tuple(map(int, x.split('..')))
y, Y = tuple(map(int, y[2:].split('..')))

print(f'Part 1: {(-y * (-y - 1)) // 2}')

area = ((X - x) + 1) * (abs(Y - y) + 1)

upper_y = -y
lower_y = Y
rightmost_x = X // 2
leftmost_x = int(sqrt(x))
count = 0

for initial_i, initial_j in product(range(leftmost_x, rightmost_x + 1), range(lower_y, upper_y + 1)):
    current_pos = (0, 0)
    i = initial_i
    j = initial_j
    while current_pos[0] <= X and current_pos[1] >= y:
        current_pos = current_pos[0] + i, current_pos[1] + j
        if x <= current_pos[0] <= X and y <= current_pos[1] <= Y:
            count += 1
            break
        i = max(0, i - 1)
        j -= 1

print(f'Part 2: {count + area}')
