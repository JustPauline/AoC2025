answer = 0
with open('data.txt') as f:
    for line in f:
        line = line.strip()
        maxval = max(line[:-1])
        idmax = line.index(maxval)

        secmaxval = max(line[idmax + 1:])
        secidmax = line.index(secmaxval)

        joltage = maxval + secmaxval
        answer += int(joltage)

print(answer)
