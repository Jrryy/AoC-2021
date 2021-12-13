dots = set()
dots_every_step = []

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            break

        dots.add(tuple(map(int, line.split(','))))

    for line in f:
        axis, coord = line.strip()[11:].split('=')
        coord = int(coord)
        axis = 1 if axis == 'y' else 0

        next_dots = set()
        for dot in dots:
            if dot[axis] > coord:
                new_dot = list(dot)
                new_dot[axis] = dot[axis] - (dot[axis] - coord) * 2
                next_dots.add(tuple(new_dot))
            else:
                next_dots.add(dot)

        dots = next_dots
        dots_every_step.append(len(dots))

print(f'Part 1: {dots_every_step[0]}')

print('Part 2:')
for j in range(6):
    print(''.join('#' if (i, j) in dots else ' ' for i in range(39)))
