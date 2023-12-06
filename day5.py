data = open("input.txt", "r").read().splitlines()

seeds = [int(s) for s in data[0].split(":")[1].split(" ") if s]
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

maps = [seed_to_soil, soil_to_fertilizer, fertilizer_to_water,
        water_to_light, light_to_temperature, temperature_to_humidity, humidity_to_location]

seed_starting_points = []
seed_range_lengths = []

for i in range(len(seeds)):
    if i % 2 == 0:
        seed_starting_points.append(seeds[i])
    else:
        seed_range_lengths.append(seeds[i])


def collect_rules(index, map_name):
    index += 1
    while data[index]:
        destination_range_start = int(data[index].split(" ")[0])
        source_range_start = int(data[index].split(" ")[1])
        range_length = int(data[index].split(" ")[2])
        map_name.append([destination_range_start, source_range_start, range_length])
        index += 1
        if index == len(data):
            break


for i in range(len(data)):
    if data[i] == "seed-to-soil map:":
        collect_rules(i, seed_to_soil)
    elif data[i] == "soil-to-fertilizer map:":
        collect_rules(i, soil_to_fertilizer)
    elif data[i] == "fertilizer-to-water map:":
        collect_rules(i, fertilizer_to_water)
    elif data[i] == "water-to-light map:":
        collect_rules(i, water_to_light)
    elif data[i] == "light-to-temperature map:":
        collect_rules(i, light_to_temperature)
    elif data[i] == "temperature-to-humidity map:":
        collect_rules(i, temperature_to_humidity)
    elif data[i] == "humidity-to-location map:":
        collect_rules(i, humidity_to_location)


def get_next_value(seed_number, rule_set):
    for rule in rule_set:
        if seed_number in range(rule[1], rule[1] + rule[2]):
            return seed_number - (rule[1] - rule[0])
    return seed_number


def part1():
    locations = []
    for seed in seeds:
        location = seed
        for m in maps:
            location = get_next_value(location, m)
        locations.append(location)

    print(min(locations))


def part2():
    locations = []
    all_seeds = []
    for j in range(len(seed_starting_points)):
        seed_starting_point = seed_starting_points[j]
        range_length = seed_range_lengths[j]
        all_seeds.extend(range(seed_starting_point, seed_starting_point + range_length))
        print(j)
    print(len(all_seeds))
    for seed in all_seeds:
        location = seed
        for m in maps:
            location = get_next_value(location, m)
        locations.append(location)

    print(min(locations))


part1()
part2()

