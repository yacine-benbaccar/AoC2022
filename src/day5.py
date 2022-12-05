with open("../input/day5.input") as f:
    lines = f.read().splitlines()

g_lines = lines[:8]
m_lines = lines[10:]


def populate_grid(g_lines):
    grid = [[] for _ in range(9)]
    for l in g_lines:
        for ii in range(0, len(l), 4):
            if l[ii:ii + 4][1] != " ": grid[ii // 4].append(l[ii:ii + 4][1])
    return grid


def draw_grid(grid):
    longest_col = max([len(x) for x in grid])

    for jj in range(longest_col - 1, -1, -1):
        line = ""
        for tower in grid:
            if len(tower) < jj + 1:
                line = line + "    "
            else:
                line = line + f"[{tower[::-1][jj]}] "
        print(line)
    print(" ".join([f" {e} " for e in range(1, len(grid) + 1)]))


print("PART 1")
grid = populate_grid(g_lines)
print("INITIAL GRID")
draw_grid(grid)


def get_instruction(move_line):
    return [int(e) for e in move_line.split(" ") if e.isnumeric()]


def move_blocks9000(grid, instruction):
    count, src, dst = instruction
    # move instruction
    grid[dst - 1] = grid[src - 1][:count][::-1] + grid[dst - 1]
    grid[src - 1] = grid[src - 1][count:]


# Part 2
def move_blocks9001(grid, instruction):
    count, src, dst = instruction
    # move instruction
    grid[dst - 1] = grid[src - 1][:count] + grid[dst - 1]
    grid[src - 1] = grid[src - 1][count:]


def get_top_blocks(grid):
    line = ""
    for tower in grid:
        line += tower[0]
    return line


for l in m_lines[:]:
    move_blocks9001(grid, get_instruction(l))

print("FINAL GRID")
draw_grid(grid)
print("TOP BLOCKS ->", get_top_blocks(grid))
