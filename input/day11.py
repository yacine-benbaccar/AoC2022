import math

with open("../input/day11.input") as f:
    lines = f.read().splitlines()

op = {'+': lambda x, y: x + y,
      '*': lambda x, y: x * y}


class Monkey:

    def __init__(self, id):
        self.id = id
        self.items = list()
        self.optionT = None
        self.optionF = None
        self.test = 0
        self.operator = ""
        self.element = None
        self.n_inspection = 0

    def _get_element(self, item):
        if self.element is None:
            return item
        return self.element

    def _inc_inspection(self):
        self.n_inspection += 1

    def update_stress_for_item(self, modulo):
        for idx, item in enumerate(self.items):
            new = op[self.operator](item, self._get_element(item)) % modulo
            self.items[idx] = new
            self._inc_inspection()

    def throw_items_to_monkey(self):
        for item in self.items:
            if not item % self.test:
                self.optionT.items.append(item)
            else:
                self.optionF.items.append(item)
        self.items = list()

    def __str__(self):
        return f"id = {self.id}, items = {self.items}, test = {self.test}, operator = {self.operator}, element = {self.element}, " + \
            f"option T = {self.optionT.id}, option F = {self.optionF.id}, n_inspection = {self.n_inspection}"


def parse_input(n_monkeys=8):
    monkeys = {i: Monkey(i) for i in range(n_monkeys)}

    current_monkey = None
    for line in lines:
        if line.startswith("Monkey "):
            current_monkey = monkeys[int(line[len("Monkey ")])]
        if line.startswith("  Starting items:"):
            items = [int(e) for e in line[len("  Starting items:"):].split(",")]
            current_monkey.items = items
        if line.startswith("  Operation:"):
            x = line[len("  Starting items:"):].split(" ")
            current_monkey.operator = x[2]
            if x[3] == "old":
                current_monkey.element = None
            else:
                current_monkey.element = int(x[3])
        if line.startswith("  Test:"):
            current_monkey.test = int(line.split(" ")[-1])
        if line.startswith("    If true:"):
            current_monkey.optionT = monkeys[int(line.split(" ")[-1])]
        if line.startswith("    If false:"):
            current_monkey.optionF = monkeys[int(line.split(" ")[-1])]
    return monkeys


monkeys_map = parse_input(n_monkeys=8)
n_rounds = 10000

modulo1 = 3
modulo2 = math.prod([e.test for _, e in monkeys_map.items()])

for _ in range(n_rounds):
    for id, m in monkeys_map.items():
        m.update_stress_for_item(modulo2)
        m.throw_items_to_monkey()

monkey_business = sorted([e.n_inspection for _, e in monkeys_map.items()], reverse=True)[:2]
for id, m in monkeys_map.items():
    print(m)

print(math.prod(monkey_business))
