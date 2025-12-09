answer = 0

with open('data.txt') as f:
    for line in f:
        line = line.strip()
        digits = 11
        joltage = ""
        idmax = -1

        while digits != 0:
            maxval = max(line[:-digits])
            idmax = line.index(maxval)

            joltage += maxval
            digits -= 1
            line = line[idmax + 1:]
        maxval = max(line)
        joltage += maxval
        answer += int(joltage)

print(answer)
