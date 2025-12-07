dial = 50
count = 0
with open('data.txt') as f:
    for line in f:
        if line[0] == "R":
            dial += int(line[1:])
            if dial > 99:
                count += dial // 100
        if line[0] == "L":
            if dial == 0:
                count -= 1
            dial -= int(line[1:])
            d = dial
            while d <= 0:
                d += 100
                count += 1
        dial = dial % 100

print(count)

