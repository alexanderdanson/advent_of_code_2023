data = open("input.txt", "r").read().splitlines()


def parse_line(line):
    card_id = [int(n) for n in line.split(":")[0].split(" ") if n.isnumeric()][0]
    winning_numbers = [n for n in line.split(":")[1].split("|")[0].strip().split(" ") if n]
    card_numbers = [n for n in line.split(":")[1].split("|")[1].strip().split(" ") if n]
    return winning_numbers, card_numbers, card_id


def get_match_count(card_numbers, winning_numbers):
    match_count = 0
    for n in card_numbers:
        if n in winning_numbers:
            match_count += 1
    return match_count


def get_score(match_count):
    if match_count:
        score = 2 ** (match_count - 1)
    else:
        score = 0
    return score


def part1():
    scores = []
    for line in data:
        winning_numbers, card_numbers, card_id = parse_line(line)
        scores.append(get_score(get_match_count(card_numbers, winning_numbers)))
    print(int(sum(scores)))


def part2():
    card_quantities = {}
    for i in range(1, len(data) + 1):
        card_quantities[i] = 1
    for line in data:
        winning_numbers, card_numbers, card_id = parse_line(line)
        number_of_matches = get_match_count(card_numbers, winning_numbers)
        for n in range(card_id + 1, card_id + number_of_matches + 1):
            card_quantities[n] += card_quantities[card_id]
    print(sum(card_quantities.values()))


part1()
part2()



