import os


# Ceres Search

def part_1():
    current_directory = os.path.dirname(__file__)
    input_file_path = os.path.join(current_directory, "input.txt")
    with open(input_file_path) as file:
        file_data = file.read()

    word = 'XMAS'
    word_reversed = word[::-1]
    counter = 0

    lines = file_data.strip().split('\n')
    letters = [list(line) for line in lines]

    # Horizontal

    for h in lines:
        counter += h.count(word) + h.count(word_reversed)

    # Vertical

    for x in range(0, len(letters)):
        v = ''
        for y in range(0, len(letters)):
            v += letters[y][x]
        counter += v.count(word) + v.count(word_reversed)

    # Diagonal Top-Left Bottom-Right

    for x_start in range(0, len(letters)):
        d = ''
        y = 0
        for x in range(x_start, len(letters)):
            d += letters[y][x]
            y += 1
        counter += d.count(word) + d.count(word_reversed)

    for y_start in range(1, len(letters)):
        d = ''
        x = 0
        for y in range(y_start, len(letters)):
            d += letters[y][x]
            x += 1
        counter += d.count(word) + d.count(word_reversed)

    # Diagonal Bottom-Left Top-Right

    for x_start in range(0, len(letters)):
        d = ''
        y = len(letters) - 1
        for x in range(x_start, len(letters)):
            d += letters[y][x]
            y -= 1
        counter += d.count(word) + d.count(word_reversed)

    for y_start in range(len(letters) - 2, -1, -1):
        d = ''
        x = 0
        for y in range(y_start, -1, -1):
            d += letters[y][x]
            x += 1
        counter += d.count(word) + d.count(word_reversed)

    return counter


def part_1_bis():
    current_directory = os.path.dirname(__file__)
    input_file_path = os.path.join(current_directory, "input.txt")
    with open(input_file_path) as file:
        file_data = file.read()

    def propagate(position, vector, stack='XMAS'):
        if stack == '':
            return 1
        if position < 0 or position >= len(file_data):
            return 0
        if file_data[position] == stack[0]:
            return propagate(position + vector, vector, stack[1:])
        return 0

    width = file_data.find('\n')
    counter = 0

    for i in range(0, len(file_data)):
        counter += propagate(i, -1) + propagate(i, 1) + propagate(i, -(width + 1)) + propagate(i,
                                                                                               (width + 1)) + propagate(
            i,
            -1 - (
                    width + 1)) + propagate(
            i, 1 - (width + 1)) + propagate(i, (width + 1) - 1) + propagate(i, (width + 1) + 1)

    return counter


def part_2():
    current_directory = os.path.dirname(__file__)
    input_file_path = os.path.join(current_directory, "input.txt")
    with open(input_file_path) as file:
        file_data = file.read()

    word = 'MAS'
    word_reversed = word[::-1]
    counter = 0

    lines = file_data.strip().split('\n')
    letters = [list(line) for line in lines]

    for x in range(0, len(letters)):
        for y in range(0, len(letters)):
            if letters[y][x] == 'A' and 0 < x < len(letters) - 1 and 0 < y < len(letters) - 1:
                first_diagonal = letters[y - 1][x - 1] + letters[y][x] + letters[y + 1][x + 1]
                second_diagonal = letters[y + 1][x - 1] + letters[y][x] + letters[y - 1][x + 1]
                if first_diagonal.count(word) + first_diagonal.count(word_reversed) > 0 and second_diagonal.count(
                        word) + second_diagonal.count(word_reversed) > 0:
                    counter += 1

    return counter
