from enum import Enum

with open("../input/day7.input") as f:
    lines = f.read().splitlines()

total_disk_space = 70000000
update_space = 30000000


class Type(Enum):
    DIR = 'dir'
    FILE = 'file'


class Node:
    def __init__(self, type: Type, name: str, parent, size: int = 0):
        self.type = type
        self.name = name
        self.children = list()
        self.size = size
        self.Parent = parent

    def __str__(self):
        return f"- {self.name} ({self.type}, size={self.size})"

    def has_size_under_threshold(self, threshold):
        return self.size <= threshold


def is_command(line):
    return line[0] == "$"


def get_command_type(line):
    l = line.split(" ")
    if "ls" == l[1]:
        return "ls", None
    else:
        return "cd", l[2]


def get_node(line: str, parent: Node) -> Node:
    data = line.split(" ")
    if "dir" in data:
        return Node(Type.DIR, name=data[1], parent=parent)
    else:
        return Node(Type.FILE, name=data[1], size=int(data[0]), parent=parent)


def create_graph(lines: str) -> Node:
    root = Node(type=Type.DIR, name="/", parent=None)
    currentNode = root
    for l in lines[1:]:
        if is_command(l):
            cmd, dir = get_command_type(l)
            if cmd == "cd":
                if dir == "..":
                    currentNode = currentNode.Parent
                else:
                    # search for the node
                    for node in currentNode.children:
                        if node.type == Type.DIR and node.name == dir:
                            currentNode = node
            else:
                continue
        else:
            newNode = get_node(l, currentNode)
            currentNode.children.append(newNode)
    return root


def compute_dir_size(root: Node):
    if root.type == Type.FILE:
        return root.size
    else:
        size = 0
        for n in root.children:
            size += compute_dir_size(n)
        root.size = size
        return size


def draw_file_system(root: Node, nb_indents=0):
    line = "  " * nb_indents + root.__str__()
    print(line)
    for c in root.children:
        draw_file_system(c, nb_indents=nb_indents + 1)


def solution(root: Node, disk_space_to_clean):
    acc = 0
    candidate_for_deletion = []

    def _part1_solution(root: Node, threshold=100000):
        nonlocal acc
        if root.type == Type.DIR:
            if root.has_size_under_threshold(threshold): acc += root.size
            for c in root.children:
                _part1_solution(c)

    def _part2_solution(root: Node, space_needed=disk_space_to_clean):
        nonlocal candidate_for_deletion
        if root.type == Type.DIR:
            if root.size >= space_needed: candidate_for_deletion.append(root)
            for c in root.children:
                _part2_solution(c)

    _part1_solution(root)
    _part2_solution(root)

    n = min(candidate_for_deletion, key=lambda n: n.size)

    return acc, n


root = create_graph(lines)
compute_dir_size(root)
print("File System:")
draw_file_system(root)

used_disk_space = root.size
free_disk_space = total_disk_space - used_disk_space
space_to_liberate = update_space - free_disk_space
part1, part2 = solution(root, space_to_liberate)

print("PART 1")
print(f"{part1}")
print("PART 2")
print(f"need to free {total_disk_space - used_disk_space}")
print(f"Smallest dir to delete -> {part2}")