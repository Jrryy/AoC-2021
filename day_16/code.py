from functools import reduce
from typing import Tuple

def decode_packet(data: str, index: int) -> Tuple[int, int, int]:
    version = int(binary[index:index + 3], 2)
    type = int(binary[index + 3:index + 6], 2)
    index += 6
    if type == 4:
        keep_reading = 1
        literal = ''
        while keep_reading:
            keep_reading = int(binary[index], 2)
            literal += binary[index + 1:index + 5]
            index += 5
        final_value = int(literal, 2)
    else:
        length_type = binary[index]
        index += 1
        values = []
        if length_type == '0':
            total_length = int(binary[index:index + 15], 2)
            index += 15
            static_index = index
            while index - static_index < total_length:
                index, more_versions, value = decode_packet(data, index)
                values.append(value)
                version += more_versions
        else:
            subpackets = int(binary[index:index + 11], 2)
            index += 11
            for _ in range(subpackets):
                index, more_versions, value = decode_packet(data, index)
                values.append(value)
                version += more_versions
        if type == 0:
            final_value = sum(values)
        elif type == 1:
            final_value = reduce(lambda x, y: x*y, values, 1)
        elif type == 2:
            final_value = min(values)
        elif type == 3:
            final_value = max(values)
        elif type == 5:
            final_value = 1 if values[0] > values[1] else 0
        elif type == 6:
            final_value = 1 if values[0] < values[1] else 0
        else:
            final_value = 1 if values[0] == values[1] else 0

    return index, version, final_value

with open('input.txt', 'r') as f:
    binary = bin(int(f.read().strip(), 16))[2:]

sum_versions = 0
i = 0
_, versions, _value = decode_packet(binary, i)

print(f'Part 1: {versions}')
print(f'Part 2: {_value}')
