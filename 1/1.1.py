dial = 50
count = 0
with open('data.txt') as f:
    for line in f:
        if line[0] == "R":
            dial += int(line[1:])
        if line[0] == "L":
            dial -= int(line[1:])
        dial = dial % 100
        if dial == 0:
            count += 1

print(count)

