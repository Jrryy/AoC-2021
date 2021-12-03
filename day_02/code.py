with open('input.txt', 'r') as f:
    x, y, y_2 = 0, 0, 0
    for instruction in f:
        direction, units_str = instruction.split(' ')
        units = int(units_str)
        if direction == 'forward':
            x += units
            y_2 += units * y
        elif direction == 'down':
            y += units
        elif direction == 'up':
            y -= units
    product_1 = x * y
    product_2 = x * y_2
    
    print(f'Part 1: {product_1}')
    print(f'Part 2: {product_2}')
