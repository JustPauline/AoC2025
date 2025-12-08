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
        L = len(number)
        for i in range(1, L//2 + 1):
            if L % i == 0:
                chunk = number[:i]
                if chunk * (L//i) == number:
                    answer += low
                    break
        low += 1
print(answer)