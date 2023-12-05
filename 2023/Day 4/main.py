with open("in.txt") as file:
    grand = 0
    for line in file.readlines():
        line = line.strip().split(':')[1].split('|')
        winners = [int(x) for x in line[0].split()]
        mine = [int(x) for x in line[1].split()]
        total = 0.5
        for winner in winners:
            if winner in mine:
                total *= 2
        if total >= 1:
            grand += int(total)
print(grand)

with open("in.txt") as file:
    games = []
    for line in file.readlines():
        line = line.strip().split(':')[1].split('|')
        winners = [int(x) for x in line[0].split()]
        mine = [int(x) for x in line[1].split()]
        games.append([winners, mine, 1])

    for number, game in enumerate(games):
        total = 0
        for winner in game[0]:
            if winner in game[1]:
                total += 1
        if total >= 1:
            for n in range(int(total)):
                if number + n + 1 < len(games):
                    games[number + n + 1][2] += game[2]

total = 0
for game in games:
    total += game[2]
print(total)
