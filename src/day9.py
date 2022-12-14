with open("../input/day9.input") as f:
    lines = f.read().splitlines()


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_vector(self, other):
        return Pos(abs(self.x - other.x), abs(self.y - other.y))

    def is_adjacent(self, other):
        if self == other:
            return True
        distance = self.distance_vector(other)
        if distance in DIRS:
            return True
        return False

    def is_two_steps_away(self, other):
        distance = self.distance_vector(other)
        if (distance.x == 0 and distance.y <= 2) or (distance.x <= 2 and distance.y == 0):
            return True
        else:
            return False

    def norm(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"(x={self.x}, y={self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

NORTH = Pos(-1, 0)
SOUTH = Pos(1, 0)
WEST = Pos(0, -1)
EAST = Pos(0, 1)

NW = NORTH + WEST
NE = NORTH + EAST
SW = SOUTH + WEST
SE = SOUTH + EAST

DIRS = {NORTH, SOUTH, WEST, EAST, NW, NE, SW, SE}
DIRECTION_MAP = {'R': EAST, 'L': WEST, 'U': NORTH, 'D': SOUTH}
VH_DIRS = [NORTH, SOUTH, WEST, EAST]
DIAG_DIRS = [NW, NE, SW, SE]

n_knots = 10
starting_pos = Pos(0, 0)
rope = [starting_pos for _ in range(n_knots)]

position_visited = {starting_pos}


def update_tail_position(head: Pos, tail: Pos, tail_index: int):
    h = head
    t = tail
    if h.is_adjacent(t):
        # do nothing
        pass
    elif h.is_two_steps_away(t):
        for dir in VH_DIRS:
            if h.is_adjacent(t + dir):
                t += dir
                break
    else:
        for dir in DIAG_DIRS:
            if h.is_adjacent(t + dir):
                t += dir
                break
    if tail_index == n_knots:
        position_visited.add(t)
    return h, t


VERBOSE = False

for line in lines:
    direction, n = line.split(" ")
    print(direction, "-->", n)
    direction = DIRECTION_MAP[direction]
    n = int(n)

    for _ in range(n):
        rope[0] += direction
        for ii in range(0, len(rope)-1):
            head, tail = rope[ii:ii+2]
            if VERBOSE:
                print(f"- head = {head}, tail = {tail}")
            head, tail = update_tail_position(head, tail, ii+2)
            if VERBOSE:
                print(f"--- New head = {head}, tail = {tail}")
            rope[ii:ii+2] = [head, tail]

print(len(position_visited))
