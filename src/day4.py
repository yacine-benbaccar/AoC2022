with open("../input/day4.input") as f:
    lines = f.read().splitlines()


def generate_ranges(lst):
    output = []
    for e in lst:
        (low, high) = e.split("-")
        output.append(set(range(int(low), int(high)+1)))
    return output


def check_sub_set(a, b):
    return a.issubset(b) or a.issuperset(b)

def check_overlap(a, b):
    return len(a & b) > 0


final_count = 0
overlap_count = 0
for pair in lines[:]:
    a,b = generate_ranges(pair.split(","))
    final_count = final_count + check_sub_set(a,b)
    overlap_count = overlap_count + check_overlap(a, b)

print("PART 1")
print(final_count)

print("PART 2")
print(overlap_count)