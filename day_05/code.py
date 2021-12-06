field = [['.'] * 1000 for _ in range(1000)]
field_diagonals = [['.'] * 1000 for _ in range(1000)]

count = count_diagonals = 0

with open('input.txt', 'r') as f:
    for line in f:
        diagonal = False
        x1, y1, x2, y2 = map(int, ','.join(line.split(' -> ')).split(','))
        if y1 == y2:
            if x1 < x2:
                r_x = range(x1, x2 + 1)
            else:
                r_x = range(x2, x1 + 1)
            r_y = range(y1, y1 + 1)
        elif x1 == x2:
            if y1 < y2:
                r_y = range(y1, y2 + 1)
            else:
                r_y = range(y2, y1 + 1)
            r_x = range(x1, x1 + 1)
        else:
            diagonal = True
            if x1 > x2:
                r_x = range(x1, x2 - 1, -1)
            else:
                r_x = range(x1, x2 + 1)
            if y1 > y2:
                r_y = range(y1, y2 - 1, -1)
            else:
                r_y = range(y1, y2 + 1)

        if diagonal:
            for x, y in zip(r_x, r_y):
                if field_diagonals[x][y] == '.':
                    field_diagonals[x][y] = 'o'
                elif field_diagonals[x][y] == 'o':
                    field_diagonals[x][y] = 'X'
                    count_diagonals += 1
        else:
            for x in r_x:
                for y in r_y:
                    if field[x][y] == '.':
                        field[x][y] = 'o'
                    elif field[x][y] == 'o':
                        field[x][y] = 'X'
                        count += 1
                    if field_diagonals[x][y] == '.':
                        field_diagonals[x][y] = 'o'
                    elif field_diagonals[x][y] == 'o':
                        field_diagonals[x][y] = 'X'
                        count_diagonals += 1

print(f'Part 1: {count}')
print(f'Part 2: {count_diagonals}')
