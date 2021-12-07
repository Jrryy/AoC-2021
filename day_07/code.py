with open('input.txt', 'r') as f:
    pos = list(map(int, f.read().strip().split(',')))
    
    median = sorted(pos)[len(pos)//2 - 1]
    total = sum([abs(median - x) for x in pos])
    print(f'Part 1: {total}')

    mean = sum(pos)/len(pos)
    mean_floor = int(mean)
    mean_rounded = round(mean)
    total_floor = int(sum([0.5*abs(mean_floor - x)*(abs(mean_floor - x) + 1) for x in pos]))
    total_rounded = int(sum([0.5*abs(mean_rounded - x)*(abs(mean_rounded - x) + 1) for x in pos]))
    print(f'Part 2: {min(total_floor, total_rounded)}')