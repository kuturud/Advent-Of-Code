with open("in.txt") as file:
    data = []
    for line in file.readlines():
        line = line.replace("one", "o1ne")
        line = line.replace("two", "t2wo")
        line = line.replace("three", "t3hree")
        line = line.replace("four", "f4our")
        line = line.replace("five", "f5ive")
        line = line.replace("six", "s6ix")
        line = line.replace("seven", "s7even")
        line = line.replace("eight", "e8ight")
        line = line.replace("nine", "n9ine")
        line = line.replace("zero", "z0ero")
        item = []
        for character in line:
            if '0' <= character <= '9':
                item.append(int(character))
        data.append(item)

total = 0
for item in data:
    total += (10 * item[0])
    total += item[-1]

print(total)