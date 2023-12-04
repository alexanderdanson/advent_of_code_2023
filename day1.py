import re

data = open("starOne.txt", "r").read().splitlines()


def part1():
    numbers = []
    for line in data:
        characters = list(line)
        digits = []
        for c in characters:
            if c.isnumeric():
                digits.append(c)
        numbers.append(int(digits[0] + digits[-1]))
    print(sum(numbers))


def part2():

    numbers_as_words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    numbers = []
    for line in data:
        digits = []
        for key in numbers_as_words.keys():
            if key in line:
                p = re.compile(key)
                for m in p.finditer(line):
                    while m.start() >= len(digits):
                        digits.append(None)
                    digits[m.start()] = numbers_as_words[key]
        for i in range(len(line)):
            if line[i].isnumeric():
                while i >= len(digits):
                    digits.append(None)
                digits[i] = line[i]
        digits_cleaned = [d for d in digits if d]
        numbers.append(int(digits_cleaned[0] + digits_cleaned[-1]))
    print(sum(numbers))


part1()
part2()