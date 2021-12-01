with open(file, 'r') as f:
    larger = 0
    larger_3 = 0

    last_measurement = None

    measurements_list = []
    last_3_sum = None

    for i, line in enumerate(f):
        measurement = int(line.strip())
        if last_measurement and measurement > last_measurement:
            larger += 1
        last_measurement = measurement

        # Part 2
        measurements_list.append(measurement)
        if len(measurements_list) > 3:
            measurements_list.pop(0)
            if sum(measurements_list) > last_3_sum:
                larger_3 += 1
        last_3_sum = sum(measurements_list)

print(f'Part 1: {larger}')
print(f'Part 2: {larger_3}')
