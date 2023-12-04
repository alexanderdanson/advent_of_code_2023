data = open("carro_input.txt", "r").read().splitlines()

max_red = 12
max_green = 13
max_blue = 14


def parse_line(line):
    game_id = int(line.split(":")[0].split(" ")[-1])
    handfuls = [handful.strip() for handful in line.split(":")[1].split(";")]
    return game_id, handfuls


def check_possible(handfuls):
    max_recorded_per_colour = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    for handful in handfuls:
        cubes_picked = [c.strip() for c in handful.split(",")]
        for cube_colour in cubes_picked:
            quantity = int(cube_colour.split(" ")[0])
            colour = cube_colour.split(" ")[1]
            if quantity > max_recorded_per_colour[colour]:
                max_recorded_per_colour[colour] = quantity
    #print(max_recorded_per_colour)

    if (max_recorded_per_colour["red"] > max_red) or (max_recorded_per_colour["blue"] > max_blue) or (max_recorded_per_colour["green"] > max_green):
        return False
    return True


def get_power(handfuls):
    max_recorded_per_colour = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    for handful in handfuls:
        cubes_picked = [c.strip() for c in handful.split(",")]
        for cube_colour in cubes_picked:
            quantity = int(cube_colour.split(" ")[0])
            colour = cube_colour.split(" ")[1]
            if quantity > max_recorded_per_colour[colour]:
                max_recorded_per_colour[colour] = quantity
    #print(max_recorded_per_colour)

    return max_recorded_per_colour["red"] * max_recorded_per_colour["blue"] * max_recorded_per_colour["green"]


def part1():
    possible_game_ids = []
    for line in data:
        game_id, handfuls = parse_line(line)
        if check_possible(handfuls):
            possible_game_ids.append(game_id)
    print(sum(possible_game_ids))


def part2():
    powers = []
    for line in data:
        game_id, handfuls = parse_line(line)
        powers.append(get_power(handfuls))

    print(sum(powers))


part1()
part2()