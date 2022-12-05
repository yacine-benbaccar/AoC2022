with open("../input/day3.input") as f:
    lines = f.read().splitlines()


def get_priority_from_ascii(char):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


final_priority = 0
for items in lines[:]:
    shared = set(items[:len(items)//2]) & set(items[len(items)//2:])
    final_priority = final_priority + get_priority_from_ascii(list(shared)[0])

print("PART 1")
print(final_priority)

print("PART 2")

final_priority2 = 0
for ii in range(0, len(lines), 3):
    x = [set(jj) for jj in lines[ii:ii+3]]
    badge = list(x[0] & x[1] & x[2])[0]
    print(badge)
    final_priority2 = final_priority2 + get_priority_from_ascii(badge)
print(final_priority2)
