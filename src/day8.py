import math

with open("../input/day8.input") as f:
    lines = f.read().splitlines()


def create_grid(lines):
    grid = list()
    for line in lines:
        grid.append([int(x) for x in list(line)])
    return grid


def draw_viewability_grid(viewability_grid):
    for ii in range(len(viewability_grid)):
        line = ""
        for jj in range(len(viewability_grid[0])):
            if viewability_grid[ii][jj]:
                line += "T"
            else:
                line += "F"
        print(line)


def gird_viewability(grid):
    def _is_tree_on_edge(x, y):
        if x == 0 or x == len(grid):
            return True
        if y == 0 or y == len(grid[x]):
            return True
        return False

    def _is_pos_in_grid(x, y):
        if (0 <= x < len(grid)) and (0 <= y < len(grid[0])):
            return True
        return False

    def _check_tree_viewable(tree_x, tree_y):
        if _is_tree_on_edge(tree_x, tree_y):
            return True

        dirs = [
            (0, -1),  # LEFT
            (0, 1),  # RIGHT
            (-1, 0),  # UP
            (1, 0)  # DOWN
        ]

        for dir in dirs:
            curr_x, curr_y = tree_x + dir[0], tree_y + dir[1]
            viewable = True
            while _is_pos_in_grid(curr_x, curr_y):
                if grid[tree_x][tree_y] > grid[curr_x][curr_y]:
                    curr_x, curr_y = curr_x + dir[0], curr_y + dir[1]
                else:
                    viewable = False
                    break
            if viewable:
                return True

        return False

    def _compute_scenic_distance(tree_x, tree_y):
        if _is_tree_on_edge(tree_x, tree_y):
            return 0

        dirs = [
            (0, -1),  # LEFT
            (0, 1),  # RIGHT
            (-1, 0),  # UP
            (1, 0)  # DOWN
        ]

        scores = [0] * len(dirs)
        for idx, dir in enumerate(dirs):
            curr_x, curr_y = tree_x + dir[0], tree_y + dir[1]
            while _is_pos_in_grid(curr_x, curr_y):
                if grid[tree_x][tree_y] > grid[curr_x][curr_y]:
                    scores[idx] += 1
                    curr_x, curr_y = curr_x + dir[0], curr_y + dir[1]
                else:
                    scores[idx] += 1
                    break
        return math.prod(scores)

    def _solve():
        cols = len(grid[0])
        _grid_viewability = [[False] * cols for _ in range(len(grid))]
        _scenic_distance_grid = [[0] * cols for _ in range(len(grid))]

        count = 0
        max_scenic_distance = -1
        for ii in range(len(grid)):
            for jj in range(len(grid[0])):
                _grid_viewability[ii][jj] = _check_tree_viewable(ii, jj)
                _scenic_distance_grid[ii][jj] = _compute_scenic_distance(ii, jj)
                count += _grid_viewability[ii][jj]
                max_scenic_distance = max(max_scenic_distance, _scenic_distance_grid[ii][jj])
        return _grid_viewability, count, _scenic_distance_grid, max_scenic_distance

    return _solve()


viewability_grid, count, scenic_distance_grid, max_scenic_distance = gird_viewability(create_grid(lines))
print(count, max_scenic_distance)
# draw_viewability_grid(viewability_grid)
