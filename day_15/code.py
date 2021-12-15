from typing import List
from copy import deepcopy

def find_best_risk(risk_map: List[List[int]]) -> List[List[int]]:
    added_risks = [[] for _ in range(len(risk_map))]

    added_first_line = 0
    for x in risk_map[0]:
        added_first_line += x
        added_risks[0].append(added_first_line)

    added_first_col = 0
    for index, line in enumerate(risk_map):
        added_first_col += line[0]
        if index == 0:
            continue
        added_risks[index].append(added_first_col)

    for i in range(1, len(risk_map)):
        for j in range(1, len(risk_map)):
            added_risks[i].append(min(
                added_risks[i - 1][j] + risk_map[i][j],
                added_risks[i][j - 1] + risk_map[i][j],
            ))

    return added_risks

def find_reversed_risks(
    added_risks_map: List[List[int]],
    risk_map: List[List[int]],
) -> None:
    for i in range(len(risk_map) - 2, -1, -1):
        for j in range(len(risk_map) - 2, -1, -1):
            added_risks_map[i][j] = min(
                added_risks_map[i][j],
                added_risks_map[i + 1][j] + risk_map[i][j],
                added_risks_map[i][j + 1] + risk_map[i][j],
            )

def find_best_risk_again(
    added_risks_map: List[List[int]],
    risk_map: List[List[int]],
) -> None:
    for i in range(1, len(risk_map)):
        for j in range(1, len(risk_map)):
            added_risks_map[i][j] = min(
                added_risks_map[i][j],
                added_risks_map[i - 1][j] + risk_map[i][j],
                added_risks_map[i][j - 1] + risk_map[i][j],
            )


with open('input.txt', 'r') as f:
    risks = [list(map(int, line.strip())) for line in f]

added_risks = find_best_risk(risks)

print(f'Part 1: {added_risks[-1][-1] - added_risks[0][0]}')

risks_len = len(risks)
risks_2 = []
for _ in range(5):
    for line in risks:
        risks_2.append(line.copy() + line.copy() + line.copy() + line.copy() + line.copy())

risks_2_len = len(risks_2)
for i in range(risks_2_len):
    for j in range(risks_2_len):
        new_risk = risks_2[i][j] + i // risks_len + j // risks_len
        if new_risk > 9:
            new_risk -= 9
        risks_2[i][j] = new_risk

added_risks_2 = find_best_risk(risks_2)
previous_map = deepcopy(added_risks_2)
while True:
    find_reversed_risks(added_risks_2, risks_2)
    find_best_risk_again(added_risks_2, risks_2)
    if previous_map == added_risks_2:
        break
    previous_map = deepcopy(added_risks_2)

print(f'Part 2: {added_risks_2[-1][-1] - added_risks_2[0][0]}')
