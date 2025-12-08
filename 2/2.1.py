with open('data.txt') as f:
    for line in f:
        line = line.split(",")

IDs = []

for i in range(len(line)):
    IDs.append(line[i].split("-"))

answer = 0

for ranges in IDs:
    low = int(ranges[0])
    high = int(ranges[1])
    while low <= high:
        number = str(low)
        if number[:len(number)//2] == number[len(number)//2:]:
            answer += low
        low += 1

print(answer)