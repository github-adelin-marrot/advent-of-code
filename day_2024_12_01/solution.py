import os


# Historian Hysteria

def common():
    current_directory = os.path.dirname(__file__)
    input_file_path = os.path.join(current_directory, "input.txt")
    with open(input_file_path) as file:
        file_data = file.read()

    lines = file_data.strip().split('\n')
    left = list()
    right = list()

    for line in lines:
        locations = line.split()
        left.append(int(locations[0]))
        right.append(int(locations[-1]))

    left.sort()
    right.sort()

    return left, right


def part_1():
    distance = 0
    left, right = common()

    for i in range(0, len(left)):
        distance += abs(left[i] - right[i])

    return distance


def part_2():
    score = 0
    left, right = common()

    for i in range(0, len(left)):
        score += left[i] * right.count(left[i])

    return score
