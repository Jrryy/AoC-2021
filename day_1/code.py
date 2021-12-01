import os

file = 'input.txt'
if os.getenv('ONLINE'):
    file = 'custom_input.txt'

with open(file, 'r') as f:
    # The two counts we want to track
    larger = 0
    larger_3 = 0
    # The last measurement to compare for part 1
    last_measurement = None
    # A list of the 3 measurements we're checking and
    # a sum of the last 3 ones for part 2
    measurements_list = []
    last_3_sum = None
    # Enumerate so that we can track if we've already seen the first 3
    for i, line in enumerate(f):
        # Convert the line to an integer
        measurement = int(line.strip())
        # Add 1 to the count if the measurement is bigger than the last one.
        if last_measurement and measurement > last_measurement:
            larger += 1
        # And replace last measurement with the current.
        last_measurement = measurement

        # Starting part 2
        # First append the new measurement to the list
        measurements_list.append(measurement)
        # If the list has more than 3 elements, we can start comparing
        if len(measurements_list) > 3:
            # Pop the first element since we only want 3
            measurements_list.pop(0)
            # Add 1 to the count if the sum of elements is bigger than the last one
            if sum(measurements_list) > last_3_sum:
                larger_3 += 1
        # Save the sum of the last 3 visited elements
        last_3_sum = sum(measurements_list)

print(f'Part 1: {larger}')
print(f'Part 2: {larger_3}')
