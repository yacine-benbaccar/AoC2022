with open("../input/day2.input") as f:
    games = f.read().splitlines()

# Rock defeats Scissors {"Rock", "Scissors"}
# Scissors defeats Paper {"Paper", "Scissors"}
# Paper defeats Rock {"Paper", "Rock"}

symbol2Play = {
    "A": "Rock",
    "X": "Rock",
    "B": "Paper",
    "Y": "Paper",
    "C": "Scissors",
    "Z": "Scissors"
}

score = {
    "W": 6, "D": 3, "L": 0
}
play2Value = {
    "Rock": 1, "Paper": 2, "Scissors": 3
}

outcomeMap = {
    "X":"L", "Y":"D", "Z":"W"
}


def guessOutcome(game):
    opp = game[0]
    res = game[1]
    if res == "D": return opp
    if opp == "Rock":
        if res == "W": return "Paper"
        else: return "Scissors"
    if opp == "Paper":
        if res == "W": return "Scissors"
        else: return "Rock"
    if opp == "Scissors":
        if res == "W": return "Rock"
        else: return "Paper"

def rules(opp, me):
    # L if opp wins
    # W if me wins
    # D if draw
    if opp == me: return "D"
    if set([opp, me]) == {"Rock", "Scissors"}:
        if opp == "Rock":
            return "L"
        else:
            return "W"
    if set([opp, me]) == {"Paper", "Scissors"}:
        if opp == "Scissors":
            return "L"
        else:
            return "W"
    if set([opp, me]) == {"Paper", "Rock"}:
        if opp == "Paper":
            return "L"
        else:
            return "W"


def outcome(game: list):
    # player2 = me
    return play2Value[game[1]] + score[rules(game[0], game[1])]


finalScore = 0
print(len(games))
print("PART 1")
for game in games:
    g = [symbol2Play[e] for e in game.split(" ")]
    finalScore = finalScore + outcome(g)
    #print(game, "->", g, "->", outcome(g))

print(finalScore)
print("PART 2")

finalScore2 = 0
for game in games:
    g = game.split(" ")
    g = [symbol2Play[g[0]], outcomeMap[g[1]]]
    shouldPlay = guessOutcome(g)
    guessedScore = outcome([g[0], shouldPlay])
    finalScore2 = finalScore2 + guessedScore

print(finalScore2)