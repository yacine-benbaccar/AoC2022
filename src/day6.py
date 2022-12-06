with open("../input/day6.input") as f:
    lines = f.read().splitlines()

marker_size_1 = 4


def find_marker_pos(line, marker_size):
    for ii in range(0, len(line)-marker_size, 1):
        if len(set(line[ii:ii+marker_size])) == marker_size:
            print(ii+marker_size, line[ii:ii+marker_size])
            break


print("PART 1")
find_marker_pos(lines[0], marker_size_1)


print("PART 2")
marker_size_2 = 14
find_marker_pos(lines[0], marker_size_2)