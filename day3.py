data = open("carro_input.txt", "r").read().splitlines()

width = len(data[0])
height = len(data)

symbol_coordinates = []
star_coordinates = []

for y in range(height):
    for x in range(width):
        if (not data[y][x].isnumeric()) & (data[y][x] != "."):
            symbol_coordinates.append((x, y))
            if data[y][x] == "*":
                star_coordinates.append((x,y))

numbers = {

}

for y in range(height):
    next_number = []
    starting_coordinate = ()
    for x in range(width):
        if data[y][x].isnumeric():
            if not next_number:
                starting_coordinate = (x, y)
                next_number.append(data[y][x])
            else:
                next_number.append(data[y][x])
        else:
            if next_number:
                numbers[starting_coordinate] = int("".join(next_number))
                next_number = []
    if next_number:
        numbers[starting_coordinate] = int("".join(next_number))


def get_adjacent_coordinates(first_coordinate, number_of_digits):
    adjacent_coordinates = []
    if (first_coordinate[0] + number_of_digits) < width:
        adjacent_coordinates.append((first_coordinate[0] + number_of_digits, first_coordinate[1]))
    if (first_coordinate[0] - 1) >= 0:
        adjacent_coordinates.append((first_coordinate[0] - 1, first_coordinate[1]))
    if first_coordinate[1] + 1 < height:
        possible_coordinates_on_next_row = range(first_coordinate[0] - 1, first_coordinate[0] + number_of_digits + 1)
        for n in possible_coordinates_on_next_row:
            if (n >= 0) & (n < width):
                adjacent_coordinates.append((n, first_coordinate[1] + 1))
    if first_coordinate[1] - 1 >= 0:
        possible_coordinates_on_next_row = range(first_coordinate[0] - 1, first_coordinate[0] + number_of_digits + 1)
        for n in possible_coordinates_on_next_row:
            if (n >= 0) & (n < width):
                adjacent_coordinates.append((n, first_coordinate[1] - 1))
    return adjacent_coordinates


def check_for_symbol(adjacent_coordinates):
    for coordinate in adjacent_coordinates:
        if coordinate in symbol_coordinates:
            return True
    return False


def part1():
    part_numbers = []
    for coordinate in numbers:
        adjacent_coordinates = get_adjacent_coordinates(coordinate, len(str(numbers[coordinate])))
        if check_for_symbol(adjacent_coordinates):
            part_numbers.append(numbers[coordinate])

    print(sum(part_numbers))


def part2():
    number_locations = {}
    gear_ratios = []

    for number in numbers:
        for i in range(len(str(numbers[number]))):
            number_locations[(number[0] + i, number[1])] = number

    for star in star_coordinates:
        nearby_numbers = set()
        adjacent_coordinates = get_adjacent_coordinates(star, 1)
        for coordinate in adjacent_coordinates:
            if coordinate in number_locations:
                nearby_numbers.add(number_locations[coordinate])
        if len(nearby_numbers) == 2:
            gear_ratio = numbers[list(nearby_numbers)[0]] * numbers[list(nearby_numbers)[1]]
            gear_ratios.append(gear_ratio)
    print(sum(gear_ratios))


part1()
part2()