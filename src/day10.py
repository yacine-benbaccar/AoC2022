with open("../input/day10.input") as f:
    lines = f.read().splitlines()

X = 1
x_register = {}
cycle_counter = 1

checkpoints = set(range(20, 240, 40))
pixel = "_"
crt = "%%%"
sprite = crt + pixel * 37
row = ""


def cycle():
    global row
    if cycle_counter in checkpoints:
        x_register[cycle_counter] = X


def cmd_interpreter(cmd):
    # returns wait_turns, register update
    if cmd == "noop":
        # do nothing\
        return 1, 0
    else:
        return 2, int(cmd.split(" ")[1])


for i in range(len(lines[:])):
    # During the cyle
    operation = lines[i]
    wait_turns, register_update = cmd_interpreter(operation)
    # end of cyle`
    for _ in range(wait_turns-1):
        cycle()
        row += sprite[(cycle_counter - 1)%40]
        cycle_counter += 1

    cycle()
    row += sprite[(cycle_counter - 1)%40]
    cycle_counter += 1
    X += register_update
    blank_line = pixel * (X-1) + crt + pixel * (38-X)
    sprite = blank_line

print(x_register)
for ii in range(0,len(row), 40):
    print(row[ii:ii+40])
print(sum([k*v for (k,v) in x_register.items()]))