with open("in.txt") as file:
    numbers = []
    symbols = []
    for rowNumber, line in enumerate(file.readlines()):
        number = 0
        columns = []
        for columnNumber, c in enumerate(line.strip() + '.'):
            if '0' <= c <= '9':
                number = (10 * number) + int(c)
                columns.append(columnNumber)
            else:
                if number > 0:
                    numbers.append((rowNumber, columns, number))
                if c != '.':
                    symbols.append((rowNumber, columnNumber, c))
                number = 0
                columns = []

    total = 0
    offsets = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
    for number in numbers:
        found = False
        for symbol in symbols:
            for offset in offsets:
                location = [symbol[0] + offset[0], symbol[1] + offset[1]]
                if number[0] == location[0] and location[1] in number[1]:
                    found = True
                    total += number[2]
                    break
    print(total)

with open("in.txt") as file:
    numbers = []
    symbols = []
    for rowNumber, line in enumerate(file.readlines()):
        number = 0
        columns = []
        for columnNumber, c in enumerate(line.strip() + '.'):
            if '0' <= c <= '9':
                number = (10 * number) + int(c)
                columns.append(columnNumber)
            else:
                if number > 0:
                    numbers.append((rowNumber, tuple(columns), number))
                if c != '.':
                    symbols.append((rowNumber, columnNumber, c))
                number = 0
                columns = []

    total = 0
    offsets = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
    for symbol in symbols:
        found = set()
        for number in numbers:
            for offset in offsets:
                location = [symbol[0] + offset[0], symbol[1] + offset[1]]
                if number[0] == location[0] and location[1] in number[1]:
                    found.add(tuple(number))
                    break
        if len(found) == 2:
            value = 1
            for v in found:
                value *= v[2]
            total += value
    print(total)
