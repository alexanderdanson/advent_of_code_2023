import math

data = open("input.txt", "r").read().splitlines()
max_times = [int(t) for t in data[0].split(":")[1].split(" ") if t]
record_distances = [int(d) for d in data[1].split(":")[1].split(" ") if d]


def get_possible_distances(max_time):
    possible_distances = []
    for i in range(max_time + 1):
        speed = i
        time_remaining = max_time - i
        distance_travelled = time_remaining * speed
        possible_distances.append(distance_travelled)
    return possible_distances


def check_number_of_wins(possible_distances, record_distance):
    count = 0
    for d in possible_distances:
        if d > record_distance:
            count += 1
    return count


def part1():
    wins = []
    for i in range(len(max_times)):
        wins.append(check_number_of_wins(get_possible_distances(max_times[i]), record_distances[i]))
    print(math.prod(wins))


def part2():
    time = int("".join(str(t) for t in max_times))
    record = int("".join(str(r) for r in record_distances))
    wins = check_number_of_wins(get_possible_distances(time), record)
    print(wins)


part1()
part2()
