def find_bingo(cards: list, found: list, won: list, numbers: list) -> tuple:
    part_1_result = 0
    for n in numbers:
        for card_index, card in enumerate(cards):
            for line_index, line in enumerate(card):
                if n in line:
                    n_index = line.index(n)
                    found[card_index][line_index][n_index] = True
                    if (
                        all(found[card_index][line_index])
                        or all([found_line[n_index] for found_line in found[card_index]])
                    ):
                        won[card_index] = True
                        if not part_1_result or all(won):
                            not_found_numbers = []
                            for bingo_line_index, bingo_line in enumerate(card):
                                for bingo_number_index, bingo_number in enumerate(bingo_line):
                                    if not found[card_index][bingo_line_index][bingo_number_index]:
                                        not_found_numbers.append(bingo_number)
                            if not part_1_result:
                                part_1_result = sum(map(int, not_found_numbers)) * int(n)
                            else:
                                return part_1_result, sum(map(int, not_found_numbers)) * int(n)


_cards = [[]]
_found = [[]]

with open('input.txt', 'r') as f:
    _numbers = f.readline().strip().split(',')
    f.readline()

    i = 0
    for line in f:
        stripped_line = line.strip()
        if not stripped_line:
            _cards.append([])
            _found.append([])
            i += 1
            continue
        _cards[i].append(stripped_line.split())
        _found[i].append([False] * 5)
_won = [False] * (i + 1)

part_1, part_2 = find_bingo(_cards, _found, _won, _numbers)
print(f'Part 1: {part_1}')
print(f'Part 2: {part_2}')
