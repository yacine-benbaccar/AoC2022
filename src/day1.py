with open("../input/day1.input") as f:
    lines = f.read().splitlines()

elves = list()
ii = 0
acc = 0
max_value = -1
max_ii = -1

while ii < len(lines):
    if lines[ii] != "":
        acc = acc + int(lines[ii])

    else:
        if acc > max_value:
            max_value = acc
            max_ii = len(elves)
        elves.append(acc)
        acc = 0

    ii = ii + 1

print("PART 1")
print(elves[max_ii])

print("PART 2")
print(sum(sorted(elves, reverse=True)[:3]))